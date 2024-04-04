import pytest

from functions.level_4.five_extra_fields import fetch_app_config_field, fetch_extra_fields_configuration


@pytest.mark.parametrize('value', ['value1', '[tool:app-config]', 'field'])
def test__five_extra_fields__return_none_if_the_str_is_not_in_config_fields(file_path, value):
    assert fetch_app_config_field(file_path, value) is None


def test__five_extra_fields__return_value_if_the_str_is_in_config_fields(file_path):
    assert fetch_app_config_field(file_path, 'field1') == 'value1'


def test__fetch_extra_fields_configuration__return_empty_dict_if_there_is_no_extrafield(file_path):
    assert fetch_extra_fields_configuration(file_path) == {}


def test__fetch_extra_fields_configuration__return_field_and_its_type_if_there_is_extrafield(file_path_config):
    assert fetch_extra_fields_configuration(file_path_config) == {'field1': int}
