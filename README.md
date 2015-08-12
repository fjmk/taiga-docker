## Install taiga + letschat on new VM (Ubuntu 14.04 or higher)

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install git wget curl

wget -qO- https://raw.githubusercontent.com/fjmk/taiga-docker/1.8.0/install | sh
```

## Using Taiga

Point your browser to http://taiga.example.com/ (replace example.com with your domain)

Login with user **admin** and password **123123**. Change your password as soon as possible.

Create your first project in Taiga.

There are some nice tutorials [here](https://www.youtube.com/playlist?list=PLgsasMWN5JssgHHHHI50xkz_kzXg-dElt).



## Using LetsChat

Point your browser to http://chat.example.com/

* Create a new user (suggestion for the name: Taiga)
* Login as Taiga user
* Add your first room and remember the slug (example: project1) 
* Create a new Auth token for this user and copy this token

In another tab of your browser, go to your project, ADMIN -> PLUGINS and fill in:
```bash
Let's Chat messages endpoint
http://chat.example.com/rooms/project1/messages
Let's Chat Auth token
NTVjYjI2YmQzNz  very log token M4NzkxMzAwOTUyNyZjFmM2NhNWFlNjQ4MDUyNGM0ZjM5MQ==
```

Save and test letschat. After test you **should** see ```**Test:** *LetsChat* message``` in your ```project1``` room.
