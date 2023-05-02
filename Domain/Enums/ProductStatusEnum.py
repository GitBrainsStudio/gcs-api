import enum

class ProductStatusEnum(enum.IntEnum) :

    InProgress = 0,
    Shipped = 1,
    Arrived = 2,
    Solded = 3