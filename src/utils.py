import re
from typing import Union
from typing import Any
from collections import deque


def print_data_structure(
    data: dict[str, dict[str, Union[None, dict[str, deque[Any]]]]]
) -> None:
    """
    Print the data structure
    Function not used in the final code
    """
    print(type(data))
    for base_name, group in data.items():
        print(f"Message Group: {base_name}")
        print("  Signals:")
        for signal in group:
            print(f"    - {signal}")
        print(" ")


def natural_sort_key(item: Any) -> Any:
    """
    Sort by natural order
    :param item: The item to sort
    :return: The sorted item
    """
    name = item[0]
    match = re.search(r"(\d+)$", name)
    return (
        name[: match.start()] if match else name,
        int(match.group(0)) if match else 0,
    )


def base_name(message: str) -> str:
    """
    Get the base name of the message
    :param message: The message name
    :return: The base name
    """
    return re.sub(r"_\d+$", "", message)
