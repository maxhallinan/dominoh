# dominoh 

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
            "text": "\"Information is both input and output of its own production process.\"",
            "start": [1, 1],
            "end": [1, 72]
        }
    ]
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
            "text": "\"Information is both input and output of its own production process.\"",
            "start": [1, 1],
            "end": [1, 72]
        }
    ],
    "tags": [
        {
            "name": "networked information economy",
            "fragments": [0]
        },
        {
            "name": "Yochai Benkler",
            "fragments": [0] 
        }
    ]
}
```
