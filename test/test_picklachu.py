import mock
from picklachu.picklachu import Picklachu


def test_i_pickle_you():
    with mock.patch('picklachu.storage.local.Local') as mock_storage:
        picklachu = Picklachu(mock_storage)
        picklachu.i_pickle_you(path='foobar', data={'foo': 'bar'})

        args, kwargs = mock_storage.persist.call_args

        assert 'foobar.pickle' == kwargs['path']
        assert b'\x80\x03}q\x00X\x03\x00\x00\x00fooq\x01X\x03\x00\x00\x00barq\x02s.' == kwargs['data']


def test_evolve():
    with mock.patch('picklachu.storage.local.Local') as mock_storage:
        mock_storage.retrieve.return_value = b'\x80\x03}q\x00X\x03\x00\x00\x00fooq\x01X\x03\x00\x00\x00barq\x02s.'

        picklachu = Picklachu(mock_storage)
        response = picklachu.evolve(path='foobar')

        args, kwargs = mock_storage.retrieve.call_args

        assert 'foobar.pickle' == kwargs['path']
        assert {'foo': 'bar'} == response
