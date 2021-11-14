# Secret Manager

!!!info
    For API overview and usages, check out [this page](0-overview.md)

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
            ],
            "title": "title"
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
    ],
    "title": "title"
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
    "id": "050c61bf-a285-427e-b9bd-826b01705239",
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
    ],
    "title": "title"
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
    "id": "050c61bf-a285-427e-b9bd-826b01705239",
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
    ],
    "title": "title"
}
```
