with open('requirements.txt', encoding='utf-16') as old, open('requirements1.txt', 'w', encoding='utf-8') as new:
    new.write(old.read())
