import os, sys


os.environ["DATABRICKS_API_HOST"] = sys.argv[1]
os.environ["DBUTILSTOKEN"] = sys.argv[2]
print(os.getcwd())

from autobricks import Dbfs


filename = "autobricks-*-py3-none-any.whl"
build_dir = sys.argv[3]
deploy_dir = sys.argv[4] 

wheels = Dbfs.find_file('*.whl', build_dir)

for whl in wheels:

    whl_filename = os.path.basename(whl)

    print(f"{whl} => {deploy_dir}/{whl_filename}")
    Dbfs.dbfs_upload(whl, f"{deploy_dir}/{whl_filename}", True)