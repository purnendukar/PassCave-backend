# Secret Manager

!!!info
    For API overview and usages, check out [this page](0-overview.md)

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
            ],
            "title": "title"
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
    ],
    "title": "title"
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
    ],
    "title": "title"
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "fbb14152-6292-44f5-a155-60038acafcdf",
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
    ],
    "title": "title"
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
    ],
    "title": "title"
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "fbb14152-6292-44f5-a155-60038acafcdf",
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
    ],
    "title": "title"
}
```
