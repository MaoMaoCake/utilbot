def get_ip():
    import requests
    return requests.get('https://api.ipify.org?format=json').json().get("ip")