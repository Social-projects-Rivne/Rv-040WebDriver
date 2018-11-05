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


class InitUrls:
    """Pages"""

    login = "https://app.fluxday.io/users/sign_in"
    dashboard = "https://app.fluxday.io/"
    tasks = "https://app.fluxday.io/tasks"
    departsments = "https://app.fluxday.io/projects"
    team = "https://app.fluxday.io/teams"
    users = "https://app.fluxday.io/users"
    okr = "https://app.fluxday.io/okrs"
    reports = "https://app.fluxday.io/worklogs"
    oauth_applications = "https://app.fluxday.io/oauth_applications"
    admin_user = "https://app.fluxday.io/users/FT1"
    logout = "https://app.fluxday.io/users/sign_out"
