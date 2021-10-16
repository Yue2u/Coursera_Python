import os
import csv


def isfloat(number):
    array = number.split('.')
    if 2 < len(array) < 1:
        return False
    for elem in number.split('.'):
        if not str.isdigit(elem):
            return False
    return True


def parse_whl(whl):
    zero_array = [0.0, 0.0, 0.0]
    result = []
    body_whl = whl.split(sep='x')
    if len(body_whl) != 3:
        return zero_array
    for elem in body_whl:
        if not isfloat(elem):
            return zero_array
        result.append(float(elem))
    return result


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count or 0)


class Truck(CarBase):

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        whl = parse_whl(body_whl)
        self.body_length = whl[0]
        self.body_width = whl[1]
        self.body_height = whl[2]

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def check_default_inputs(inputs):
    photo_extensions = ('.jpeg', '.jpg', '.png', '.gif')
    return len(inputs) == 7 and inputs[0] and inputs[1] and inputs[3] and inputs[5] and os.path.splitext(inputs[3])[1] in photo_extensions


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if check_default_inputs(row):
                if row[0] == 'car' and row[2]:
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine' and row[6]:
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))

    return car_list


def _main():
    print(get_car_list('cars.csv'))


if __name__ == '__main__':
    _main()
