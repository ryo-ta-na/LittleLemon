# Prerequisite
-'LittleLemon' database is created in your mysql database
-Migrations have already been run
-'admin' user is created using Django admin interface
-The password for the 'admin' user is updated in the DATABASES section in settings.py
-At least one record is added to two tables: restaurant_booking and restaurant_menu

# API paths to test
## Restaurant app
/restaurant/ # static content
/restaurant/menu
/restaurant/menu/1
/restaurant/booking/

## LittleLemonAPI app
/api/menu-items/
/api/menu-items/1
/api/message/ # Authentication required
/api/api-token-auth # POST request with username and password fields as form data
