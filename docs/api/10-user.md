# User Profile

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get Users List

```
GET /api/user (requires authentication)
```
**Parameters**

Name     | Description
---------|-------------------------------------
search | Seach based on email, first_name, last_name value

**Response**
```
Status: 200 OK
```
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "2739c134-4271-4e3f-bf62-3811e6d7ed93",
            "email": "purnendu.kar8+13@gmail.com",
            "first_name": "Purnendu",
            "last_name": "asd"
        },
        {
            "id": "732c89a0-fed8-4bfe-bc8a-3476226d2c93",
            "email": "purnendu.kar8+12@gmail.com",
            "first_name": "Purnendu",
            "last_name": "asd"
        }
    ]
}
```
