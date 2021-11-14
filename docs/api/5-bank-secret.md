# Secret Manager

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Bank Card

### Get List
Get list of bank card details that is owned by the user.

```
GET /api/secrets/bank_card (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "0e5c38fb-7fe6-4103-9006-fbe19736718e",
            "card_number": "987967864567",
            "expire_month": "1",
            "expire_year": "2022",
            "cvv": "989",
            "holder_name": "uyihiuh",
            "bank": "uuyguygu",
            "card_type": "credit_card",
            "owned_by": {
                "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
                "email": "purnendu.kar8@gmail.com",
                "first_name": "",
                "last_name": ""
            },
            "access_given": [
                {
                    "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
                    "email": "purnendu.kar8@gmail.com",
                    "first_name": "",
                    "last_name": ""
                }
            ]
        }
    ]
}
```

### Get Object

```
GET /api/secrets/bank_card/:id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "0e5c38fb-7fe6-4103-9006-fbe19736718e",
    "card_number": "987967864567",
    "expire_month": "1",
    "expire_year": "2022",
    "cvv": "989",
    "holder_name": "uyihiuh",
    "bank": "uuyguygu",
    "card_type": "credit_card",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```


### Create new data

```
POST /api/secrets/bank_card (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
card_number | Card Number
expire_month | Card Expire Month
expire_year | Card Expire Year
cvv | Card CVV Number
holder_name | Holder Name
bank | Bank Name
card_type | Card Type (credit_card, debit_card, atm_card, other)
bank | Bank Name
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "card_number": "987967864567",
    "expire_month": "1",
    "expire_year": "2022",
    "cvv": "989",
    "holder_name": "uyihiuh",
    "bank": "uuyguygu",
    "card_type": "credit_card",
    "access_given": [
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1"
    ]
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "902c893c-9788-446a-bdea-def7e4585469",
    "card_number": "987967864567",
    "expire_month": "1",
    "expire_year": "2022",
    "cvv": "989",
    "holder_name": "uyihiuh",
    "bank": "uuyguygu",
    "card_type": "credit_card",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        },
        {
            "id": "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1",
            "email": "purnendu.kar8+2@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```


### Partial Update

```
PATCH /api/secrets/bank_card/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
card_number | Card Number
expire_month | Card Expire Month
expire_year | Card Expire Year
cvv | Card CVV Number
holder_name | Holder Name
bank | Bank Name
card_type | Card Type (credit_card, debit_card, atm_card, other)
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "card_number": "987967864567",
    "expire_month": "1",
    "expire_year": "2022",
    "cvv": "989",
    "holder_name": "uyihiuh",
    "bank": "uuyguygu",
    "card_type": "credit_card",
    "access_given": [
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1"
    ]
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "902c893c-9788-446a-bdea-def7e4585469",
    "card_number": "987967864567",
    "expire_month": "1",
    "expire_year": "2022",
    "cvv": "989",
    "holder_name": "uyihiuh",
    "bank": "uuyguygu",
    "card_type": "credit_card",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        },
        {
            "id": "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1",
            "email": "purnendu.kar8+2@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```


## Bank Detail

### Get List
Get list of bank details that is owned by the user.

```
GET /api/secrets/bank_detail (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "694fc4bb-0887-462a-a7bf-e8debbdb70b0",
            "created_at": "2021-11-03T09:39:16.091061Z",
            "updated_at": "2021-11-03T09:39:16.091116Z",
            "account_number": "AccountNumber",
            "ifsc_code": "IFSCCode",
            "branch_code": "BranchCode",
            "branch_name": "BankBranch",
            "holder_name": "Purnendu Kar",
            "bank": "BANK",
            "owned_by": {
                "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
                "email": "purnendu.kar8@gmail.com",
                "first_name": "",
                "last_name": ""
            },
            "access_given": [
                {
                    "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
                    "email": "purnendu.kar8@gmail.com",
                    "first_name": "",
                    "last_name": ""
                }
            ]
        }
    ]
}
```

### Get Object

```
GET /api/secrets/bank_detail/:id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "694fc4bb-0887-462a-a7bf-e8debbdb70b0",
    "account_number": "AccountNumber",
    "ifsc_code": "IFSCCode",
    "branch_code": "BranchCode",
    "branch_name": "BankBranch",
    "holder_name": "Purnendu Kar",
    "bank": "BANK",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```

### Create new data

