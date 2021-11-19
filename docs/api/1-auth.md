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
first_name    | First Name of the user
last_name    | Last Name of the user
email    | Email of the user
password | Password of the user

**Request**
```json
{
    "email": "hello@example.com",
    "first_name": "first_name",
    "last_name": "last_name",
    "password": "VerySafePassword0909"
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "email": "hello@example.com",
    "first_name": "first_name",
    "last_name": "last_name",
    "profile": null,
    "token": "ade1f6798ea28300a3886cd1c62ced05fef66a5a"
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
    "email": "hello@example.com",
    "first_name": "first_name",
    "last_name": "last_name",
    "profile": null,
    "token": "f7949ae8e70876d217b18648ae14b94c9a8a9222"
}
```


## Logout

```
POST /api/auth/logout (requires authentication)
```

**Response**
```
Status: 204 No Content
```


## Forgot Password

```
POST /api/auth/forgot-password
```

**Parameters**

Name     | Description
---------|-------------------------------------
email    | Email of the user

**Request**
```json
{
    "email": "hello@example.com"
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "message": "Further instructions will be sent to the email if it exists"
}
```


## Reset Password

```
POST /api/auth/password-reset-confirm
```

**Parameters**

Name     | Description
---------|-------------------------------------
email    | Email of the user
token    | Token for forgot password confirmation
new_password    | New Password for the account

**Request**
```json
{
    "email": "hello@example.com",
    "token": "MjRkZDM0MzYtMzJiYi00OTQ2LThhOTgtYzQ2Y2ZhNmEzZmQw::aw0ecv-099b0a07616e897c9bdbd1b3a5845d97",
    "new_password": "Admin@123"
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "message": "Further instructions will be sent to the email if it exists"
}
```
