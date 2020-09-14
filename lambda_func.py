from functools import reduce

if __name__ == "__main__":
    
    items = [4, 3, 2, 1]
    
    # MAP: returns modified list; same func to each item
    # list ( map ( funct, list ) )
    lambda_func_map = lambda x : x * 2
    map_modified = list(map(lambda_func_map, items))
    print('MAP : ' + str(map_modified))
    
    # FILTER: filter from list; returns modified list
    # list ( filter( funct, list ) )
    lambda_func_filter = lambda x : x > 2
    filter_modified = list(filter(lambda_func_filter, items))
    print('FILTER: ' + str(filter_modified))
    
    # REDUCE: returns item; performs function on all items in seq
    # reduce ( func, list )
    lambda_func_reduce = lambda x, y : x * y
    reduce_modified = reduce(lambda_func_reduce, items)
    print('REDUCE: ' + str(reduce_modified))
