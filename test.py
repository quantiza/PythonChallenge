import re
import sys

s = 'klsdf122jh->>lsd122fj->>lak231sjfl->>k345ajsjjs'

print(re.findall(r'\d{3}', s))
print(sys.version)
print(sys.version_info)