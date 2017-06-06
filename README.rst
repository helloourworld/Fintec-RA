Project Fintec-RA
==================
Demo of Fintec-RA

Quickstart
----------
::

    $ git clone git@github.com:helloourworld/Fintec-RA.git

    $ cd Fintec-RA

    $ virtualenv env

    $ source env/bin/activate

    $ pip install -r requirements.txt

After that, you should create your admin user, run the following command:
::

    $ ./manage.py install

and follow the instructions


Edit the settings.py and change the settings to suit your needs, sepcifically you can change Flask security settings, security keys, Mongodb settings,and Flask mail.

to run the system, you can use a management command:
::

    $ ./manage.py runserver


Features
--------
- Flask based
- Fully working user registration and authentication + user roles via Flask security and Flask Principal
- Memory caching via Redis and Flask cache
- Simple admin backend via Flask Admin
- Command line scripting via Flask Script (will be replaced by "click" in the next release)
- Automatic assets bundling and minification via Flask assets
- Mongodb and Mongoengine ORM
- Background tasks via Celery
- Email integration via Flask Mail
- Best practices by utilizing Flask blueprints and development/production configuration

License
-------
None

