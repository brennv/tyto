## Approaches

Rolling window
- chunk across the passage looking for best fit
- TODO gain efficiencies by adapting a modified z algorithm

## Way ahead

Density mapping
- create map of transcript words found in passage
- index transcript against passage based on map density

Difflib
- guessing it uses line count to help establish mapping

Graphing
- establish relationships measuring confidence between words

Elastic
- create combinatoric records of possible mappings
- apply elasticsearch, select the top result
