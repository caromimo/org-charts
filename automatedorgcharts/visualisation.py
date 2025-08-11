
import gviz_api

def visualize_org_chart(organization):
    # Create a data table
    description = {"position": ("string", "Position"), "manager": ("string", "Manager"), "tooltip": ("string", "Tooltip")}
    data = []
    for position_number, position_details in organization.positions.items():
        incumbent_label = "VACANT"
        if "incumbent" in position_details and position_details["incumbent"] in organization.employees:
            employee = organization.employees[position_details["incumbent"]]
            incumbent_label = f'{employee["firstName"]} {employee["lastName"]}'

        tooltip = f'{position_details["title"]}\n{position_details["classification"]}'
        
        # The node format is:
        # [{'v': 'unique_id', 'f': 'display_html'}, 'reporting_to_id', 'tooltip']
        node = {
            "position": (str(position_number), f'{position_number}<div style="color:red; font-style:italic">{incumbent_label}</div>'),
            "manager": str(position_details.get("reportsTo", "")),
            "tooltip": tooltip
        }
        data.append(node)

    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Create the JSON representation of the data table
    json_data = data_table.ToJSon(columns_order=("position", "manager", "tooltip"), order_by="position")

    # Create the HTML file
    html = f'''
    <html>
      <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
          google.charts.load('current', {{'packages':['orgchart']}});
          google.charts.setOnLoadCallback(drawChart);

          function drawChart() {{
            var data = new google.visualization.DataTable({json_data});

            var chart = new google.visualization.OrgChart(document.getElementById('chart_div'));
            chart.draw(data, {{'allowHtml':true, 'size': 'large', 'allowCollapse': true}});
          }}
        </script>
      </head>
      <body>
        <div id="chart_div"></div>
      </body>
    </html>
    '''

    with open("org_chart.html", "w") as f:
        f.write(html)
    
    print("Org chart has been generated in org_chart.html")
