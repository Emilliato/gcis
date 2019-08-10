with open('requirements1.txt', encoding='utf-16') as old, open('requirements.txt', 'w', encoding='utf-8') as new:
    new.write(old.read())
