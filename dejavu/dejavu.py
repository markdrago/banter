import readline
import sys

import crucible
import config
import config_ui

def main():
    if sys.argv[1] == 'setup':
        return setup()

    conf = load_config()
    if conf is None:
        return 1

    crucible_url = conf.get_value('crucible', 'url')
    crucible_conn = crucible.Crucible(crucible_url)
    username = conf.get_value('crucible', 'username')
    auth_token = conf.get_value('crucible', 'token')
    project_key = conf.get_value('crucible', 'project_key')

    patch = sys.stdin.read()

    review_id = create_review(crucible_conn, username, auth_token, project_key, patch)
    print crucible_url + "/cru/" + review_id

def create_review(crucible, username, auth_token, project_key, patch):
    parameters = {
        'allow_reviewers_to_join': True,
        'author': username,
        'description': '',
        'name': '',
        'project_key': project_key,
        'patch': patch
    }

    resp = crucible.create_review(auth_token, **parameters)
    #print resp.request.data
    #print resp.text
    return resp.json['permaId']['id']

def setup():
    conf = config.Config()
    conf.load_from_file()
    config_ui.setup_config_except_auth_token(conf)

    crucible_url = conf.get_value('crucible', 'url')
    crucible_conn = crucible.Crucible(crucible_url)

    config_ui.setup_auth_token(conf, crucible_conn)

    return 0

def load_config():
    """load config, check for required fields, print error if any are missing"""
    conf = config.Config()
    conf.load_from_file()
    if not has_all_required_fields(conf):
        print "Your configuration is incomplete, please run 'dejavu setup' to get that fixed up"
        return None
    return conf

def has_all_required_fields(conf):
    for field in ('url', 'username', 'token', 'project_key'):
        if conf.get_value('crucible', field) is None:
            return False
    return True

if __name__ == '__main__':
    sys.exit(main())
