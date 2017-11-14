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

### Escape

Escape a single character: `\`.

Escape a range of characters: `f`.

## Grammar

This grammar uses [Extended Backus-Naur Form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form).

```ebnf
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
  = LineSpace, TagExpr, WhiteSpace, LineBreak
  | LineSpace, SubtextExpr, WhiteSpace, LineBreak, MetaBody
  | LineSpace, SubtextExpr, WhiteSpace, LineBreak
  | LineSpace, SubtextExpr, WhiteSpace, LineBreak, MetaBody

TagExpr = Word, ":", String, LineBreak

SubtextExpr = Word, ":", String, LineBreak

Fragment 
  = FragmentBlock, Any, FragmentBlock
  | FragmentBlock, Any, FragmentBlock, SymbolList

FragmentBlock = "::"

SymbolList = SymbolListOpen, SymbolListBody, SymbolListClose

SymbolListOpen = "(("

SymbolListClose = "))"

SymbolListBody
 = Symbol
 | Symbol, SymbolListBody

Symbol = Word, LineSpace

LineBreak 
  = "\n" 
  | "\n", LineBreak

LineSpace 
  = Space
  | Tab

Space 
  = "\s"
  | "\s", Space

Tab 
  = "\t"
  | "\t", Tab

WhiteSpace 
  = Space
  | Space, WhiteSpace
  | Tab
  | Tab, WhiteSpace
  | LineBreak
  | LineBreak, WhiteSpace
  | Empty 

Text 
  = Any 
  | Empty

Any = ? one or more occurrences of any character, including a linebreak ?

String = ? one or more occurrences of any character, not including a linebreak ?

Word = ? one or more occurences of any character, not including whitespace ?

Empty = ""
```
