import yaml


with open('Config/experiment.yml', 'r') as f:
    data = yaml.load(f)

print(data)
print(data['Scan']['start'])
print(data['Scan']['channel_in'])