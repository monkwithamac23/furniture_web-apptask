class CustomerInfoException(Exception):
    ...


class CustomerInfoNotFoundError(CustomerInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Customer Info Not Found"


class CustomerInfoInfoAlreadyExistError(CustomerInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Customer Info Already Exists"
