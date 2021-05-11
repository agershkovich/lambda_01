import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def bmi(event, context):
    logger.info("Request: %s", event)

    # getting input from the user and assigning it to user

    height = float(event["body"]["height"])
    weight = float(event["body"]["weight"])
    logger.info("height: %s", height)
    logger.info("weight: %s", weight)

    # the formula for calculating bmi
    bmi = weight / (height ** 2)

    # conditions
    if (bmi < 16):
        decribe = "severely underweight"

    elif (bmi >= 16 and bmi < 18.5):
        decribe = "underweight"

    elif (bmi >= 18.5 and bmi < 25):
        decribe = "Healthy"

    elif (bmi >= 25 and bmi < 30):
        decribe = "overweight"

    elif (bmi >= 30):
        decribe = "severely overweight"

    result = ("Your BMI is " + str(int(bmi)) + " and you are " + decribe)
    # response = {'result': result}
    response = {
        "body": result
    }

    return response
