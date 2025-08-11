import yaml
from pprint import pp
from automatedorgcharts import Organization
from automatedorgcharts.visualisation import visualize_org_chart

mdccd = Organization()

with open("data/raw/data.yaml", "r") as file:
    actions = yaml.safe_load_all(file)
    for action in actions:
        mdccd.process_action(action)

pp(mdccd.positions)
pp(mdccd.employees)

visualize_org_chart(mdccd)
