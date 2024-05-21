#!/usr/bin/env python3
'''
This script is all about pagination module
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    This function returns a range oof indexes of a pagination param
    '''
    first = (page - 1) * page_size
    last = first + page_size
    return (first, last)
