class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    LOGIN_URL = f"{BASE_URL}/login"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_URL = f"{BASE_URL}/reset-password"
    PROFILE_URL = f"{BASE_URL}/account/profile"
    ORDER_HISTORY_URL = f"{BASE_URL}/account/order-history"
    ORDER_FEED_URL = f"{BASE_URL}/feed"

    # API ручки для создания/удаления пользователей в фикстурах
    REGISTER_API = f"{BASE_URL}/api/auth/register"
    USER_API = f"{BASE_URL}/api/auth/user"