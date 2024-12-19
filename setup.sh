
#building images
#-----to test building images --------#

#docker build -t api_authentification_image -f Dockerfile.authentification .
#docker build -t api_authorization_image -f Dockerfile.authorization .
#docker build -t api_content_image -f Dockerfile.content .

#building each container to test#
#docker run --name="authentification_container"  --network="host" api_authentification_image
#docker run  --name="authorization_container" --network="host" api_authorization_image
#docker run --name="content_container" --network="host" api_content_image

docker-compose build --no-cache

docker-compose up

