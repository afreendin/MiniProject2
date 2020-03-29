






def confidenceinterval(lst, conf):
    x = mean(lst)
    std = st_dev(lst)
    if conf == 95:
        t = 1.96
    elif conf == 90:
        t = 1.64
    elif conf == 99:
        t = 2.58
    else:  # 95 default confidence percentage
        t = 1.96

    std_error = division(std, root(len(lst)))
    conf_upper = addition(x, multiplication(t, std_error))
    conf_upper = round(conf_upper, 2)
    conf_lower = subtraction(multiplication(t, std_error), x)
    conf_lower = round(conf_lower, 2)
    return conf_upper, conf_lower
