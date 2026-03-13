import pytest
from project import rank_coin, coin_price, supply, maxsupply, volume_usd, change_percent


def fake_coin():
    return {
        "rank": "1",
        "priceUsd": "102345.678",
        "supply": "19600000.0",
        "maxSupply": "21000000.0",
        "volumeUsd24Hr": "35200000000.0",
        "changePercent24Hr": "2.34567"
    }

def fake_coin_no_supply():
    return {
        "rank": "3",
        "priceUsd": "0.5678",
        "supply": None,
        "maxSupply": None,
        "volumeUsd24Hr": "1500000000.0",
        "changePercent24Hr": "-1.23456"
    }


def test_rank_coin():
    assert rank_coin(fake_coin()) == "1"

def test_rank_coin_different_rank():
    coin = fake_coin()
    coin["rank"] = "42"
    assert rank_coin(coin) == "42"


def test_coin_price():
    assert coin_price(fake_coin()) == 102345.68

def test_coin_price_small_value():
    coin = fake_coin()
    coin["priceUsd"] = "0.004567"
    assert coin_price(coin) == 0.0

def test_coin_price_returns_float():
    assert isinstance(coin_price(fake_coin()), float)


def test_supply_returns_string():
    result = supply(fake_coin())
    assert isinstance(result, str)

def test_supply_when_none():
    assert supply(fake_coin_no_supply()) == "None"

def test_supply_not_empty():
    result = supply(fake_coin())
    assert result != ""


def test_maxsupply_returns_string():
    result = maxsupply(fake_coin())
    assert isinstance(result, str)

def test_maxsupply_when_none():
    assert maxsupply(fake_coin_no_supply()) == "None"

def test_maxsupply_not_empty():
    result = maxsupply(fake_coin())
    assert result != ""


def test_volume_usd_returns_string():
    result = volume_usd(fake_coin())
    assert isinstance(result, str)

def test_volume_usd_not_empty():
    assert volume_usd(fake_coin()) != ""


def test_change_percent_positive():
    assert change_percent(fake_coin()) == 2.346

def test_change_percent_negative():
    assert change_percent(fake_coin_no_supply()) == -1.235

def test_change_percent_returns_float():
    assert isinstance(change_percent(fake_coin()), float)