# Crawler for Binance Announce

## Getting started
### Setup Development Environment
▍Method 1 - Python Built-in venv

- Create your virtual environment
```
$ python3 -m venv venv
```
- And enable virtual environment
```
$ . venv/bin/activate
```
- Install requirements
```
$ pip install -r requirements.txt 
```

▍Method 2 - Poetry
- Install requirements
```
$ poetry install
```
- And enable virtual environment
```
$ poetry shell
```

### Setup your Database & Run
Build your [Cloud Firestore](https://console.firebase.google.com/project/maxtodo-app/firestore), and download your [Firestore credential](https://console.firebase.google.com/project/your-project/settings/serviceaccounts/adminsdk) in the folder


Run Crawler
```
$ python3 main.py
```
