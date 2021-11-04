# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get Object

```
GET /api/secret_group (requires authentication)
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
    "grp_type": "personal",
    "admin": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "members": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```


## Create new data

```
POST /api/secret_group (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
grp_type | Group Type (personal, orgnisation)
members | List of user ids who can access this credential
name | Name of the group

**Request**
```json
{
    "grp_type": "personal",
    
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
    "grp_type": "personal",
    "admin": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "members": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```


## Partial Update

```
PATCH /api/secret_group/:id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
grp_type | Group Type (personal, orgnisation)
members | List of user ids who can access this credential
name | Name of the group

**Request**
```json
{
    "grp_type": "personal",
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
    "grp_type": "personal",
    "admin": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "members": [
        "0e51875b-6786-4604-8c86-e7c6ab9ff516",
        "24dd3436-32bb-4946-8a98-c46cfa6a3fd0"
    ]
}
```
