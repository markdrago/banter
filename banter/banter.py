import readline
import sys
import argparse

import crucible
import config
import config_ui
import utils

def main():
    parser = argparse.ArgumentParser(description='Create Code Reviews')
    parser.add_argument('--setup', action='store_true', help='setup banter configuration')
    parser.add_argument('-t', '--title', help="set title of new review")
    parser_results = vars(parser.parse_args())

    if parser_results['setup']:
        setup()
    else:
        create_review(title=parser_results['title'])

def create_review(title=''):
    conf = load_config()
    if conf is None:
        return 1

    crucible_url = conf.get_value('crucible', 'url')
    crucible_conn = crucible.Crucible(crucible_url)
    username = conf.get_value('crucible', 'username')
    auth_token = conf.get_value('crucible', 'token')
    project_key = conf.get_value('crucible', 'project_key')
    reviewers = conf.get_value('crucible', 'reviewers')

    patch = sys.stdin.read()

    review_id = do_create_review(crucible_conn, username, auth_token, project_key, patch, title)
    add_reviewers(crucible_conn, auth_token, review_id, reviewers)
    print utils.combine_url_components(crucible_url, "cru", review_id)

def do_create_review(crucible_conn, username, auth_token, project_key, patch, title=''):
    parameters = {
        'allow_reviewers_to_join': True,
        'author': username,
        'description': '',
        'name': title,
        'project_key': project_key,
        'patch': patch
    }

    resp = crucible_conn.create_review(auth_token, **parameters)
    return resp.json()['permaId']['id']

def add_reviewers(crucible_conn, auth_token, review_id, reviewers):
    if reviewers is not None and reviewers != "":
        reviewer_list = [r.strip() for r in reviewers.split(',')]
        r = crucible_conn.add_reviewers(auth_token, review_id, reviewer_list)

def setup():
    conf = config.Config()
    conf.load_from_file()
    updated_conf = config_ui.get_config_from_user(conf.as_dict())
    set_crucible_token(updated_conf)
    conf.set_from_dict(updated_conf)
    conf.save()

def set_crucible_token(conf):
    #get crucible token and forget crucible password
    crucible_conn = crucible.Crucible(conf['crucible']['url'])
    token = crucible_conn.get_auth_token(conf['crucible']['username'], conf['crucible']['password'])

    conf['crucible']['token'] = token
    del conf['crucible']['password']

def load_config():
    """load config, check for required fields, print error if any are missing"""
    conf = config.Config()
    conf.load_from_file()
    if not has_all_required_fields(conf):
        print "Your configuration is incomplete, please run 'banter setup' to get that fixed up"
        return None
    return conf

def has_all_required_fields(conf):
    for field in ('url', 'username', 'token', 'project_key'):
        if conf.get_value('crucible', field) is None:
            return False
    return True

if __name__ == '__main__':
    sys.exit(main())
