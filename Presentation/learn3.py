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

tekst = "It's a really good product! I wish every scarf was that comfy!"
tekst2 = "I've never bought such a bad scarf, it's very itchy"
tekst3 = "Pretty nice product, really comfy and really warm"
tekst4 = "Terrible!"
tekst5 = "Best product!"
tekst6 = "Scarf is really cozy, nice coloring"
tekst7 = "Worthy buying"
tekst8 = "I don't know..."
tekst9 = "Awesome, but not very various in coloring"
tekst10 = "It was worth the wait"

opinions = [tekst, tekst2, tekst3, tekst4, tekst5, tekst6, tekst7, tekst8, tekst9, tekst10]

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
