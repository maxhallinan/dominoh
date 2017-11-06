# dominoh

_Work in Progress_

A lightweight markup language for annotating text.

## Syntax

### Fragment: Basic

Input:

```
::Information is both input and output of its own production process.::
```

Output:

```json
[
  {
    "text": "Information is both input and output of its own production process.",
    "start": {
      "line": 1,
      "char": 1
    },
    "end": {
      "line": 1,
      "char": 72
    },
    "notes": [],
    "sources": [],
    "tags": []
  }
]
```

### Fragment: Tagged

Input:

```
::Information is both input and output of its own production process.::
::networked information economy, Yochai Benkler::
```

Output:

```json
[
  {
    "text": "Information is both input and output of its own production process.",
    "start": {
      "line": 1,
      "char": 1
    },
    "end": {
      "line": 1,
      "char": 72
    },
    "notes": [],
    "sources": [],
    "tags": [
      "networked information economy",
      "Yochai Benkler"
    ]
  }
]
```

### Fragment: Sourced

```
:::
Benkler
  The Wealth of Networks
  ISBN 9780300127232
:::

::Information is both input and output of its own production process.::
::$Benkler, networked information economy, Yochai Benkler::
```

```json
[
  {
    "text": "Information is both input and output of its own production process.",
    "start": {
      "line": 1,
      "char": 1
    },
    "end": {
      "line": 1,
      "char": 72
    },
    "notes": [],
    "sources": [
      "The Wealth of Networks",
      "ISBN 9780300127232"
    ],
    "tags": [
      "networked information economy",
      "Yochai Benkler"
    ]
  }
]
```

### Fragment: Annotated

```
:::
Benkler
  The Wealth of Networks
  ISBN 9780300127232

1
  Yochai Benkler is a professor at Harvard Law School.
:::

::Information is both input and output of its own production process.::
::$Benkler, @1, networked information economy, Yochai Benkler::
```

```json
[
  {
    "text": "Information is both input and output of its own production process.",
    "start": {
      "line": 1,
      "char": 1
    },
    "end": {
      "line": 1,
      "char": 72
    },
    "notes": [
      "Yochai Benkler is a professor at Harvard Law School."
    ],
    "sources": [
      "The Wealth of Networks",
      "ISBN 9780300127232"
    ],
    "tags": [
      "networked information economy",
      "Yochai Benkler"
    ]
  }
]
```


## Development

```
virtualenv venv
source venv/bin/activate
pip install -e .
```
