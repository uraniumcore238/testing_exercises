import pytest

from functions.level_4.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field


@pytest.mark.parametrize('value', ['value1', '[tool:app-config]', 'field'])
def test__five_extra_fields__return_none_if_the_str_is_not_in_config_fields(file_path_config, value):
    assert fetch_app_config_field(file_path_config, value) is None


def test__five_extra_fields__return_value_if_the_str_is_in_config_fields(file_path_config):
    assert fetch_app_config_field(file_path_config, 'field1') == 'value1'
