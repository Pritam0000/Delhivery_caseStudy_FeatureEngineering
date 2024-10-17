import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_process_data():
    # Load the data
    df = pd.read_csv("delhivery.csv")

    # Data cleaning and processing
    df["location_level_grouping"] = df["trip_uuid"] + df["source_center"] + df["destination_center"]
    df = df.drop(["is_cutoff", "cutoff_factor", "cutoff_timestamp", "factor", "segment_factor"], axis=1)

    # Convert timestamps to datetime
    df['od_start_time'] = pd.to_datetime(df['od_start_time'])
    df['od_end_time'] = pd.to_datetime(df['od_end_time'])

    # Calculate total duration
    df["od_total_duration_by_hour"] = (df["od_end_time"] - df["od_start_time"]).dt.total_seconds() / 3600

    # Group by trip_uuid
    df = df.groupby("trip_uuid").agg({
        "data": "first",
        'trip_creation_time': "first",
        'route_schedule_uuid': "first",
        'route_type': "first",
        'source_center': "first",
        'source_name': "first",
        'destination_center': "last",
        'destination_name': "last",
        'od_total_duration_by_hour': "sum",
        'start_scan_to_end_scan': "sum",
        'actual_distance_to_destination': "sum",
        'actual_time': "sum",
        'osrm_time': "sum",
        'osrm_distance': "sum",
        'segment_actual_time': "sum",
        'segment_osrm_time': "sum",
        'segment_osrm_distance': "sum",
    }).reset_index()

    # Extract date components
    df["trip_creation_time"] = pd.to_datetime(df["trip_creation_time"])
    df["year"] = df["trip_creation_time"].dt.year
    df["month"] = df["trip_creation_time"].dt.month
    df["day"] = df["trip_creation_time"].dt.day

    # Extract state and city
    df[["city", "state"]] = df["destination_name"].str.extract(r'(.+?)\s*\((.+?)\)')
    df["city"] = df["city"].str.split("_").str[0]

    # Clean city names
    city_mapping = {
        "Bangalore": "Bengaluru",
        "PNQ Rahatani DPC": "Pune",
        "PNQ Vadgaon Sheri DPC": "Pune",
        "PNQ Pashan DPC": "Pune",
        "Pune Balaji Nagar": "Pune",
        "HBR Layout PC": "Bengaluru",
        "Bhopal MP Nagar": "Bhopal",
        "Mumbai Antop Hill": "Mumbai"
    }
    df["city"] = df["city"].replace(city_mapping)

    # Drop unnecessary columns
    df = df.drop(["trip_creation_time", "destination_name"], axis=1)

    # Calculate delay
    df["delay"] = df["osrm_time"] - df["actual_time"]

    # Encode route_type
    label_encoder = LabelEncoder()
    df["route_type"] = label_encoder.fit_transform(df["route_type"])

    return df