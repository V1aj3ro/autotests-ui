import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows','linux', 'debian'])
@pytest.mark.parametrize('browser', ['firefox', 'chromium', 'webkit'])
def test_multiple_of_numbers(browser: str, os: str):
    assert len(os+browser) > 0


@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'Running test on user: {user} and account: {account}')

    def test_user_without_operations(self, user: str):
        print(f'Running test on user: {user}')



users = {
    '+70000000011': 'user with money on bank account',
    '+70000000022': 'user without money on bank account',
    '+70000000033': 'user with operations on bank account'
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...