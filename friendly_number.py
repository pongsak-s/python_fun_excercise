import math


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    print( "problem with number: %s" % str(number) )
    power_number = list(reversed([pow(base, x_i) for x_i in range(len(powers))]))
    print(power_number)
    print(base)
    index_result = 0
    times = 0
    for index, each in enumerate(power_number):
        print("each:%d, number: %d" %
              (each, number))
        times = math.floor(abs(number) / each)
        times = (-1) * times if number < 0 else times
        if times is not 0:
            index_result = len(powers) - index - 1
            number = number - (times * each)
            print("times:%d, len(powers):%d, index:%d, each:%d, number: %d" %
                  (times, len(powers), index, each, number))
            break

    print("returning: %s" % str("%s%s" % (times, powers[index_result])))
    strResult = str("%s%s" % (times, powers[index_result]))

    if decimals:
        pass
        residual = number / power_number[len(powers) - index_result -1]
        number_format = "%." + str(decimals) + "f%s"
        print(">0dec returning: %s" % str(number_format % ( times + residual, powers[index_result] ) ))
        strResult = str(number_format % ( times + residual, powers[index_result] ))
    if suffix:
    	strResult += suffix
    return strResult




        # if not decimals:
    # 	print("0dec returning: %s" % str("%s%s" % (times, powers[index_result])))
    # 	return "%s%s" % (times, powers[index_result])
    # else:
    # 	residual = number / power_number[index_result]
    # 	print(">0dec returning: %s" % str("%.2f%s" % ( times + residual, powers[index_result] ) ))
    # 	return  "%.2f%s" % ( times + residual, powers[index_result])


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024,
                           suffix='iB') == '976MiB', '976MiB'

    assert friendly_number(12000000, decimals=3) == '12.000M'

    assert friendly_number(-150, base=100, powers=["","d","D"]) == '-1d'
