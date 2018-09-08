# Picklachu

Pickle data and store it somewhere

2 built-in storage types

- S3
- local filesystem

More can be derived from BaseStorage


## Usage

Persisting data:

```
from picklachu import Picklachu

with Picklachu(LocalStorage('/tmp/')) as picklachu:
    picklachu.i_pick_you({'foo':'bar'}, 'foobar')
```

Retrieving data:

```
from picklachu import Picklachu

with Picklachu(LocalStorage('/tmp/')) as picklachu:
    picklachu.evolve('foobar') #  will return {'foo', 'bar'}
```

## TODO

- implement S3
