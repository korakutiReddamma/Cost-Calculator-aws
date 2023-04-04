import sqlite3

mock_data = {
    "current_month_cost": 150.00,
    "forecasted_month_end_cost": 200.00,
    "last_month_cost": 100.00,
    "top_costs_current_month": [
        {"service": "EC2", "cost": 50.00},
        {"service": "S3", "cost": 30.00},
        {"service": "RDS", "cost": 20.00}
    ]
}

conn = sqlite3.connect('database_name.db')

conn.execute('''CREATE TABLE mock_data
                (current_month_cost REAL,
                 forecasted_month_end_cost REAL,
                 last_month_cost REAL,
                 top_cost_service_1 TEXT,
                 top_cost_service_1_cost REAL,
                 top_cost_service_2 TEXT,
                 top_cost_service_2_cost REAL,
                 top_cost_service_3 TEXT,
                 top_cost_service_3_cost REAL);''')


conn.execute('''INSERT INTO mock_data (current_month_cost, forecasted_month_end_cost, last_month_cost, top_cost_service_1, top_cost_service_1_cost, top_cost_service_2, top_cost_service_2_cost, top_cost_service_3, top_cost_service_3_cost)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
             (mock_data['current_month_cost'], mock_data['forecasted_month_end_cost'], mock_data['last_month_cost'], mock_data['top_costs_current_month'][0]['service'], mock_data['top_costs_current_month'][0]['cost'], mock_data['top_costs_current_month'][1]['service'], mock_data['top_costs_current_month'][1]['cost'], mock_data['top_costs_current_month'][2]['service'], mock_data['top_costs_current_month'][2]['cost']))
                
conn.commit()
conn.close()
                