class ErrorSchema:
    errors = {
        "InternalServerError": {
            "message": "Something went wrong, Please try after sometime.",
            "status": "fail",
            "code": 500
        },
        "UnauthorizedError": {
            "message": "Invalid email or password.",
            "status": "fail",
            "code": 401
        },
        "InvalidAdminTokenError": {
            "message": "Provide a valid admin auth token.",
            "status": "fail",
            "code": 401
        },
        "InvalidAuthTokenError": {
            "message": "Provide a valid auth token.",
            "status": "fail",
            "code": 401
        },
        "SignatureExpiredError": {
            "message": "Signature expired. Please log in again.",
            "status": "fail",
            "code": 401
        },
        "StockExistError": {
            "message": "Stock already exists. this",
            "status": "fail",
            "code": 403
        },
        "UserNotExistError": {
            "message": "User not exist in our system",
            "status": "fail",
            "code": 403
        },
        "OrderNotExistError": {
            "message": "Order not exist or you are not authorized to cancel this order",
            "status": "fail",
            "code": 403
        },
        "UserExistError": {
            "message": "User already exists. Please Log in.",
            "status": "fail",
            "code": 409
        },
    }

    @classmethod
    def get_response(cls, error_name, e=None):
        print(e)
        response_object = {
            'status': cls.errors[error_name]['status'],
            'message': cls.errors[error_name]['message']
        }
        return response_object, cls.errors[error_name]['code']
