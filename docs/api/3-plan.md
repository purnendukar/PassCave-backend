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
            "created_at": "2021-11-04T08:28:59.743509Z",
            "updated_at": "2021-11-04T08:28:59.743557Z",
            "name": "Basic",
            "description": "Decription",
            "slug": "basic",
            "amount": "1.00",
            "members_count": 1
        },
        {
            "id": "f74c6f17-c604-4024-b856-1f93687194e7",
            "created_at": "2021-11-04T08:29:40.610730Z",
            "updated_at": "2021-11-04T08:29:40.610781Z",
            "name": "Pro",
            "description": "Decription",
            "slug": "pro",
            "amount": "3.00",
            "members_count": 4
        }
    ]
}
```
