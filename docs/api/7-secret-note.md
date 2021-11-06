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
GET /api/credentials/secret_note/:id (requires authentication)
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
POST /api/credentials/secret_note (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
topic | Topic/Heading for the note
note | Note 
access_given | List of user ids who can access this credential

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
PATCH /api/credentials/secret_note/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
topic | Topic/Heading for the note
note | Note 
access_given | List of user ids who can access this credential

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