Custom Django Management Commands
==================================

We can create our own commands for our apps and include them in the list by creating a management/commands directory inside an app directory

Basic Custom Command
====================

Generate a random date:
-----------------------
    python manage.py random_date
    [CODE](http://)

Handling Arguments:
-------------------
    python manage.py create_user 3
    [CODE](http://)


Optional Arguments:
-------------------
    python manage.py create_user 3 --prefix custom_user
    [CODE](http://)

Flag Arguments:
-------------------
    python manage.py create_user 3 --admin
    [CODE](http://)


Arbitary Arguments:
-------------------
    python manage.py delete_user 1
                 or
    python manage.py delete_user 1, 2, 3
    [CODE](http://)


Scheduled Management Commands:
-------------------

cron_schedule python_path manage_py_path command_name possitional_args optional_args

# m h  dom mon dow   command
0 6 * * * /home/mysite/venv/bin/python /home/mysite/mysite/manage.py custom_command