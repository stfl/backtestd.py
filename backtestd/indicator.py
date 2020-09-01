# {'name': 'ash',
#     'inputs': [[9.0, 4.0, 20.0, 1.0],
#             [2.0, 0.0, 10.0, 1.0],
#             [0.0, 0.0, 1.0, 1.0],
#             [0.0, 0.0, 3.0, 1.0],
#             [0.0, 0.0, 6.0, 1.0]],
#     'shift': 0,
#     'buffers': [0],
#     'class': 'ZeroLineCross',
#     'filename': 'ASH'},
#                   'params': [0, 1, 2],
#                   'levels': [75, 25, 25,
#     'input_description': [{name, type, descrete}]

# pub struct Indicator {
#     pub name: String,
#     pub filename: Option<String>,
#     pub class: SignalClass,
#     pub inputs: Vec<Vec<BigDecimal>>,
#     pub buffers: Option<Vec<u8>>,
#     pub params: Option<Vec<BigDecimal>>,
#     pub shift: u8,
# }

# def split_longest_input(indi):


def get_indi_set_input_names(indi_set):
    """
    get the names of the inputs for all functions in the set
    prepend with function like Confirm_<name>
    """
    # TODO
    return None


def get_indi_input_names(indi):
    """
    get the names of the inputs according to input_description
    generate input_%i if not defined
    """
    try:
        return [d['name'] for d in indi["input_description"]]
    except KeyError:
        ["input_" + str(i) for i in range(len(indi.inputs))]
