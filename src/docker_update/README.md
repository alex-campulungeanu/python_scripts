
<h1 align="center">
<br>
  "Update running container"
</h1>

<p align="center">update environment variables inside runnnig container</p>

<hr />
<br />


## 📚 Project Definition

Per definition


## 🛠️ Features

Technologies used:

- 🌐 **Docker**


## 🚀 Instalation
1. 
  - cp  env_data.example env_data
  - update the file
  OR
  -update env_data dictionary inside main.py
2. 
  ```sh
  ./run.ps1
  ```

## 💻 Development
docker ps -q | % { docker stop $_ }
docker run --rm -it -v /:/host -v $PWD/main.py:/var/lib/docker/containers/main.py python:3 bash

## Documentation
Docker version 19.03.13, build 4484c46d9d

1. container host
docker run --rm -it -v /:/host alpine

Once inside container, for config you can directly cd to /host/var/lib/docker/containers/ or do a chroot to host and to get linux directory structure.
chroot /host
cd /var/lib/docker/containers/

## TODO:
- [ ] make a backup of config.v2.json before everything
- [X] change only a docker at a time

## Testing