```
POST /api/secrets/bank_detail (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
account_number | Account Number
ifsc_code | IFSC Code
branch_code | Branch Code
branch_name | Branch Name
holder_name | Holder Name
bank | Bank Name
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "account_number": "AccountNumber",
    "ifsc_code": "IFSCCode",
    "branch_code": "BranchCode",
    "branch_name": "BankBranch",
    "holder_name": "Purnendu Kar",
    "bank": "BANK",
    "access_given": [
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1"
    ]
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "4e337d13-8a61-4948-9758-17065b9d2480",
    "account_number": "AccountNumber",
    "ifsc_code": "IFSCCode",
    "branch_code": "BranchCode",
    "branch_name": "BankBranch",
    "holder_name": "Purnendu Kar",
    "bank": "BANK",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        },
        {
            "id": "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1",
            "email": "purnendu.kar8+2@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```

### Partial Update

```
PATCH /api/secrets/bank_detail/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
account_number | Account Number
ifsc_code | IFSC Code
branch_code | Branch Code
branch_name | Branch Name
holder_name | Holder Name
bank | Bank Name
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "account_number": "AccountNumber",
    "ifsc_code": "IFSCCode",
    "branch_code": "BranchCode",
    "branch_name": "BankBranch",
    "holder_name": "Purnendu Kar",
    "bank": "BANK",
    "access_given": [
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1"
    ]
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "4e337d13-8a61-4948-9758-17065b9d2480",
    "account_number": "AccountNumber",
    "ifsc_code": "IFSCCode",
    "branch_code": "BranchCode",
    "branch_name": "BankBranch",
    "holder_name": "Purnendu Kar",
    "bank": "BANK",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        },
        {
            "id": "960c6604-52f8-4ee1-98a4-d6bd5bbe1da1",
            "email": "purnendu.kar8+2@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```


## UPI Gateway

### Get List
Get list of upi gateway details that is owned by the user.

```
GET /api/secrets/upi_gateway (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "a5f3a098-a290-4ecd-b171-992d54d5c372",
            "upi_id": "upi id",
            "portal": "google pay",
            "pin": "pin",
            "owned_by": {
                "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
                "email": "purnendu.kar8@gmail.com",
                "first_name": "",
                "last_name": ""
            },
            "access_given": [
                {
                    "id": "0e51875b-6786-4604-8c86-e7c6ab9ff516",
                    "email": "purnendu.kar8+5@gmail.com",
                    "first_name": "",
                    "last_name": ""
                },
                {
                    "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
                    "email": "purnendu.kar8@gmail.com",
                    "first_name": "",
                    "last_name": ""
                }
            ]
        }
    ]
}
```

### Get Object

```
GET /api/secrets/upi_gateway/:id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "a5f3a098-a290-4ecd-b171-992d54d5c372",
    "upi_id": "upi id",
    "portal": "google pay",
    "pin": "pin",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "0e51875b-6786-4604-8c86-e7c6ab9ff516",
            "email": "purnendu.kar8+5@gmail.com",
            "first_name": "",
            "last_name": ""
        },
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```

### Create new data

```
POST /api/secrets/upi_gateway (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
upi_id | UPI ID
portal | Portal Name
pin | UPI Pin
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "upi_id": "upi id",
    "portal": "google pay",
    "pin": "pin",
    "access_given": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "7ff65521-3483-4b1d-a717-acc7fad801ba",
    "upi_id": "upi id",
    "portal": "google pay",
    "pin": "pin",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "0e51875b-6786-4604-8c86-e7c6ab9ff516",
            "email": "purnendu.kar8+5@gmail.com",
            "first_name": "",
            "last_name": ""
        },
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```

### Partial Update

```
PATCH /api/secrets/upi_gateway/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
upi_id | UPI ID
portal | Portal Name
pin | UPI Pin
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "upi_id": "upi id",
    "portal": "google pay",
    "pin": "pin",
    "access_given": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "7ff65521-3483-4b1d-a717-acc7fad801ba",
    "upi_id": "upi id",
    "portal": "google pay",
    "pin": "pin",
    "owned_by": {
        "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
        "email": "purnendu.kar8@gmail.com",
        "first_name": "",
        "last_name": ""
    },
    "access_given": [
        {
            "id": "0e51875b-6786-4604-8c86-e7c6ab9ff516",
            "email": "purnendu.kar8+5@gmail.com",
            "first_name": "",
            "last_name": ""
        },
        {
            "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "email": "purnendu.kar8@gmail.com",
            "first_name": "",
            "last_name": ""
        }
    ]
}
```
