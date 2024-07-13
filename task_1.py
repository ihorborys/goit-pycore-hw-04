from pathlib import Path
from typing import Tuple

FILE_NAME = Path("salary_file.txt")


def total_salary(path: Path) -> Tuple:
    if not Path.exists(path):
        print("Please, enter correct path")
        return 0, 0

    summ = 0
    count = 0
    with open(path, mode="r", encoding="utf-8") as fh:
        while True:
            line = fh.readline().strip()
            if not line:
                break
            current_salary = int(line.split(",")[1])
            summ += current_salary
            count += 1

    return summ, int(summ / count)


print(total_salary(FILE_NAME))
