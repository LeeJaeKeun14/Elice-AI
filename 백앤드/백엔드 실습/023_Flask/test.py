#%%
import json
from os import lseek

t1 = json.loads('{"title":"react","body":"react is .."}')

# %%
print(t1)
# %%
print(type(t1))
# %%
obj = [{"title":"react","body":"react is .."}]
js = json.dumps(obj)
# %%
type(js)
# %%
ld = json.loads(js)
# %%
type(ld)
# %%
