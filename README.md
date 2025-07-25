# sqlserver-dlthub
# Add Microsoft repository
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc

# Add the repository (replace with your Ubuntu version if different)
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Update package list
sudo apt-get update

# Install the ODBC driver
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Install unixODBC development headers (if needed)
sudo apt-get install -y unixodbc-dev