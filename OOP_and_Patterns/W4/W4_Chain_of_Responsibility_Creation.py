class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, got_val):
        self.type = 'GET'
        self.got_val = got_val


class EventSet:
    def __init__(self, value):
        self.type = 'SET'
        self.value = value


class NullHandler:
    def __init__(self, next_chain=None):
        self.next = next_chain

    def handle(self, obj, event):
        if self.next:
            return self.next.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.type == 'GET' and event.got_val is int:
            return obj.integer_field
        elif event.type == 'SET' and isinstance(event.value, int):
            obj.integer_field = event.value
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.type == 'GET' and event.got_val is float:
            return obj.float_field
        elif event.type == 'SET' and isinstance(event.value, float):
            obj.float_field = event.value
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.type == 'GET' and event.got_val is str:
            return obj.string_field
        elif event.type == 'SET' and isinstance(event.value, str):
            obj.string_field = event.value
        else:
            return super().handle(obj, event)

