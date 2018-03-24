import requests

OAUTH_ENDPOINT = "/oauth2/token"
MONEY_MOVEMENT = "/money-movement"
BANK_STARTER = '/deposits'
TRANSFER_REQUESTS = "/transfer-requests"
ACCOUNTS = "/accounts"
APPLICATION = '/application'

def setup_oauth(client_id = 'vgw3sf4f8nq3b98i1gdfr8wpx4gpty0ska52', 
    client_secret = 'eb5f6rda6v0d1ld8y4fymkudo86gorrc47cj', base_url = 'https://api.dxhackathon.com'):
    global CAPITAL_ONE_SANDBOX
    CAPITAL_ONE_SANDBOX = base_url
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    oauth_headers = {
        'Accept': "application/json",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(CAPITAL_ONE_SANDBOX + OAUTH_ENDPOINT, data=payload, headers=oauth_headers)
        response.raise_for_status()
        json_response = response.json()

        access_token = json_response['token_type'] + ' ' + json_response['access_token']
        global api_headers
        api_headers = {
            'Accept': "application/json;v=0",
            'Authorization': access_token
        }
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def get_eligible_accounts():
    url = CAPITAL_ONE_SANDBOX + MONEY_MOVEMENT + ACCOUNTS
    try:
        response = requests.get(url, headers=api_headers)
        response.raise_for_status()
        print("Get Accounts Successful")
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def initiate_transfer(transfer_request):
    url = CAPITAL_ONE_SANDBOX + MONEY_MOVEMENT + TRANSFER_REQUESTS
    try:
        print(transfer_request)
        response = requests.post(url, json=transfer_request, headers=api_headers)
        response.raise_for_status()
        print("Post Transfer Request Successful")
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())
        return response.json()

def get_transfer_request(transfer_request_id):
    url = CAPITAL_ONE_SANDBOX + MONEY_MOVEMENT + TRANSFER_REQUESTS + "/" + transfer_request_id
    try:
        response = requests.get(url, headers=api_headers)
        response.raise_for_status()
        print("Get Transfer Request Successful")
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def get_transfer_requests(account_reference_id, filters):
    filters["moneyMovementAccountReferenceId"] = account_reference_id
    url = CAPITAL_ONE_SANDBOX + MONEY_MOVEMENT + TRANSFER_REQUESTS
    try:
        response = requests.get(url, params=filters, headers=api_headers)
        response.raise_for_status()
        print("Get Transfer Requests Successful")
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def update_transfer_request(transfer_request_id, status):
    transfer_request = {
        "transferRequestStatus": status
    }
    url = CAPITAL_ONE_SANDBOX + MONEY_MOVEMENT + TRANSFER_REQUESTS + "/" + transfer_request_id
    try:
        response = requests.patch(url, json=transfer_request, headers=api_headers)
        print("Update Transfer Request Successful")
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def make_application(transfer_request):
    url = CAPITAL_ONE_SANDBOX + BANK_STARTER + APPLICATION
    try:
        response = requests.post(url, json=transfer_request.__dict__, headers=api_headers)
        response.raise_for_status()
        print("Post Transfer Request Successful")
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())
