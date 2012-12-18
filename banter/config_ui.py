import getpass

def get_config_from_user(existing={}):
    cr_settings = existing.get('crucible', {})
    cr_settings['url'] = get_input("Please enter the URL for crucible:", cr_settings.get('url'))
    cr_settings['project_key'] = get_input("Please enter the crucible project key:", cr_settings.get('project_key'))
    cr_settings['username'] = get_input("Please enter your crucible username:", cr_settings.get('username'))

    reviewers_msg = "Enter a comma-separated list of usernames for anyone you'd like to include on reviews by default:"
    cr_settings['reviewers'] = get_input(reviewers_msg, cr_settings.get('reviewers'))

    cr_settings['password'] = get_crucible_password()

    existing['crucible'] = cr_settings
    return existing

def get_input(prompt, previous):
    prompt_suffix = " "
    if previous is not None:
        prompt_suffix = " [" + previous + "]"
    value = raw_input(prompt + prompt_suffix)
    if len(value) == 0:
        return previous
    return value

def get_crucible_password():
    print "In order to get an auth token from crucible, you must enter your password once."
    password = getpass.getpass()
    return password
