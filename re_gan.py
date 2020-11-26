import re
html = """
<div><p>我命由我不由天</p></div>
<div><p>AID2008,开干~~~</p></div>
"""

pattrn = re.compile('<div><p>(.*?)</p></div>',re.S)
r_list = pattrn.findall(html)
print(r_list)

