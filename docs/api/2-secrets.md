# Secrets

!!!info
    For API overview and usages, check out [this page](0-overview.md)


### Get List
Get list of all secrets that is owned by the user.

```
GET /api/secrets (requires authentication)
```

!!! Note
    - **secret_type:** ("webapplication", "bankcard", "bankdetail", "indentity", "secretnote", "upigateway)
    - **secret_object** is an dynamic json object that is based on secret_type

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
            "secret_type": "webapplication",
            "secret_object": {
                "id": "90dda5a6-967b-4270-abe1-95dda5fe7faf",
                "url": "asd",
                "username": "asd",
                "email": "asd@as.com",
                "mobile": "89798",
                "password": "asdadd",
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
        }
    ]
}
```
