# c2-recipe-app-api-2

Course code for: Build a Backend REST API with Python &amp; Django - Advanced: Take the course here: https://londonapp.dev/c2

Run commands in container :
docker compose run --rm app sh -c "python manage.py test"

docker compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

docker-compose run --rm app env
