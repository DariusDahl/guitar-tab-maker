import streamlit.web.cli as stcli
import sys

sys.argv = ["streamlit", "run", "src/tab_writer_app.py"]
sys.exit(stcli.main())