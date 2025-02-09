JENKINS_NETWORK=temp_jenkins
DOCKER_DIND_NAME=jckin_jenkins-docker
DOCKER_DIND_PORT=2376
BLUEOCEAN_NAME=jenkins-blueocean
BLEUOCEAN_PORT=2777

docker network create $JENKINS_NETWORK

docker run \
  --name $DOCKER_DIND_NAME \
  --rm \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish $DOCKER_DIND_PORT:2376 \
  docker:dind \
  --storage-driver overlay2

docker build -t myjenkins-blueocean:2.492.1-1 -f Dockerfile.jenkins .

docker run \
  --name $BLEUOCEAN_NAME \
  --restart=on-failure \
  --detach \
  --network $JENKINS_NETWORK \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish $BLUEOCEAN_PORT:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.492.1-1


