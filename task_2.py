from pathlib import Path
from typing import List, Dict

FILE_NAME = Path("cats_list.txt")


def get_cats_info(path: Path) -> List[Dict]:
    if not Path.exists(path):
        print("Please, enter correct path")
        return []

    formated_list = []
    with open(path, "r",) as cats_info:
        lines = cats_info.readlines()
        for line in lines:
            formated = line.strip().split(",")
            formated_list.append({
                "id": formated[0],
                "name": formated[1],
                "age": formated[2]
            })

    return formated_list


print(get_cats_info(FILE_NAME))
