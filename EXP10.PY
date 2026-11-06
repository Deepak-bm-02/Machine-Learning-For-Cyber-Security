import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Dataset columns
cols = [
'duration','protocol_type','service','flag','src_bytes',
'dst_bytes','land','wrong_fragment','urgent','hot',
'num_failed_logins','logged_in','num_compromised',
'root_shell','su_attempted','num_root','num_file_creations',
'num_shells','num_access_files','num_outbound_cmds',
'is_host_login','is_guest_login','count','srv_count',
'serror_rate','srv_serror_rate','rerror_rate',
'srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
'dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate',
'label','difficulty'
]

# Load dataset
data = pd.read_csv(
    r"F:\MLCS\10th dataset\KDDTrain+.txt",
    names=cols
)

print("Dataset loaded:", data.shape)

# Select numerical features
X = data.select_dtypes(include='number')

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering
model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

data['cluster'] = model.fit_predict(X_scaled)

# Identify normal cluster using original labels
normal_cluster = data.groupby('cluster')['label'].apply(
    lambda x: (x == 'normal').mean()
).idxmax()

# Classify network events
data['status'] = data['cluster'].apply(
    lambda x: 'Normal' if x == normal_cluster else 'Abnormal'
)

print("\nNetwork Anomaly Detection:")
print(data[['label', 'cluster', 'status']].head(10))