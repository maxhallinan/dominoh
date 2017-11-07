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
    "symbols": {},
    "location": {
      "clean": {
        "start": {
          "line": 2,
          "char": 1
        },
        "end": {
          "line": 2,
          "char": 72 
        }
      },
      "source": {
        "start": {
          "line": 9,
          "char": 3
        },
        "end": {
          "line": 9,
          "char": 75 
        }
      }
    }
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

::Information is both input and output of its own production process.:: $benkler #network_econ
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
    },
    "location": {
      "clean": {
        "start": {
          "line": 2,
          "char": 1
        },
        "end": {
          "line": 2,
          "char": 72 
        }
      },
      "source": {
        "start": {
          "line": 9,
          "char": 3
        },
        "end": {
          "line": 9,
          "char": 75 
        }
      }
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

::Information is both input and output of its own production process.:: $#benkler #network_econ
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
    },
    "location": {
      "clean": {
        "start": {
          "line": 2,
          "char": 1
        },
        "end": {
          "line": 2,
          "char": 72 
        }
      },
      "source": {
        "start": {
          "line": 9,
          "char": 3
        },
        "end": {
          "line": 9,
          "char": 75 
        }
      }
    }
  }
]
```
