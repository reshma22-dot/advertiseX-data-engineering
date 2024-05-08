import sys
from os.path import dirname, abspath

# Add the directory containing dataingestion.py and dataprocessing.py to the PYTHONPATH
sys.path.append(dirname(dirname(abspath('C:\Data Engineering Case Study'))))

# Importing functions from dataingestion.py and dataprocessing.py
from dataingestion import ingest_json_data, ingest_csv_data, ingest_other_data
from dataprocessing import transform_data, validate_data, filter_data, deduplicate_data, correlate_data

class DataStorage:
    def __init__(self):
        self.data_store = {}

    def store_data(self, data):
        # Store processed data efficiently
        # For simplicity, using a dictionary as an in-memory storage
        # Replace this with an appropriate data storage solution (e.g., database, data warehouse)
        for record in data:
            key = record['campaign_id']  # Assuming each record has a campaign ID
            if key not in self.data_store:
                self.data_store[key] = []
            self.data_store[key].append(record)

    def query_performance(self, campaign_id):
        # Retrieve campaign performance data efficiently
        # For simplicity, directly querying the in-memory data store
        # Replace this with optimized querying for your chosen data storage solution
        if campaign_id in self.data_store:
            return self.data_store[campaign_id]
        else:
            return []

# Example usage for testing purposes
if __name__ == "__main__":
    # Example data
    ad_impressions = [
        {"ad_id": 1, "user_id": 101, "timestamp": "2024-05-08T12:00:00Z"},
        {"ad_id": 2, "user_id": 102, "timestamp": "2024-05-08T12:05:00Z"}
    ]
    clicks = [
        {"ad_id": 1, "user_id": 101, "timestamp": "2024-05-08T12:02:00Z"},
        {"ad_id": 2, "user_id": 102, "timestamp": "2024-05-08T12:06:00Z"}
    ]
    conversions = [
        {"ad_id": 1, "user_id": 101, "conversion_type": "purchase", "timestamp": "2024-05-08T12:10:00Z"}
    ]

    # Data processing
    transformed_data = [transform_data(data) for data in ad_impressions + clicks + conversions]
    validated_data = [data for data in transformed_data if validate_data(data)]
    filtered_data = filter_data(validated_data)
    deduplicated_data = deduplicate_data(filtered_data)
    correlated_data = correlate_data(ad_impressions, clicks, conversions)

    # Store processed data
    storage = DataStorage()
    storage.store_data(deduplicated_data)

    # Query performance for a specific campaign
    campaign_id = 1
    campaign_performance = storage.query_performance(campaign_id)
    print("Campaign Performance for Campaign ID {}: {}".format(campaign_id, campaign_performance))

