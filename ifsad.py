def stay_motivated(emotion):
    if emotion.lower() in ["upset", "frustrated", "sad", "angry"]:
        print("It's okay to feel upset or frustrated, but remember your goal!")
        print("Take a deep breath and keep moving forward.")
    else:
        print("You're doing great! Keep up the good work and stay focused on your goal.")

your_emotion = input("How are you feeling? ")

stay_motivated(your_emotion)
