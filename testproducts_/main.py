import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database connection URL
db_url = "postgresql://username:password@localhost:port/database"  # edit your own database connection string

# Create SQLAlchemy engine
engine = create_engine(db_url)

# Example: Read a table named 'cars' into a DataFrame
try:
    df = pd.read_sql("SELECT * FROM testproducts", engine)
    print(df.head())

    # Optional: Plotting if 'product_name' and 'category_id' columns exist
    if 'product_name' in df.columns and 'category_id' in df.columns:
        plt.figure(figsize=(25, 6))
        plt.bar (df['product_name'], df['category_id'])
        plt.xlabel('product Name')
        plt.ylabel('category ID')
        plt.title('test products by Category')
        plt.tight_layout()
        plt.grid(True, axis='y')
        plt.show()
    else:
        print("CRequired columns not found.")
except Exception as e:
    print("Error:", e)
