
import csv
from textblob import TextBlob

import datetime
import random
# import matplotlib.pyplot as plt

# # make up some data
# x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
# y = [i+random.gauss(0,1) for i,_ in enumerate(x)]

# plot
# plt.plot(x,y)
# # beautify the x-labels
# plt.gcf().autofmt_xdate()

# plt.show()


# Each word in the lexicon has scores for:
# 1)     polarity: negative vs. positive    (-1.0 => +1.0)
# 2) subjectivity: objective vs. subjective (+0.0 => +1.0)

infile = './cleaned.csv'

with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    next(rows, None)  # skip the headers


# instantiate dictionaries for respective brand
    bird_count = 0
    bird_dict = {
        "sum_pol": 0,
        "sum_sub": 0,
        "count": 0,
        "avg_pol": 0,
        "avg_sub": 0
    }

    lime_count = 0
    lime_dict = {
        "sum_pol": 0,
        "sum_sub": 0,
        "count": 0,
        "avg_pol": 0,
        "avg_sub": 0
    }

    jump_count = 0
    jump_dict = {
        "sum_pol": 0,
        "sum_sub": 0,
        "count": 0,
        "avg_pol": 0,
        "avg_sub": 0
    }

    # row_count = 0
    for row in rows:
        # print(row)

        id = row[0]
        time = row[1]
        sentence = row[2]

        # just in case
        rt = 1

        try:
            rt = int(row[-4]) + 1

        except:
            rt = 1


        sentence = sentence.upper()
        if 'DEMI' in sentence.upper() or 'LOVATO' in sentence.upper() or 'BRAUN' in sentence.upper() or 'LOVATIC' in sentence.upper():
            # ignore music references
            pass
        else:
            if 'SCOOTER' in sentence.upper():
                blob = TextBlob(sentence)



                # if int(blob.sentiment[0]) != 0:
                #     lime_dict["sum_pol"] += blob.sentiment[0] * rt
                #     lime_dict["sum_sub"] += blob.sentiment[1] * rt
                #     lime_dict["count"] += 1 * rt



                lime_dict["sum_pol"] += blob.sentiment[0] * rt
                lime_dict["sum_sub"] += blob.sentiment[1] * rt
                lime_dict["count"] += 1 * rt
            # if 'LIME' in sentence.upper():
            #     blob = TextBlob(sentence)
            #
            #
            #
            #     # if int(blob.sentiment[0]) != 0:
            #     #     lime_dict["sum_pol"] += blob.sentiment[0] * rt
            #     #     lime_dict["sum_sub"] += blob.sentiment[1] * rt
            #     #     lime_dict["count"] += 1 * rt
            #
            #
            #
            #     lime_dict["sum_pol"] += blob.sentiment[0] * rt
            #     lime_dict["sum_sub"] += blob.sentiment[1] * rt
            #     lime_dict["count"] += 1 * rt
            #
            #
            #
            # elif 'BIRD' in sentence.upper():
            #     blob = TextBlob(sentence)
            #
            #
            #
            #     # if int(blob.sentiment[0]) != 0:
            #     #     bird_dict["sum_pol"] += blob.sentiment[0] * rt
            #     #     bird_dict["sum_sub"] += blob.sentiment[1] * rt
            #     #     bird_dict["count"] += 1 * rt
            #
            #
            #
            #     bird_dict["sum_pol"] += blob.sentiment[0] * rt
            #     bird_dict["sum_sub"] += blob.sentiment[1] * rt
            #     bird_dict["count"] += 1 * rt
            #
            #
            #
            # elif 'JUMP' in sentence.upper():
            #     blob = TextBlob(sentence)
            #
            #
            #
            #     # if int(blob.sentiment[0]) != 0:
            #     #     jump_dict["sum_pol"] += blob.sentiment[0] * rt
            #     #     jump_dict["sum_sub"] += blob.sentiment[1] * rt
            #     #     jump_dict["count"] += 1 * rt
            #
            #     jump_dict["sum_pol"] += blob.sentiment[0] * rt
            #     jump_dict["sum_sub"] += blob.sentiment[1] * rt
            #     jump_dict["count"] += 1 * rt
            #
            #
            #
            else:
                pass

    lime_dict["avg_pol"] = lime_dict["sum_pol"] / lime_dict["count"]
    lime_dict["avg_sub"] = lime_dict["sum_sub"] / lime_dict["count"]

    # bird_dict["avg_pol"] = bird_dict["sum_pol"] / bird_dict["count"]
    # bird_dict["avg_sub"] = bird_dict["sum_sub"] / bird_dict["count"]
    #
    # jump_dict["avg_pol"] = jump_dict["sum_pol"] / jump_dict["count"]
    # jump_dict["avg_sub"] = jump_dict["sum_sub"] / jump_dict["count"]


    print("LIME POL: " + str(lime_dict["avg_pol"]))
    print("BIRD POL: " + str(bird_dict["avg_pol"]))
    print("JUMP POL: " + str(jump_dict["avg_pol"]))
    # print("")
    # print("LIME SUB: " + str(lime_dict["avg_sub"]))
    # print("BIRD SUB: " + str(bird_dict["avg_sub"]))
    # print("JUMP SUB: " + str(jump_dict["avg_sub"]))
    print("")
    print("LIME: " + str(lime_dict))
    print("BIRD: " + str(bird_dict))
    print("JUMP: " + str(jump_dict))