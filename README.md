# cyclone-based project for heroku and other PaaS based on foreman.

	This is the source code of ThereBeDocs
	Foo Bar <root@localhost>

## About

This file has been created automatically by cyclone-tool for ThereBeDocs.
It contains the following files:

- ``Procman``: standard foreman file
- ``ThereBeDocs.conf``: configuration file for the web server
- ``ThereBeDocs/__init__.py``: information such as author and version of this package
- ``ThereBeDocs/web.py``: map of url handlers and main class of the web server
- ``ThereBeDocs/config.py``: configuration parser for ``ThereBeDocs.conf``
- ``ThereBeDocs/views.py``: code of url handlers for the web server
- ``scripts/localefix.py``: script to fix html text before running ``xgettext``
- ``scripts/cookie_secret.py``: script for generating new secret key for the web server

### Running

For development and testing:

    gem install foreman
    cd ThereBeDocs
    foreman start

For production on any foreman based env: 
    
    Follow foreman instructions, configure Procman as needed. Check the .env file and the configuration file for your app.

For production at heroku:
    
    - Start a git repo
        git init
        git add .
        git commit -m 'first'
        heroku create ThereBeDocs (or whatever name you want)
        git push heroku master
    - check your app, make it better, create a db, etc 

### Convert this document to HTML

Well, since this is a web server, it might be a good idea to convert this document
to HTML before getting into customization details.

This can be done using [markdown](http://daringfireball.net/projects/markdown/).

	brew install markdown
	markdown README.md > frontend/static/readme.html

And point your browser to <http://localhost:8888/static/readme.html> after this server
is running.

## Customization

This section is dedicated to explaining how to customize your brand new package.

### Databases

cyclone provides built-in support for SQLite and Redis databases.
It also supports any RDBM supported by the ``twisted.enterprise.adbapi`` module,
like MySQL or PostgreSQL.

The default configuration file ``ThereBeDocs.conf`` ships with pre-configured
settings for SQLite, Redis and MySQL.

The code for loading all the database settings is in ``ThereBeDocs/config.py``.
Feel free to comment or even remove such code, and configuration entries. It
shouldn't break the web server.

Take a look at ``ThereBeDocs/utils.py``, which is where persistent database
connections are initialized.


### Internationalization

cyclone uses the standard ``gettext`` library for dealing with string
translation.

Make sure you have the ``gettext`` package installed. If you don't, you won't
be able to translate your software.

For installing the ``gettext`` package on Debian and Ubuntu systems, do this:

    apt-get install gettext

For Mac OS X, I'd suggest using [HomeBrew](http://mxcl.github.com/homebrew>).
If you already use HomeBrew, run:

    brew install gettext
    brew link gettext

For generating translatable files for HTML and Python code of your software,
run this:

    cat frontend/template/*.html ThereBeDocs/*.py | python scripts/localefix.py | \
        xgettext - --language=Python --from-code=utf-8 --keyword=_:1,2 -d ThereBeDocs

Then translate ThereBeDocs.po, compile and copy to the appropriate locale
directory:

    (pt_BR is used as example here)
    vi ThereBeDocs.po
    mkdir -p frontend/locale/pt_BR/LC_MESSAGES/
    msgfmt ThereBeDocs.po -o frontend/locale/pt_BR/LC_MESSAGES/ThereBeDocs.mo

There are sample translations for both Spanish and Portuguese in this package,
already compiled.


### Cookie Secret

The current cookie secret key in ``ThereBeDocs.conf`` was generated during the
creation of this package. However, if you need a new one, you may run the
``scripts/cookie_secret.py`` script to generate a random key.

## Credits

- [cyclone](http://github.com/fiorix/cyclone) web server.
