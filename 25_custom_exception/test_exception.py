"""
Test untuk Custom Exception
"""
import pytest
from main import (
    AppError, ValidationError, NotFoundError,
    DetailedError, LoginError, TokenExpiredError,
    AppException, ConnectionError, QueryError,
    APIError, NotFoundAPIError, UserNotFoundError,
    DuplicateUserError, get_user, create_user,
    users_db,
)


class TestCustomExceptionDasar:
    def test_validation_error(self):
        with pytest.raises(ValidationError):
            raise ValidationError("test error")

    def test_is_app_error(self):
        with pytest.raises(AppError):
            raise ValidationError("test")

    def test_error_message(self):
        e = ValidationError("test message")
        assert str(e) == "test message"


class TestDetailedError:
    def test_attributes(self):
        e = DetailedError("Error", code=422, details={"field": "email"})
        assert e.code == 422
        assert e.details["field"] == "email"

    def test_to_dict(self):
        e = DetailedError("Error", code=400)
        d = e.to_dict()
        assert d["error"] == "Error"
        assert d["code"] == 400
        assert d["details"] == {}


class TestExceptionHierarchy:
    def test_login_error_is_auth_error(self):
        with pytest.raises(AuthError):
            raise LoginError("test")

    def test_token_expired_is_auth_error(self):
        with pytest.raises(AppException):
            raise TokenExpiredError("test")

    def test_connection_error_is_database_error(self):
        with pytest.raises(DatabaseError):
            raise ConnectionError("test")


class TestNotFoundAPIError:
    def test_attributes(self):
        e = NotFoundAPIError("User", 123)
        assert e.status_code == 404
        assert e.resource == "User"
        assert e.resource_id == 123

    def test_error_message(self):
        e = NotFoundAPIError("Product", 456)
        assert "Product" in str(e)
        assert "456" in str(e)


class TestUserService:
    def test_get_user_found(self):
        user = get_user(1)
        assert user["nama"] == "Budi"

    def test_get_user_not_found(self):
        with pytest.raises(UserNotFoundError) as exc_info:
            get_user(999)
        assert exc_info.value.user_id == 999

    def test_create_user_success(self):
        new_user = create_user("Test User", "test@example.com")
        assert new_user["nama"] == "Test User"
        assert new_user["email"] == "test@example.com"

    def test_create_user_duplicate(self):
        with pytest.raises(DuplicateUserError) as exc_info:
            create_user("Budi", "budi@test.com")
        assert exc_info.value.email == "budi@test.com"
