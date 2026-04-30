fn = open('Test.txt', 'r')
fn1 = open('text.txt', 'w')
content = fn.readlines()
type(content)
for i in range(1 , len(content) + 1):
    if (i % 2 != 0):
        fn1.write(content[i-1])
    else:
        pass
fn1.close()
fn1 = open('text.txt', 'r')
content1 = fn1.read()
print(content1)
fn1.close()
fn.close()