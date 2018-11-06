"""Default constants"""


class InitUsers:
    """Default users"""

    users = {"admin@fluxday.io": "password",
             "lead@fluxday.io": "password",
             "emp1@fluxday.io": "password",
             "emp2@fluxday.io": "password"}

    fake_user_email = "ivan@fluxday.io"
    fake_user_password = "yui123zxc"

    admin_email = "admin@fluxday.io"
    lead_email = "lead@fluxday.io"
    emp1_email = "emp1@fluxday.io"
    emp2_email = "emp1@fluxday.io"

    password = "password"


class PagesPath:
    """Pages paths"""

    login = "/users/sign_in"
    dashboard = "/"
    tasks = "/tasks"
    departsments = "/projects"
    team = "/teams"
    users = "/users"
    okr = "/okrs"
    reports = "/worklogs"
    oauth_applications = "/oauth_applications"
    admin_user = "/users/FT1"
    logout = "/users/sign_out"
