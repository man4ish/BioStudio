import scanpy as sc

# Load the file
adata = sc.read_h5ad('test_data.h5ad')

# Print general info
print(adata)

# Print gene names (stored in .var_names)
print("Gene names:")
print(adata.var_names)

# Print first 10 gene names
print("First 10 genes:", list(adata.var_names)[:10])

# Print cell/sample names (stored in .obs_names)
print("Cell/sample names:")
print(adata.obs_names)

# Optional: print obs metadata columns
print("Metadata columns:")
print(adata.obs.columns)
