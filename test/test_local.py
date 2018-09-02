import os
import pickle

from picklachu.storage.local import Local


def set_up_tmp(func):
    """Set up tmp folder"""
    def wrapper():
        if not os.path.isdir('tmp/'):
            os.mkdir('tmp')

        if os.path.isfile('tmp/foobar.pickl'):
            os.remove('tmp/foobar.pickle')

    return wrapper


@set_up_tmp
def test_local_storage():
    """Test storing data to the local file system"""
    if not os.path.isdir('tmp/'):
        os.mkdir('tmp')

    local = Local(directory='tmp/')
    local.persist(path='foobar.pickle', data=pickle.dumps({'foo':'bar'}))

    assert os.path.isfile('tmp/foobar.pickle')

    os.remove('tmp/foobar.pickle')


@set_up_tmp
def test_local_retrieve():
    """Test retrieving the stored data from the local file system"""
    local = Local(directory='tmp/')
    local.persist(path='foobar.pickle', data=pickle.dumps({'foo':'bar'}))

    response = local.retrieve(path="foobar.pickle")

    assert pickle.loads(response)

    os.remove('tmp/foobar.pickle')
