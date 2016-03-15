# Domino 

A lightweight markup language (LML) for notetaking. 

## Markup

### Fragment

#### Fragment: Basic

Input:

```
::"Information is both input and output of its own production process."::
```

Output:

```json
{
    "fragments": [
        {
            "_id": 1,
            "text": "\"Information is both input and output of its own production process.\"",
            "start": 0,
            "end": 72
        }
    ],
    "document": "\"Information is both input and output of its own production process.\""
}
```

#### Fragment: Tagged

Input:

```
::"Information is both input and output of its own production process."|networked information economy, Yochai Benkler|
```

Output:

```json
{
    "fragments": [
        {
            "_id": 1,
            "text": "\"Information is both input and output of its own production process.\"",
            "start": 0,
            "end": 72
        },
    ],
    "tags": [
        {
            "_id": 2,
            "name": "networked information economy",
            "fragments": [1]
        },
        {
            "_id": 3,
            "name": "Yochai Benkler",
            "fragments": [1] 
        }
    ],
    "document": "\"Information is both input and output of its own production process.\""
}
```

#### Fragment: Sourced

```
:::
sources:
    Benkler:
        title: The Wealth of Networks
        location: ISBN 9780300127232
:::

::"Information is both input and output of its own production process."::[Benkler:: Chapter 2]
```

```json
{
    "sources": [
        {
            "_id": 4,
            "title": "The Wealth of Networks",
            "fragments": [
                {
                    "_id": 1,
                    "location": ["ISBN 9780300127232", "Chapter 2"]
                }
            ]
        }
    ], 
    "fragments": [
        {
            "_id": 1,
            "text": "\"Information is both input and output of its own production process.\"",
            "start": 0,
            "end": 72
        },
    ],
    "document": "\"Information is both input and output of its own production process.\""
}
```