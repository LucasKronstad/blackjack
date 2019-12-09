questions = [ ("What country is padel most popular in? 1. Spain, 2. USA, 3. Sweden ", "1", "One", "one"),
              ("What sport is padel most similar to? ", "Tennis", "tennis", "tennis"), 
              ("The score system in padel is the same as tennis, how many points is the first ball? ", "15", "Fifteen", "fifteen"),
              ("Which of the following is not the name of a shot? A. Smash, B. Slice, C. Spin ", "c", "C", "C"),
              ("Generally, how many players are on the court? ", "four", "Four", "4")
]

score = 0
for q in questions:
    print()
    ans = input(q[0])
    if ans == (q[1]) or ans == (q[2]) or ans == (q[3]):
        print("Good job")
        score += 1
    else:
        print("Wrong")

print()  
print("You got", score, "questions right")
print("That's", int(score*100/len(questions)), "percent correct")