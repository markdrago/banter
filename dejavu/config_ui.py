import getpass

def setup_config_except_auth_token(conf):
    get_crucible_url(conf)
    get_project_key(conf)
    get_username(conf)

def get_crucible_url(conf):
    url = conf.get_value('crucible', 'url')
    if url is None:
        url = acquire_crucible_url()
        conf.set_value('crucible', 'url', url)

def acquire_crucible_url():
    prompt = "Please enter the URL for crucible (probably something like http://hostname.com/fisheye): "
    return raw_input(prompt)

def get_project_key(conf):
    project_key = conf.get_value('crucible', 'project_key')
    if project_key is None:
        project_key = prompt_for_project_key()
        conf.set_value('crucible', 'project_key', project_key)

def prompt_for_project_key():
    prompt = "Please enter your crucible project key (probably something like CR): "
    return raw_input(prompt)

def get_username(conf):
    username = conf.get_value('crucible', 'username')
    if username is None:
        username = prompt_for_username()
        conf.set_value('crucible', 'username', username)

def prompt_for_username():
    prompt = "Please enter your crucible username: "
    return raw_input(prompt)

def setup_auth_token(conf, crucible):
    token = conf.get_value('crucible', 'token')
    if token is None:
        username = conf.get_value('crucible', 'username')
        token = acquire_auth_token(crucible, username)
        conf.set_value('crucible', 'token', token)

def acquire_auth_token(crucible, username):
    password = prompt_for_password()
    response = crucible.get_auth_token(username, password)
    return response.json['token']

def prompt_for_password():
    print "In order to get an auth token from crucible, you must enter your password once."
    password = getpass.getpass()
    return password
