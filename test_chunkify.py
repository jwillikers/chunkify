import pytest
from chunkify import chunkify


def test_accept_empty_string():
    assert chunkify('', 5, 'x') == ['xxxxx']


def test_should_reject_chunk_size_of_zero():
    with pytest.raises(ValueError):
        chunkify('ABCDEFG', 0, 'x')


def test_should_reject_negative_chunk_size():
    with pytest.raises(ValueError):
        chunkify('ABCDEFG', -1, 'x')


def test_should_reject_s_given_an_int():
    with pytest.raises(TypeError):
        chunkify(1, 1, 'x')


def test_should_reject_s_given_an_float():
    with pytest.raises(TypeError):
        chunkify(5.5, 1, 'x')


def test_should_reject_s_given_a_list_of_ints():
    with pytest.raises(TypeError):
        chunkify([1, 2, 3, 4, 5], 1, 'x')


def test_should_reject_given_an_int_for_fill():
    with pytest.raises(TypeError):
        chunkify('ABCDEFG', 3, 1)


def test_should_reject_given_a_float_for_fill():
    with pytest.raises(TypeError):
        chunkify('ABCDEFG', 3, 1.2)


def test_should_reject_given_a_list_for_fill():
    with pytest.raises(ValueError):
        chunkify('ABCDEFG', 3, [])


def test_should_reject_given_a_string_with_more_than_a_single_character_for_fill():
    with pytest.raises(ValueError):
        chunkify('ABCDEFG', 3, 'xx')


def test_should_reject_a_list_of_strings_given_for_fill():
    with pytest.raises(TypeError):
        chunkify('ABCDEFG', 3, ['x'])


def test_chunks_of_size_one():
    assert chunkify('ABCDEFG', 1, 'z') == ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def test_should_chunkify_the_example_correctly():
    assert chunkify('ABCDEFG', 3, 'x') == ['ABC', 'DEF', 'Gxx']


def test_should_work_just_the_same_given_a_list_of_strings():
    assert chunkify(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 3, 'x') == ['ABC', 'DEF', 'Gxx']
