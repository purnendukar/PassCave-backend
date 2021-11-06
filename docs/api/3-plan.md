# Plan

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/plan
```

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
            "id": "005ea056-364c-4abb-9294-1dfe49eaa88c",
            "name": "Basic",
            "description": "Decription",
            "amount": "1.00",
            "members_count": 1
        },
        {
            "id": "f74c6f17-c604-4024-b856-1f93687194e7",
            "name": "Pro",
            "description": "Decription",
            "amount": "3.00",
            "members_count": 4
        }
    ]
}
```
