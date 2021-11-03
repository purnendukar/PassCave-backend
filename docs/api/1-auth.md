# Authentication

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Signup

```
POST /api/auth/signup
```

**Parameters**

Name     | Description
---------|-------------------------------------
email    | Email of the user
password | Password of the user

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "message": "Registration successful",
    "data": {
        "email": "purnendu.kar8+6@gmail.com",
        "profile": null,
        "token": "ade1f6798ea28300a3886cd1c62ced05fef66a5a"
    }
}
```


## Login

```
POST /api/auth/login
```

**Parameters**

Name     | Description
---------|-------------------------------------
email    | Email of the user
password | Password of the user

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "message": "Login successful",
    "data": {
        "email": "purnendu.kar8@gmail.com",
        "profile": null,
        "token": "f7949ae8e70876d217b18648ae14b94c9a8a9222"
    }
}
```

