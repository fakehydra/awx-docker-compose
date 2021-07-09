# awx-docker-compose
####  docker-compose.yml for ansible-awx 
### before use it,you need install docker and docker-compose

#### Install docker

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg |apt-key add -
add-apt-repository \ "deb [arch=amd64] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) \ stable"
apt update
apt install -y docker-ce docker-ce-cli containerd.io
docker version
```

####  Install docker-compose

```
curl -s https://api.github.com/repos/docker/compose/releases/latest \
| grep browser_download_url | grep docker-compose-Linux-x86_64 \
| cut -d '"' -f 4 | wget -qi -
chmod +x docker-compose-Linux-x86_64
mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
docker-compose version
```

### How To Use 
#### clone repo
git clone https://github.com/fakehydra/awx-docker-compose.git

#### use

```
tar xf awx-docker-compose.tar.gz
cd awx-docker-compose
docker-compose up -d
```
