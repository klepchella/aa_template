from typing import Generator, Sequence

from pydantic.v1.typing import AnyCallable


class CSVInts(str):
    def __init__(self, csv_ints: str) -> None:
        # У строк нет базового инициализатора, т.к. это неизменяемый тип, соответственно он не вызывается
        self._parsed = tuple(int(item) for item in csv_ints.split(","))

    @property
    def values(self) -> Sequence[int]:
        return self._parsed

    @classmethod
    def __get_validators__(cls) -> Generator[AnyCallable, None, None]:
        yield cls

    @classmethod
    def __modify_schema__(cls, schema: dict[str, object]) -> None:
        schema.update(min_length=1, regex=r"(\d+,)*\d+", examples=["1", "1,2"])
