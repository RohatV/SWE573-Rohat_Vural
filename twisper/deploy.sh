# build our heroku-ready local Docker image
docker build -t dj-docker-twhisper-to-heroku -f Dockerfile .


# push your directory container for the web process to heroku
heroku container:push web -a twhisper


# promote the web process with your container 
heroku container:release web -a twhisper


# run migrations
heroku run python3 manage.py migrate -a twhisper
