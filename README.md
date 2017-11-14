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
    "symbols": {}
  }
]
```


### Symbols

Document

```
:::
$ : sources
# : tags

benkler      , Yochai Benkler
network_econ , networked information economy
:::

::Information is both input and output of its own production process.:: (( $benkler #network_econ ))
```

Parsed

```json
[
  {
    "fragment": "Information is both input and output of its own production process.",
    "symbols": {
      "sources": [
        "Yochai Benkler"
      ],
      "tags": [
        "networked information economy"
      ]
    }
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
    "symbols": {
      "sources": [
        "Yochai Benkler"
      ],
      "tags": [
        "Yochai Benkler",
        "networked information economy"
      ]
    }
  }
]
```

