from textblob import TextBlob
import matplotlib.pyplot as plt

def opinion(x, positive_count, negative_count, neutral_count):
    if x > 0.1:
        print("Generally Positive")
        positive_count += 1
    elif x < -0.1:
        print("Generally Negative")
        negative_count += 1
    else:
        print("Neutral")
        neutral_count += 1
    return positive_count, negative_count, neutral_count

with open('text.txt', 'r') as file:
    opinions = file.readlines()

positive_count = 0
negative_count = 0
neutral_count = 0

for idx in opinions:
    blob = TextBlob(idx)
    sentyment = blob.sentiment

    print("Tekst: ", idx)
    print("Polarity:", sentyment.polarity)
    positive_count, negative_count, neutral_count = opinion(sentyment.polarity, positive_count, negative_count, neutral_count)
    print('======================================')

print("Positive opinions:", positive_count)
print("Negative opinions:", negative_count)
print("Neutral opinions:", neutral_count)

labels = ['Positive', 'Negative', 'Neutral']
counts = [positive_count, negative_count, neutral_count]

plt.figure(figsize=(8, 6))
plt.bar(labels, counts, color=['green', 'red', 'gray'])
plt.xlabel('Opinion')
plt.ylabel('Count')
plt.title('Opinions Analysis')
plt.show()
