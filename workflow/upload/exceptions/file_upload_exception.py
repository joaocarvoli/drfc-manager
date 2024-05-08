class FileUploadException(Exception):
    """Exception raised for errors related to files uploads."""

    def __init__(self, message="Error uploading file.", original_exception=None):
        """
        Initialize a FileException.

        Args:
            message (str): Explanation of the error.
            original_exception (Exception): The original exception that caused this exception.
        """
        self.message = message
        self.original_exception = original_exception
        super().__init__(message)

    def __str__(self):
        if self.original_exception:
            return f"{self.message} Original Exception: {str(self.original_exception)}"
        else:
            return self.message
