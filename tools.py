import random
import matplotlib.figure
import matplotlib.axes


def map_value(current_span: tuple[float, float], new_span: tuple[float, float], _value: float):
    """
    An equalant of arduino's map function

    :param current_span:
    :param new_span:
    :param _value:
    :return:
    """

    return ((_value - current_span[0])/(current_span[1] - current_span[0]) * (new_span[1] - new_span[0])) + new_span[0]


class Map:
    def __init__(self, current_span: tuple[float, float], new_span: tuple[float, float]):
        self.current_span = current_span
        self.new_span = new_span

    def covert(self, _value):
        return ((_value - self.current_span[0])/(self.current_span[1] - self.current_span[0])
                * (self.new_span[1] - self.new_span[0])) + self.new_span[0]


def corrupt_pattern(original_pattern: list, degree: float, lower_bound: float, upper_bound: float) -> list:
    """
    Takes a list of numbers, replaces randomly picked values of that list with random values(corrupt values)
    and return the altered list

    :param original_pattern: the pattern that should be corrupted
    :param degree: the fraction of values of the list that should be corrupted
    :param lower_bound: lowest value of a corrupted value could have
    :param upper_bound: the highest value a corrupted value could have
    :return: original list with the corrupted values

    """

    copy_list = [i for i in original_pattern]
    corrupt_amount = round(len(original_pattern) * degree)

    for _ in range(corrupt_amount):
        rand_index = random.randint(0, len(copy_list)-1)
        rand_val = (upper_bound - lower_bound) * random.random() + lower_bound
        selected_val = copy_list.pop(rand_index)

        original_index = original_pattern.index(selected_val)
        original_pattern[original_index] = rand_val

    return original_pattern


def decorate_graph(x_label: str, y_label: str, _fig: matplotlib.figure.Figure, _ax: matplotlib.axes._axes.Axes):
    _fig.patch.set_facecolor('#242424')
    _ax.set_xlabel(x_label, color="white")
    _ax.set_ylabel(y_label, color="white")
    _ax.yaxis.grid(color='gray', linestyle='dashed')
    _ax.patch.set_alpha(0.03)
    _ax.tick_params(axis='x', colors='white')
    _ax.tick_params(axis='y', colors='white')


if __name__ == "__main__":
    print(map_value((-1, 1), (0, 100), -0.50))
