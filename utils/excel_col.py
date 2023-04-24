# https://stackoverflow.com/questions/19153462/get-excel-style-column-names-from-column-number


def excel_col(n: int) -> str:
    """Generate Excel column name for a given number - start from 1=A

    Args:
        n (int): An integer, 1 = A

    Returns:
        str: An excel style column name, ie 1=A, ...
    """
    quot, rem = divmod(n - 1, 26)
    return excel_col(quot) + chr(rem + ord('A')) if n != 0 else ''
