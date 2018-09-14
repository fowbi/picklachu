# Picklachu

<img width="236" alt="picklachu_small" src="https://user-images.githubusercontent.com/449320/45255558-636fde00-b388-11e8-8742-2bdb63e62c9f.png">

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
    picklachu.i_pickle_you({'foo':'bar'}, 'foobar')
```

Retrieving data:

```
from picklachu import Picklachu

with Picklachu(LocalStorage('/tmp/')) as picklachu:
    picklachu.evolve('foobar') #  will return {'foo', 'bar'}
```

## TODO

- implement S3
