import pytest

from api.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(
        email="dark.killa@bol.com.br",
        username="d4rk_k1ll4",
        user_pass="ilovekittens@777",
        first_name="Oscar",
        last_name="Alho",
        country="Brasil",
        state="São Paulo",
        city="Piraporinha do Leste",
        postal_code="12345-789",
        address="R. dos Bobos, nº0"
    )

    assert user.username == "d4rk_k1ll4"
    assert user.first_name == "Oscar"
    assert user.country == "Brasil"
    assert user.city == "Piraporinha do Leste"
    assert user.id is not None