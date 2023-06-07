def main(*r):
    s = ({'MUF', 'XBASE', 2000},
         {'MUF', 'XBASE', 2013, 'ASP'},
         {'MUF', 'XBASE', 2013, 'MUPAD'},
         {'MUF', 'XBASE', 1987, 'HY'},
         {'MUF', 'XBASE', 1987, 'PAN'},
         {'MUF', 'SQL', 'HY', 'ASP'},
         {'MUF', 'SQL', 'HY', 'MUPAD'},
         {'MUF', 'SQL', 'PAN', 2000},
         {'MUF', 'SQL', 'PAN', 2013},
         {'MUF', 'SQL', 'PAN', 1987},
         {'PERL6'})
    s1 = set(*r)
    return [i for i in range(len(s))
            if not(len(s[i] - s1))][0]


print(main(['MUF', 'ASP', 'XBASE', 2013, 'PAN']))
