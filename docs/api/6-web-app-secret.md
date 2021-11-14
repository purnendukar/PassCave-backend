# Secret Manager

!!!info
    For API overview and usages, check out [this page](0-overview.md)

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
            ],
            "title": "title",
            "title": "title"
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
    ],
    "title": "title"
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
    "id": "c0750631-8b00-4a8b-80d3-06e12c898e78",
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
    ],
    "title": "title"
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
    "id": "c0750631-8b00-4a8b-80d3-06e12c898e78",
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
    ],
    "title": "title"
}
```
