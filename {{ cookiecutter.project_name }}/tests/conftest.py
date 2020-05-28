import faker  # type: ignore
import pytest  # type: ignore


@pytest.fixture(scope="session")
def fake():
    return faker.Faker()
