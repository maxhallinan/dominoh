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


## Grammar

This grammar uses [Extended Backus-Naur Form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form).

```
Document 
  = Text, Pair, Text
  | Text, Pair, Text, Document

Pair 
  = Meta, Text, Fragment
  | Fragment, Text, Meta
  | Fragment

Meta = MetaBlock, MetaBody, MetaBlock

MetaBlock = ":::"

MetaBody 
  = Linespace, TagExpr, Whitespace, LineBreak
  | Linespace, TagExpr, Whitespace, LineBreak, MetaBody
  | Linespace, SubtextExpr, Whitespace, LineBreak
  | Linespace, SubtextExpr, Whitespace, LineBreak, MetaBody

TagExpr = Word, ":", String, LineBreak

SubtextExpr = Word, ":", String, LineBreak

Fragment 
  = FragmentBlock, Any, FragmentBlock
  | FragmentBlock, Any, FragmentBlock, SymbolList

FragmentBlock = "::"

SymbolList = SymbolListOpen, SymbolListBody, SymbolListClose

SymbolListOpen = "((", Whitespace

SymbolListClose = Whitespace, "))"

SymbolListBody
  = Word
  | Word, Linespace, SymbolListBody

LineBreak 
  = "\n" 
  | "\n", LineBreak

Linespace 
  = Space
  | Tab

Space 
  = "\s"
  | "\s", Space

Tab 
  = "\t"
  | "\t", Tab

Whitespace 
  = Space
  | Space, Whitespace
  | Tab
  | Tab, Whitespace
  | LineBreak
  | LineBreak, Whitespace
  | Empty 

Text 
  = Any 
  | Empty

Any = ? one or more occurrences of any character, including linebreaks ?

String = ? one or more occurrences of any character, not including linebreaks ?

Word = ? one or more occurences of any character, not including whitespace ?

Empty = ""
```
