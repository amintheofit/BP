class RoseDictionary:
    def __init__(self):
        self.items = []

    def pop_item(self, raise_error=False, default=None, error_msg=None):
        try:
            key, value = self.items.pop()
            return value
        except IndexError as e:
            if raise_error:
                if error_msg:
                    raise KeyError(error_msg) from e
                else:
                    raise KeyError("error_msg") from e
            else:
                if default is not None:
                    return default
                else:
                    if error_msg is not None:
                        print(error_msg)
                    else:
                        print("Dictionary was empty and no default value/message was specified.")

    def get_item(self, key, raise_error=False, default=None, error_msg=None):
        for k, v in reversed(self.items):
            if k == key:
                return v

        if raise_error:
            if error_msg:
                raise KeyError(error_msg)
            else:
                raise KeyError("error_msg")
        else:
            if default is not None:
                return default
            else:
                if error_msg is not None:
                    print(error_msg)
                else:
                    print("Value was not found and no default value/message was specified.")

    def __setitem__(self, key, value):
        self.items.append((key, value))