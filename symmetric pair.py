d = {'1':'3','2':'6','3':'5','7':'4','5':'3','8':'7'}

pairs = [(key, value) for key, value in d.items()]

answer = [(x, y) for (x, y) in pairs if (y, x) in pairs]

print(answer)