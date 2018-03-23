def first_last(alist):
    return alist[0] == alist[-1]


def reverse_list(alist):
    return alist[::-1]


def reverse_list2(thelist):
    outlist = []
    for elem in thelist:
        outlist.insert(0, elem)
    return outlist
        


def middle_elements(list1, list2):
    if len(list1) % 2 == 0 or len(list2) % 2 ==0:
        print("One or both lists have an even number of elements; can't be processed.")
        return

    # at this point, both lists are of odd length

    list1middle = list1[len(list1) // 2]
    list2middle = list2[len(list2) // 2]
    return [list1middle, list2middle]


def xyz_there(string):
    '''this function will get confused with strings containing multiple instances of 'xyz'
    '''
    # if there is no 'xyz' then return False
    if string.find('xyz') == -1:
        return False
    # if 'xyz' is at the beginning of the string, it can't be preceded by a '.' so return False
    if string.find('xyz') == 0:
        return False

    # at this point there is an xyz at a position other than 0

    checkpos = string.find('xyz') - 1
    return string[checkpos] == '.'
    

def xyz_there2(string):
    if len(string) < 4:
        return False
    
    for x in range(len(string) - 3):
        substr = string[x:x+4]
        if string[x:x+4] == '.xyz':
            return True
    return False


def double_char(string):
    outstr = ""
    for c in string:
        outstr += c * 2
    return outstr


def nodup(thelist):
    outlist = []
    for elem in thelist:
        if elem not in outlist:
            outlist.append(elem)
    return outlist

