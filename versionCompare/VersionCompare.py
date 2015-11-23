'''
This contains a set of functions used to do semantic version comparisons.
Typical entry point would be the "versionCompare" function that will get the
current version number, the version number to be compared against and the
operator.
'''

def compEq(ver, comp):
    '''
    This function will accept two version numbers and check if they are the same.

    Parameters:
      ver:   list:   The "current" version number split at the "."
      comp:  list:   The version number to compare against split at the "."

    Returns:
      Boolean: True if versions are equal, False if not
    '''

    index = 0 #basic index variable

    while index < len(ver):
        #Perform the actual comparison on the current version parts
        if int(ver[index]) != int(comp[index]):
            return False

        index+=1

    return True

def compGT(ver, comp):
    '''
    This function will accept two version numbers and check if one is greater
    than the other.

    Parameters:
      ver:   list:   The "current" version number split at the "."
      comp:  list:   The version number to compare against split at the "."

    Returns:
      Boolean: True if "current" version is greater than the comparison version.
        otherwise returns False
    '''

    index = 0 #basic index variable

    while index < len(ver):
        #Comparison to see if version is greater than compare version. Test success if true.
        if int(ver[index]) > int(comp[index]):
            return True

        #Comparison to see if version is less than compare version. Test failed if true.
        if int(ver[index]) < int(comp[index]):
            return False

        index+=1

    return False #Default case meaning versions are equal

def compGTEq(ver, comp):
    '''
    This function will accept two version numbers and check if one is greater
    than or equal to the other.

    Parameters:
      ver:   list:   The "current" version number split at the "."
      comp:  list:   The version number to compare against split at the "."

    Returns:
      Boolean: True if the "current" version is greater than or equal to the
        comparison version, False otherwise.
    '''

    index = 0 #basic index variable

    while index < len(ver):
        #Comparison to see if version is greater than compare version. Test success if true.
        if int(ver[index]) > int(comp[index]):
            return True

        #Comparison to see if version is less than compare version. Test failed if true.
        if int(ver[index]) < int(comp[index]):
            return False

        index+=1

    return True #Default case meaning versions are equal

def compPes(ver, comp):
    '''
    This function will accept two version numbers and do a pessimistic
    comparison.

    Parameters:
      ver:   list:   The "current" version number split at the "."
      comp:  list:   The version number to compare against split at the "."

    Returns:
      Boolean: True if the first two numbers of the versions are the same and
        the third number in the "current" version is greater than or equal to
        the corresponding number in the comparison version, False otherwise.
    '''

    index = 0 #basic index variable

    #Comparison to make sure the first two version numbers are equal. Test fails if they are not.
    while index < len(ver)-1:
        if int(ver[index]) != int(comp[index]):
            return False

        index+=1

    #Comparison of last version number "Patch number". If current patch is less than expected test fails.
    if ver[-1] < comp[-1]:
        return False

    return True #Comparison passed.

def compLT(ver, comp):
    '''
    This function will accept two version numbers and check one is less than the
    other.

    Parameters:
      ver:   list:   The "current" version number split at the "."
      comp:  list:   The version number to compare against split at the "."

    Returns:
      Boolean: True if the "current" version is less than the coparison version,
        False otherwise.
    '''

    index = 0 #basic index variable

    while index < len(ver):
        #Comparison to see if version is less than compare version. Test success if true.
        if int(ver[index]) < int(comp[index]):
            return True

        #Comparison to see if version is greater than compare version. Test failed if true.
        if int(ver[index]) > int(comp[index]):
            return False

        index+=1

    return False #Default case meaning versions are equal

def compLTEq(ver, comp):
    '''
    This function will accept two version numbers an check if one is less than
    or equal to the other.

    Parameters:
      ver:   list:   The "current" version number split at the "."
      comp:  list:   The version number to compare against split at the "."

    Returns:
      Boolean: True if "current" version is less than or equal to the comparison
        version number. False otherwise.
    '''

    index = 0 #basic index variable

    while index < len(ver):
        #Comparison to see if version is less than compare version. Test success if true.
        if int(ver[index]) < int(comp[index]):
            return True

        #Comparison to see if version is greater than compare version. Test failed if true.
        if int(ver[index]) > int(comp[index]):
            return False

        index+=1

    return True #Default case meaning versions are equal

def versionCompare(ver, comp, operator):
    '''
    This function takes two version numbers as strings and an operator as a
    string and runs the appropriate comparison of the version numbers.

    Parameters:
      ver: String: The "current" version as a string.
      comp: String: The comparison version as a string.
      operator: String: The comparison operator as a string.

     Returns:
       Boolean: The boolean comparison result.
     '''

    if operator == '==':
        return compEq(ver.split('.'), comp.split('.'))

    elif operator == '>':
        return compGT(ver.split('.'), comp.split('.'))

    elif operator == '>=':
        return compGTEq(ver.split('.'), comp.split('.'))

    elif operator == '~>':
        return compPes(ver.split('.'), comp.split('.'))

    elif operator == '<':
        return compLT(ver.split('.'), comp.split('.'))

    elif operator == '<=':
        return compLTEq(ver.split('.'), comp.split('.'))


if __name__ == '__main__':
    '''
    This section of code allows this to be run on command line by passing in the
    arguments in order "version", "compare" and "operator". This will then run
    the versionCompare function passing in the appropriate values.
    '''

    #Setup command line arguments
    import argparse

    parser = argparse.ArgumentParser(description='Comparison between two version numbers')
    parser.add_argument('version', help='The current version to compare')
    parser.add_argument('compare', help='The version to compare against')
    parser.add_argument('operator',
        help='The comparison operator, can be "==", ">", ">=", "~>", "<", "<="')
    args = parser.parse_args()

    #Make sure operator argument is one of the expected values.
    if args.operator not in ['==', '>', '>=', '~>', '<', '<=']:
        print 'Invalid comparison operator. Please choose from the following'
        print '"==", ">", ">=", "~>", "<", "<="'
        raise ValueError('Invalid comparison operator provided')

    #Print comparison result.
    print versionCompare(args.version, args.compare, args.operator)
