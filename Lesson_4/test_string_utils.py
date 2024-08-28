import pytest
from string_utils import StringUtils

utils = StringUtils()
@pytest.mark.parametrize( 'word, result',[
    ("skypro", "Skypro"),
    ("скайпро", "Скайпро"),
    ("sky про", "Sky про"),
    ("123", "123"),
    ])
def test_positive_capitilize(word, result):
    utils = StringUtils()
    res = utils.capitilize(word)
    assert res == result


@pytest.mark.parametrize( 'word, result' ,[
    ("", ""),
    ("  ", "  ")
    ])
def test_negative_capitilize(word, result):
    utils = StringUtils()
    res = utils.capitilize(word)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize( 'word, result' ,[
    (None, None)
    ])
def test_none_capitilize(word, result):
    utils = StringUtils()
    res = utils.capitilize(word)
    assert res == result


@pytest.mark.parametrize( 'word, result',[
    ("   Skypro", "Skypro"),
    ("   Скайпро   ", "Скайпро   "),
    ("   123", "123"),
    ("   good day", "good day")
    ])
def test_positive_trim(word, result):
    utils = StringUtils()
    res = utils.trim(word)
    assert res == result


@pytest.mark.parametrize( 'word, result',[
    ("", ""),
    ("   ", "")
    ])
def test_negative_trim(word, result):
    utils = StringUtils()
    res = utils.trim(word)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize( 'word, result',[
    (None, None)
    ])
def test_negative_trim(word, result):
    utils = StringUtils()
    res = utils.trim(word)
    assert res == result


@pytest.mark.parametrize( 'list, delimeter, result',[
    ("S,k,y,p,r,o", ",", ["S", "k", "y", "p", "r", "o"]),
    ("С:к:а:й:п:р:о",":", ["С","к","а","й","п","р","о"]),
    ("1-2-3-4", "-", ["1","2","3","4"])
    ])
def test_positive_to_list(list, delimeter, result):
    utils = StringUtils()
    res = utils.to_list(list, delimeter)
    assert res == result


@pytest.mark.parametrize( 'list, delimeter, result',[
    ("   ","",[])
      ])
def test_negative_to_list(list, delimeter, result):
    utils = StringUtils()
    res = utils.to_list(list, delimeter)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize( 'list, delimeter, result',[
    (None, None,[])
      ])
def test_none_to_list(list, delimeter, result):
    utils = StringUtils()
    res = utils.to_list(list, delimeter)
    assert res == result


@pytest.mark.parametrize('word, symbol, result',[
("Alexander", "x", True or False),
("12345", "6", False),
("2024 year"," ", True)
])
def test_posttive_contains(word, symbol, result):
    utils = StringUtils()
    res = utils.contains(word, symbol)
    assert res == result


@pytest.mark.xfail
def test_negative_contains():
    utils = StringUtils()
    with pytest.raises(ValueError):
        utils.contains("123456", "-1")
    

@pytest.mark.xfail
def test_none_contains():
    utils = StringUtils()
    res = utils.contains(None, None)
    assert res == False


@pytest.mark.parametrize('word, delet, result',[
("Python", "th", "Pyon"),
("Питон", "Пи", "тон"),
("12345", "23", "145")
])
def test_posttive_delete_symbol(word, delet, result):
    utils = StringUtils()
    res = utils.delete_symbol(word, delet)
    assert res == result


@pytest.mark.xfail
def test_none_delete_symbol():
    utils = StringUtils()
    res = utils.delete_symbol(None, None)
    assert res == None
    

def test_negative_delete_symbol():
    utils = StringUtils()
    res = utils.delete_symbol("Sky", "  ")
    assert res == "Sky"


@pytest.mark.parametrize('word, symbol, result',[
("Word", "W", True),
("Дом", "Д", True),
("123", "1", True),
("Winter","t", False)
])
def test_positive_starts_with(word, symbol, result):
    utils = StringUtils()
    res = utils.starts_with(word, symbol)
    assert res == result


@pytest.mark.xfail
def test_none_starts_with():
    utils = StringUtils()
    res = utils.starts_with(None, None)
    assert res == None


@pytest.mark.xfail
@pytest.mark.parametrize('word, symbol, result',[
("Word", "d", True),
("Дом", "Д", False)
])
def test_negative_starts_with(word, symbol, result):
    utils = StringUtils()
    res = utils.starts_with(word, symbol)
    assert res == result


@pytest.mark.parametrize('word, symbol, result',[
("Word", "d", True),
("Дом", "м", True),
("123", "3", True),
("Winter","n", False)
])
def test_positive_end_with(word, symbol, result):
    utils = StringUtils()
    res = utils.end_with(word, symbol)
    assert res == result


@pytest.mark.xfail
def test_none_end_with():
    utils = StringUtils()
    res = utils.end_with(None, None)
    assert res == None


@pytest.mark.xfail
@pytest.mark.parametrize('word, symbol, result',[
("Word", "d", False),
("Дом", "Д", True)
])
def test_negative_end_with(word, symbol, result):
    utils = StringUtils()
    res = utils.end_with(word, symbol)
    assert res == result


@pytest.mark.parametrize('string, result',[
    ("", True),
    (" ", True),
    ("Sky", False),
    ("1234", False)
    ])
def test_positive_is_empty(string, result):
    utils = StringUtils()
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.xfail   
def test_none_is_empty():
    utils = StringUtils()
    res = utils.is_empty(None, None)
    assert res == None


@pytest.mark.parametrize('lst, jouner, result',[
(["s","a","s","a"],",", "s,a,s,a"),
(["1","2","3"], ";", "1;2;3"),
(["Privet", "mir"], "!", "Privet!mir")
])
def test_positive_list_to_string(lst, jouner, result):
    utils = StringUtils()
    res = utils.list_to_string(lst, jouner)
    assert res == result


@pytest.mark.xfail   
def test_none_list_to_string():
    utils = StringUtils()
    res = utils.list_to_string(None, None)
    assert res == None    


@pytest.mark.xfail   
def test_negative_list_to_string():
    utils = StringUtils()
    res = utils.list_to_string([], ",")
    assert res == []