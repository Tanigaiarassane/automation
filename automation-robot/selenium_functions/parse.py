import yaml
with open("find_element.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

ret_val = cfg['find_by']
print type(ret_val)
print ret_val
