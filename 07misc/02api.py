from getopt import error
import imp
import json
import requests
api="http://www.boredapi.com/api/activity"

random_user_api="https://randomuser.me/api"

def callApi(api):
    res = requests.get(api)
    # print(res)
    # print(res.status_code)
    res_text = json.loads(res.text)
    print(res_text)
    # print(type(res_text))
    print(res_text["activity"])

def random_user(api):
    try:
        res= requests.get(api)
        res_text = json.loads(res.text)
        # print(res_text)
        fname=res_text['results'][0]['name']['first']
        lname=res_text['results'][0]['name']['last']
        print(fname)
        print(lname)
    except BaseException as err:
        print(err)


if __name__ == "__main__":
    # callApi(api)
    random_user(random_user_api)
