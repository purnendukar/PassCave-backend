# Organisation

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/organisation (requires authentication)
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
            "id": "a2949dcb-9f5c-4587-9f66-e04aa9387e79",
            "created_at": "2021-11-04T11:55:25.818258Z",
            "updated_at": "2021-11-04T11:55:25.818340Z",
            "org_type": "family",
            "admin": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
            "members": [
                "0e51875b-6786-4604-8c86-e7c6ab9ff516",
                "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
            ]
        }
    ]
}
```

### Get Object

```
GET /api/organisation/:id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "a2949dcb-9f5c-4587-9f66-e04aa9387e79",
    "created_at": "2021-11-04T11:55:25.818258Z",
    "updated_at": "2021-11-04T11:55:25.818340Z",
    "org_type": "family",
    "admin": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "members": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```


### Create new data

```
POST /api/organisation (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
org_type | Organisation Type (family, orgnisation)
members | List of user ids who can access this credential

**Request**
```json
{
    "org_type": "family",
    "members": [
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
    "id": "a2949dcb-9f5c-4587-9f66-e04aa9387e79",
    "created_at": "2021-11-04T11:55:25.818258Z",
    "updated_at": "2021-11-04T11:55:25.818340Z",
    "org_type": "family",
    "admin": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "members": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```


### Partial Update

```
PATCH /api/organisation/:id (requires authentication)
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
access_given | List of user ids who can access this credential

**Request**
```json
{
    "org_type": "family",
    "members": [
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
    "id": "a2949dcb-9f5c-4587-9f66-e04aa9387e79",
    "created_at": "2021-11-04T11:55:25.818258Z",
    "updated_at": "2021-11-04T11:55:25.818340Z",
    "org_type": "family",
    "admin": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "members": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```