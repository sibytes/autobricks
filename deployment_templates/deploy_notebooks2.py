import os
from autobricks import Workspace

ROOT_DIR = os.getenv("ROOT_DIR")
WORKSPACE_ROOT = os.getenv("WORKSPACE_ROOT")
WORKSPACE_SUBDIRS:str = os.getenv("WORKSPACE_SUBDIRS", None)

from_notebook_root = f"{ROOT_DIR}test/artefacts/notebooks"
target_dir = f"/{WORKSPACE_ROOT}/"

if WORKSPACE_SUBDIRS:
    sub_folders = [d.strip() for d in WORKSPACE_SUBDIRS.split(",")]

    for f in sub_folders:

        source_dir = f"/{f}"
        Workspace.workspace_import_dir(
            from_notebook_root=from_notebook_root,
            source_dir=source_dir,
            target_dir=target_dir,
            deploy_mode=Workspace.DeployMode.PARENT
        )
else:

    Workspace.workspace_import_dir(
        from_notebook_root=from_notebook_root,
        # source_dir=source_dir,
        target_dir=target_dir,
        deploy_mode=Workspace.DeployMode.PARENT
    )