import re
for _ in range(int(input())):
    ans =''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}',ans)
        assert re.search(r'[\d\d\d]',ans)
        assert not re.search(r'[^a-zA-Z0-9]', ans)
        assert not re.search(r'(.)\1', ans)
        assert len(ans) == 10
    except:
        print('INVAlid')
    else:
        print("Valid")

