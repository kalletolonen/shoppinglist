all:
	rsync -v -r list/ shopping/ --exclude 'settings.py' --exclude 'db.sqlite3' djkallet@159.65.197.154:/home/djkallet/publicwsgi/shopping/; ssh djkallet@159.65.197.154 'source publicwsgi/env/bin/activate; ./publicwsgi/shopping/manage.py migrate; touch /home/djkallet/publicwsgi/shopping/shopping/wsgi.py'
