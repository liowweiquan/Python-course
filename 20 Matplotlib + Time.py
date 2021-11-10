import matplotlib.pyplot as pyplot
import time as t

times = []
mistakes = 0

print ("This program will help you type faster. You will have to type 'love' as fast as you can for five times")
input ("Press enter to start: ")

while len(times) <5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != "love"):
        mistakes += 1


print ("You made " + str(mistakes) + " mistakes.")
print ("Let's see your time spent.")
t.sleep(3)

x = [1,2,3,4,5]
y = times

pyplot.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
pyplot.xticks(x, legend)
pyplot.ylabel("times in seconds")
pyplot.xlabel("number of attempts")
pyplot.title ("Yout typing times")


pyplot.show()
