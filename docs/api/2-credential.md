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
            "created_at": "2021-11-02T20:31:49.409628Z",
            "updated_at": "2021-11-02T20:31:49.409677Z",
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
    "created_at": "2021-11-02T20:31:49.409628Z",
    "updated_at": "2021-11-02T20:31:49.409677Z",
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
    "created_at": "2021-11-03T12:45:10.868987Z",
    "updated_at": "2021-11-03T12:45:10.869035Z",
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
    "created_at": "2021-11-03T12:45:10.868987Z",
    "updated_at": "2021-11-03T12:45:10.869035Z",
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
    "created_at": "2021-11-03T14:51:42.671970Z",
    "updated_at": "2021-11-03T14:51:42.672104Z",
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
    "created_at": "2021-11-03T14:51:42.671970Z",
    "updated_at": "2021-11-03T14:54:41.331378Z",
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
            "created_at": "2021-11-03T17:58:59.734541Z",
            "updated_at": "2021-11-03T17:58:59.734600Z",
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
    "created_at": "2021-11-03T17:58:59.734541Z",
    "updated_at": "2021-11-03T17:58:59.734600Z",
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
    "created_at": "2021-11-03T18:14:23.083426Z",
    "updated_at": "2021-11-03T18:14:23.083719Z",
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
    "created_at": "2021-11-03T18:14:23.083426Z",
    "updated_at": "2021-11-03T18:15:47.798535Z",
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


## Identity

### Get List
Get list of identity details that is owned by the user.

```
GET /api/secrets/identity (requires authentication)
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
            "id": "87982293-c4b4-44f4-8fb3-6092d0d2261f",
            "created_at": "2021-11-03T09:40:34.624757Z",
            "updated_at": "2021-11-03T09:40:34.624805Z",
            "id_name": "IDName",
            "id_number": "IDNumber",
            "image": null,
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
GET /api/secrets/indentity/:id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "87982293-c4b4-44f4-8fb3-6092d0d2261f",
    "created_at": "2021-11-03T09:40:34.624757Z",
    "updated_at": "2021-11-03T09:40:34.624805Z",
    "id_name": "IDName",
    "id_number": "IDNumber",
    "image": null,
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
POST /api/secrets/identity (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
id_name | ID Name
id_number | ID Number
access_given | List of user ids who can access this secrets
image | Image object 

!!! Note
    To upload use form-data in request

**Request**
```json
{
    "id_name": "IDName",
    "id_number": "IDNumber",
    "image": null,
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
    "id": "fbb14152-6292-44f5-a155-60038acafcdf",
    "created_at": "2021-11-03T19:05:50.440511Z",
    "updated_at": "2021-11-03T19:05:50.440793Z",
    "id_name": "IDName",
    "id_number": "IDNumber",
    "image": null,
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
PATCH /api/secrets/identity/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
id_name | ID Name
id_number | ID Number
access_given | List of user ids who can access this secrets
image | Image object 

!!! Note
    To upload use form-data in request

**Request**
```json
{
    "id_name": "IDName",
    "id_number": "IDNumber",
    "image": null,
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
    "id": "fbb14152-6292-44f5-a155-60038acafcdf",
    "created_at": "2021-11-03T19:05:50.440511Z",
    "updated_at": "2021-11-03T19:06:42.769076Z",
    "id_name": "IDName",
    "id_number": "IDNumber",
    "image": null,
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


## Web Application

### Get List
Get list of web application details that is owned by the user.

```
GET /api/web_application/web_application (requires authentication)
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
            "id": "cb1f20a6-1f0c-40da-b2cb-8e1a4c87e157",
            "created_at": "2021-11-03T19:16:02.168147Z",
            "updated_at": "2021-11-03T19:16:02.168202Z",
            "url": "https://www.google.com",
            "username": "username",
            "mobile": "9876543217",
            "email": "test@example.com",
            "password": "password",
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
GET /api/secrets/web_application/:id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "cb1f20a6-1f0c-40da-b2cb-8e1a4c87e157",
    "created_at": "2021-11-03T19:16:02.168147Z",
    "updated_at": "2021-11-03T19:16:02.168202Z",
    "url": "https://www.google.com",
    "username": "username",
    "mobile": "9876543217",
    "email": "test@example.com",
    "password": "password",
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
POST /api/secrets/web_application (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
username | Username used for the website login
mobile | Mobile number used for the website login
email | Email used for the website login
url | Website URL
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "username": "username",
    "mobile": "9876543217",
    "email": "test@example.com",
    "password": "password",
    "url": "https://www.google.com",
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
    "id": "c0750631-8b00-4a8b-80d3-06e12c898e78",
    "created_at": "2021-11-03T19:18:40.829896Z",
    "updated_at": "2021-11-03T19:18:40.829940Z",
    "url": "https://www.google.com",
    "username": "username",
    "mobile": "9876543217",
    "email": "test@example.com",
    "password": "password",
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
PATCH /api/secrets/web_application/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
username | Username used for the website login
mobile | Mobile number used for the website login
email | Email used for the website login
url | Website URL
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "username": "username",
    "mobile": "9876543217",
    "email": "test@example.com",
    "password": "password",
    "url": "https://www.google.com",
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
    "id": "c0750631-8b00-4a8b-80d3-06e12c898e78",
    "created_at": "2021-11-03T19:18:40.829896Z",
    "updated_at": "2021-11-03T19:19:56.161358Z",
    "url": "https://www.google.com",
    "username": "username",
    "mobile": "9876543217",
    "email": "test@example.com",
    "password": "password",
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


## Secret Note

### Get List
Get list of notes that is owned by the user.

```
GET /api/web_application/secret_note (requires authentication)
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
            "id": "088cd6e2-a904-48cf-baf4-f8136745052b",
            "created_at": "2021-11-03T19:29:53.324837Z",
            "updated_at": "2021-11-03T19:29:53.324880Z",
            "topic": "topic",
            "note": "note",
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
GET /api/secrets/secret_note/:id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "088cd6e2-a904-48cf-baf4-f8136745052b",
    "created_at": "2021-11-03T19:29:53.324837Z",
    "updated_at": "2021-11-03T19:29:53.324880Z",
    "topic": "topic",
    "note": "note",
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
POST /api/secrets/secret_note (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
topic | Topic/Heading for the note
note | Note 
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "topic": "topic",
    "note": "note",
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
    "id": "050c61bf-a285-427e-b9bd-826b01705239",
    "created_at": "2021-11-03T20:08:52.417848Z",
    "updated_at": "2021-11-03T20:08:52.417979Z",
    "topic": "topic",
    "note": "note",
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
PATCH /api/secrets/secret_note/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
topic | Topic/Heading for the note
note | Note 
access_given | List of user ids who can access this secrets

**Request**
```json
{
    "topic": "topic",
    "note": "note",
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
    "id": "050c61bf-a285-427e-b9bd-826b01705239",
    "created_at": "2021-11-03T20:08:52.417848Z",
    "updated_at": "2021-11-03T20:08:52.417979Z",
    "topic": "topic",
    "note": "note",
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

