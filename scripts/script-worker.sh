#! /bin/bash

echo "********** STARTING WORKER **********"
sudo apt-get update

echo "********** INSTALLING CA-CERTIFICATES / CURL / GNUPG **********"
sudo apt-get install -y \
ca-certificates \
curl \
gnupg

echo "********** ADDING THE OFFICIAL GPG KEY **********"
sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo "********** SETING UP THE REPOSITORY **********"
echo \
"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "********** UPDATING APT-GET **********"
sudo apt-get update

echo "********** INSTALLING DOCKER **********"
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "********** CREATING THE FILES FOLDER **********"
sudo mkdir files

echo "********** CREATING THE VOLUME **********"
sudo docker volume create --driver local \
      --opt type=none \
      --opt device=/files \
      --opt o=bind \
      files

echo "********** SETTING UP GIT VARIABLES **********"
git config --global user.name "Monica Bajonero"
git config --global user.email m.bajonero@uniandes.edu.co

echo "********** CLONING THE REPOSITORY **********"
git clone https://github.com/monicabajonerodcastro/aplicaciones-nube.git

echo "********** CD FOLDER **********"
cd aplicaciones-nube

echo "********** CHECKOUT TO THE BRANCH **********"
git fetch && git checkout feature/gcp-instances

echo "********** PULLING THE LAST CHANGES **********"
git pull origin feature/gcp-instances

echo "********** CD FOLDER TO RUN **********"
cd worker

echo "********** DOCKER COMPOSE UP **********"
sudo docker compose up --build -d

echo "********** FINISHED WORKER **********"

EOF