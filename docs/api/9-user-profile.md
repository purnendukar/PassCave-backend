# Secret Manager

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## User Profile

### Get List
Get list of identity details that is owned by the user.

```
GET /api/me (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "email": "purnendu.kar8@gmail.com",
    "first_name": "",
    "last_name": "",
    "profile": {
        "plan": {
            "id": "005ea056-364c-4abb-9294-1dfe49eaa88c",
            "name": "Basic",
            "description": "Decription",
            "amount": "1.00",
            "members_count": 1
        }
    }
}
```

### Add Profile Related Data

```
POST /api/me/ (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
plan | Plan ID

**Request**
```json
{
    "plan": "f74c6f17-c604-4024-b856-1f93687194e7"
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "24dd3436-32bb-4946-8a98-c46cfa6a3fd0",
    "email": "purnendu.kar8@gmail.com",
    "first_name": "",
    "last_name": "",
    "profile": {
        "plan": {
            "id": "005ea056-364c-4abb-9294-1dfe49eaa88c",
            "name": "Basic",
            "description": "Decription",
            "amount": "1.00",
            "members_count": 1
        }
    }
}
```

### Partial Update

```
PATCH /api/me/ (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
plan | Plan ID

**Request**
```json
{
    "first_name": "",
    "last_name": "",
    "profile": {
        "plan": "f74c6f17-c604-4024-b856-1f93687194e7"
    }
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "3f390520-9960-4dc0-a186-a3eeb2ac8b78",
    "email": "purnendu.kar8+7@gmail.com",
    "first_name": "",
    "last_name": "",
    "profile": {
        "plan": {
            "id": "f74c6f17-c604-4024-b856-1f93687194e7",
            "name": "Pro",
            "description": "Decription",
            "amount": "3.00",
            "members_count": 4
        }
    }
}
```
