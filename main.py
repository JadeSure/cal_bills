from datetime import datetime

# modify those variables
has_electricity = True
has_water = True
has_network = True
has_gas = False

bills_dict = {
    "electricity": {
        "status": has_electricity,
        "start_date": "2024-07-03",
        "end_date": "2024-08-31",
        "cost": 448.28
    }, "water": {
        "status": has_water,
        "start_date": "2024-05-27",
        "end_date": "2024-07-24",
        "cost": 78.12
    }, "gas": {
        "status": has_gas,
        "start_date": "2024-09-01",
        "end_date": "2024-09-03",
        "cost": 100
    }, "network": {
        "status": has_network,
        "start_date": "2024-08-01",
        "end_date": "2024-08-31",
        "cost": 85
    }
}

tenants_list = [
    {
        "name": "Teresa",
        "start_date": "2024-07-20",
        "end_date": "2024-08-31",
        "exclude_bills": ["network", "water"]
    }, {
        "name": "Saifeng",
        "start_date": "2024-07-17",
        "end_date": "2024-08-31",
        "exclude_bills": []
    }, {
        "name": "Jiaqi",
        "start_date": "2024-07-03",
        "end_date": "2024-08-31",
        "exclude_bills": []
    },{
        "name": "Shawn",
        "start_date": "2024-08-01",
        "end_date": "2024-08-31",
        "exclude_bills": []
    }
]

def calculate_days(start_date, end_date):
    date_format = "%Y-%m-%d"
    start_date_obj = datetime.strptime(start_date, date_format)
    end_date_obj = datetime.strptime(end_date, date_format)
    delta = end_date_obj - start_date_obj
    return delta.days + 1

class billsBuilder:
    def __init__(self, category, start_date, end_date, cost):
        self.start_date = start_date
        self.end_date = end_date
        self.cost = cost
        self.days = calculate_days(start_date, end_date)
        self.category = category

    def get_daily_cost(self):
        return self.cost / self.days
    

    def __str__(self):
        output = f"{self.category.capitalize()} cost ${self.cost} within {self.days} days on average is: ${round(self.get_daily_cost(), 2)} between {self.start_date} and {self.end_date}"
        return output


bills_daily_cost = {}
number_of_tenants = len(tenants_list)
for category, bill in bills_dict.items():
    if bill["status"]:
        bill_obj = billsBuilder(category, bill["start_date"], bill["end_date"], bill["cost"])
        daily_cost = bill_obj.get_daily_cost()
        bills_daily_cost[category] = daily_cost
        print(bill_obj)

print("====== Your Bills ======")

for tenant in tenants_list:
    tenant_name = tenant["name"]
    tenant_start_date = tenant["start_date"]
    tenant_end_date = tenant["end_date"]
    tenant_exclude_bills = tenant["exclude_bills"]
    tenant_days = calculate_days(tenant_start_date, tenant_end_date)
    tenant_total_cost = 0

    for category, daily_cost in bills_daily_cost.items():
        if category not in tenant_exclude_bills:
            tenant_total_cost += daily_cost / number_of_tenants * tenant_days

    print(f"{tenant_name} needs to pay ${round(tenant_total_cost, 2)} from {tenant_start_date} to {tenant_end_date}, totally: {tenant_days} days")


