Odoo Services Admin
=====================================

* Groups created:

Admin user (Setting servers): To admin servers.
Normal user (Setting servers): To start, stop, restart and watch status of servers, from User side.

* Config (init.d scripts, located in config/config.ini):

[ODOO_SERVERS]
COMMAND_DIRECTORY = /etc/init.d/odoo_scripts/

* Admin views:

    Config Servers: To manage the servers.
    Servers Config List: To manage the servers configuration.
    Config Admin Servers: To link servers with servers configuration.
    
* User views:

    Config User Servers: To manage the user servers (start, stop, restart servers and refresh status).
    
* To install:

    # Install odoo:

    # https://www.odoo.com/documentation/10.0/setup/install.html
    sudo aptitude install odoo

    # To execute scripts as USER=odoo, example:
    # sudo /etc/init.d/odoo_scripts/odoo start
    # sudo /etc/init.d/odoo_scripts/odoo stop
    # sudo /etc/init.d/odoo_scripts/odoo status

    #GRANT PREMISSIONS TO odoo USER
    # Edit last line of /etc/sudoers:
    odoo ALL=(root) NOPASSWD: /etc/init.d/odoo_scripts/*/
    
    #Link the init script:
    sudo mkdir -p /etc/init.d/odoo_scripts/
    sudo ln -s /etc/init.d/odoo /etc/init.d/odoo_scripts/
    
    #Or you can create folders, that will be grouped by init command sections
    sudo mkdir -p /etc/init.d/odoo_scripts/user_1/
    sudo ln -s /etc/init.d/odoo /etc/init.d/odoo_scripts/user_1/
    


    # To create another instance of Odoo:

    ODOO_NEW_INSTANCE="odoo-new-instance"

    sudo mkdir -p /etc/init.d/odoo_scripts/
    sudo cp /etc/init.d/odoo /etc/init.d/$ODOO_NEW_INSTANCE
    sudo ln -s /etc/init.d/$ODOO_NEW_INSTANCE /etc/init.d/odoo_scripts/
    #Change header of /etc/init.d/$ODOO_NEW_INSTANCE
    # Provides:          odoo-new-instance
    sudo update-rc.d $ODOO_NEW_INSTANCE defaults >/dev/null

    sudo /etc/init.d/odoo_scripts/$ODOO_NEW_INSTANCE start
    # sudo /etc/init.d/odoo_scripts/$ODOO_NEW_INSTANCE stop
    # sudo /etc/init.d/odoo_scripts/$ODOO_NEW_INSTANCE status

Credits
=======

Contributors
------------

* César Cordero Rodríguez <cesar.cordero.r@gmail.com>
