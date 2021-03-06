Installation
============

OS dependencies
---------------

**LIBRE** supports `Spatial queries <http://en.wikipedia.org/wiki/Spatial_query>`_
as such is dependant on several libraries that are installed at the OS level.

If using Ubuntu Linux install the required libraries with:

.. code-block:: bash

    $ sudo apt-get install libgdal-dev -y

On OSX using MacPorts:

.. code-block:: bash

    $ sudo port install geos
    $ sudo port install gdal

Proceed to install the actual files of **LIBRE**:

Using pip
---------

Via `pip <http://www.pip-installer.org/>`_ Python packager installer

.. code-block:: bash

    $ pip install libre
    $ libre-admin.py syncdb --migrate
    $ cat <<'EOF' > settings_local.py
    DEBUG=True
    DEVELOPMENT=True
    EOF
    $ libre-admin.py runserver --pythonpath=.

From GitHub
-----------

By cloning the code from the `GitHub <https://github.com/commonwealth-of-puerto-rico/libre>`_ repository:

.. code-block:: bash

    $ git clone https://github.com/commonwealth-of-puerto-rico/libre.git
    $ cd libre
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r libre/requirements.txt
    $ ./manage.py syncdb --migrate
    $ cat <<'EOF' > settings_local.py
    DEBUG=True
    DEVELOPMENT=True
    EOF
    $ ./manage.py runserver

Docker container
----------------

Or by using `Yamir Encarnacion's <https://github.com/yencarnacion/libre-docker>`_ `Docker <https://www.docker.io/>`_ container:

Use this to build a new image, tagged for easier reuse

.. code-block:: bash

    $ sudo docker build -t yencarnacion/libre-docker github.com/yencarnacion/libre-docker

Running the container

.. code-block:: bash

    $ sudo docker run -d -p 8000:8000 yencarnacion/libre-docker

The default username and password for the Docker image are:
Username: **admin** | Password: **libre**

Once up and running go to `<your ip>:8000` in your browser to use **LIBRE**.
