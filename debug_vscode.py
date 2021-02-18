import debugpy
import streamlit as st
import coco_explorer
import argparse


if __name__ == "__main__":
    markdown = st.markdown(
        """
    ## Ready to attach the VS Code Debugger!

    ![Python: Remote Attach](https://awesome-streamlit.readthedocs.io/en/latest/_images/vscode_python_remote_attach.png)

    for more info see the [VS Code section at awesome-streamlit.readthedocs.io]
    (https://awesome-streamlit.readthedocs.io/en/latest/vscode.html#integrated-debugging)
    """
    )

    debugpy.listen(5678)
    debugpy.wait_for_client()

    markdown.empty()

    parser = argparse.ArgumentParser()
    parser.add_argument("--coco_train", type=str, default=None)
    parser.add_argument("--coco_predictions", type=str, default=None)
    parser.add_argument("--images_path", type=str, default=None)
    args = parser.parse_args()
    coco_explorer.app(args)

