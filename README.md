# Dominoh

_Work in Progress_

Dominoh is a lightweight markup language for annotating text. 

Annotations are associations between a fragment of text and one or more subtexts. 
User-defined symbols mark semantic relationships between a text fragment and 
each of its subtexts.

## Syntax


### Fragment

Document

```
::Information is both input and output of its own production process.::
```

Parsed

```json
[
  {
    "fragment": "Information is both input and output of its own production process.",
    "subtexts": [],
    "symbols": {},
    "tags": []
  }
]
```


### Subtext

Document

```
:::
benkler , Yochai Benkler
:::

::Information is both input and output of its own production process.:: (( benkler ))
```

Parsed

```json
[
  {
    "fragment": "Information is both input and output of its own production process.",
    "subtexts": [
      "Yochai Benkler"
    ],
    "symbols": {},
    "tags": []
  }
]
```

### Tags

Document

```
:::
network_econ : networked information economy
:::

::Information is both input and output of its own production process.:: (( network_econ ))
```

Parsed

```json
[
  {
    "fragment": "Information is both input and output of its own production process.",
    "subtexts": [],
    "symbols": {},
    "tags": [
      "networked information economy"
    ]
  }
]
```


### Symbols

Document

```
:::
$ : sources

benkler , Yochai Benkler
:::

::Information is both input and output of its own production process.:: (( $benkler ))
```

Parsed

```json
[
  {
    "fragment": "Information is both input and output of its own production process.",
    "subtexts": [
      "Yochai Benkler"
    ],
    "symbols": {
      "sources": [
        "Yochai Benkler"
      ]
    },
    "tags": [
      "sources"
    ]
  }
]
```


### Compound symbols

Document

```
:::
$ : sources
# : tags

benkler      , Yochai Benkler
network_econ , networked information economy
:::

::Information is both input and output of its own production process.:: (( $#benkler #network_econ ))
```

Parsed

```json
[
  {
    "fragment": "Information is both input and output of its own production process.",
    "subtexts": [
      "Yochai Benkler",
      "networked information economy"
    ],
    "symbols": {
      "sources": [
        "Yochai Benkler"
      ],
      "tags": [
        "Yochai Benkler",
        "networked information economy"
      ]
    },
    "tags": [
      "sources",
      "tags"
    ]
  }
]
```
