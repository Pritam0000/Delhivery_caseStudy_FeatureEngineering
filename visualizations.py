import matplotlib.pyplot as plt
import seaborn as sns

def plot_state_delivery_counts(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    df["state"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Delivery Counts by State")
    ax.set_xlabel("State")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig

def plot_monthly_delivery_counts(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("month")["trip_uuid"].count().plot(kind="bar", ax=ax)
    ax.set_title("Monthly Delivery Counts")
    ax.set_xlabel("Month")
    ax.set_ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    return fig

def plot_route_type_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 8))
    df["route_type"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_title("Route Type Distribution")
    plt.tight_layout()
    return fig