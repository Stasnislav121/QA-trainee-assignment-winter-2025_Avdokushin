import pytest
import allure

from requests import Response
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError


class ResponseHandler:
    @staticmethod
    def validate_response(response: Response, schema):
        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as err:
            pytest.fail(f'Ошибка при валидации ответа:\n{err}')

    @staticmethod
    def check_status_code(expect_status_code, actual_status_code):
        with allure.step(f"Проверка кода ответа {expect_status_code}"):
            assert actual_status_code == expect_status_code, (f"Код ответа запроса должен быть {expect_status_code}, "
                                                              f"получен {actual_status_code}")

    @staticmethod
    def check_status_is_200(response):
        ResponseHandler.check_status_code(expect_status_code=200, actual_status_code=response.status_code)
