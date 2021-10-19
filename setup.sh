mkdir -p ~/.streamlit/
echo "
[general]n
email = "mhamid161275@bscse.uiu.ac.bd"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml
