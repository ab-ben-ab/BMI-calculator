def calculate(height, weight):
    global bmi

    try:
        bmi = weight / (height * height)
    except ZeroDivisionError:
        return 0, "DIVIDED BY ZERO"


def get_weight(bmi, height):
    WEIGHT = bmi * (height * height)
    return WEIGHT


def healthy_range():
    RANGE = Range
    return RANGE


def suggest_weight():
    # category bools
    under = f"Your bmi is [color=ff00FF]{OG_BMI:.2f}[/color], you are underweight. Consider gaining [color=ff00FF]{suggest:.2f}[/color] kg for a bmi of [color=ff00FF]{bmi:.2f}[/color]"
    over = f"Your bmi is [color=ff00FF]{OG_BMI:.2f}[/color], you are in the overweight range. Consider losing [color=ff00FF]{suggest:.2f}[/color] kg for a bmi of [color=ff00FF]{bmi:.2f}[/color]"
    normal = f"Your bmi is [color=ff00FF]{OG_BMI:.2f}[/color], your weight is in the normal range"
    obese = f"Your bmi is [color=ff00FF]{OG_BMI:.2f}[/color], you are in the obese range. Consider losing [color=ff00FF]{suggest:.2f}[/color] kg for a bmi of [color=ff00FF]{bmi:.2f}[/color]"
    
    if OG_BMI < 18.5:
        return under
    
    elif 18.5 <= OG_BMI <= 24.9:
        return normal
    
    elif 25.1 <= OG_BMI <= 29.9:
        return over
    
    elif OG_BMI > 30:
        return obese
    
    else:
        return "error"    
        

def male(h, w):
    global height
    global weight
    global suggest
    global wght_bf
    global OG_BMI
    global Range
    
    height = float(h) / 100
    weight = float(w)
    wght_bf = weight
    calculate(height, weight)
    OG_BMI = bmi
    
    range1 = get_weight(19.1, height)
    range2 = get_weight(27, height)
    Range = f"a healthy weight for a height of [color=ff00FF]{height}[/color] is between [color=ff00FF]{range1:.2f}[/color] and [color=ff00FF]{range2:.2f}[/color]"
    
    while not 19.1 <= bmi <= 27:
        
        while bmi < 19.1:
            weight += .5
            calculate(height, weight)
        
        if bmi > 27:
            weight -= .5
            calculate(height, weight)
            
        else:
            break

    suggest = abs(weight - wght_bf)
    return OG_BMI

        
def female(h, w):
    global height
    global weight
    global suggest
    global wght_bf
    global OG_BMI
    global Range

    height = float(h) / 100
    weight = float(w)
    wght_bf = weight
    calculate(height, weight)
    OG_BMI = bmi

    range1 = get_weight(17.8, height)
    range2 = get_weight(26.5, height)
    Range = f"a healthy weight for a height of [color=ff00FF]{height}[/color] is between [color=ff00FF]{range1:.2f}[/color] and [color=ff00FF]{range2:.2f}[/color]"
    
    while not 17.8 <= bmi <= 26.5:
        while bmi < 17.8:
            weight += .5
            calculate(height, weight)
            
        if bmi > 26.5:
            weight -= .5
            calculate(height, weight)
            
        else:
            break
            
    suggest = abs(weight - wght_bf)
    return OG_BMI