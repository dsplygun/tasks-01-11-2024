menu = {'Pancake':4,
    'Pasta':8,
    'Coffee':3,
}

import json
to_write = json.dumps(menu,indent=2)
with open('menu.txt','w') as f:
    f.write(to_write)
    f.close()