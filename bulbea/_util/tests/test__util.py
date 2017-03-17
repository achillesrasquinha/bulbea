import pytest

from bulbea._util import (
    _raise_type_error,
    _get_type_name,
    _check_type,
    _validate_in_range,
    _validate_date,
    _assign_if_none
)

def test__raise_type_error():
    with pytest.raises(TypeError):
        _raise_type_error(
            expected_type_name = 'expected',
            recieved_type_name = 'recieved'
        )

def test__get_type_name():
    assert _get_type_name('foo') == 'str'
    assert _get_type_name(12345) == 'int'
    assert _get_type_name(1.234) == 'float'

def test__check_type():
    with pytest.raises(TypeError):
        _check_type('foo', type_ = int, raise_err = True, expected_type_name = 'str')
    with pytest.raises(TypeError):
        _check_type(12345, type_ = str, raise_err = True, expected_type_name = 'int')

    assert _check_type('bar', type_ = str) == True
    assert _check_type('foo', type_ = int) == False

def test__validate_in_range():
    with pytest.raises(ValueError):
        _validate_in_range(123, 0, 1, raise_err = True)

    assert _validate_in_range(0.5, 0, 1) == True
    assert _validate_in_range(123, 0, 1) == False

def test__validate_date():
    with pytest.raises(ValueError):
        _validate_date('12/12/12', raise_err = True)

    assert _validate_date('2012-01-01') == True
    assert _validate_date('2012/01/01') == False

def test__assign_if_none():
    assert _assign_if_none(None, 1) == 1
    assert _assign_if_none(1,'foo') == 1
