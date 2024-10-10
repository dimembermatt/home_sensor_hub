# home_sensor_hub
Home sensor hub running off an RPI and supporting several STEMMA-QT compatible I2C sensors.

## Architecture

The RPI is hooked up to several sensors, sampled periodically, and published to a backend database and a frontend dashboard accessible on the local network. A python script pulls the system configuration from `config.json` and instantiates the connection for each sensor. It polls the sensor data at a fixed or interrupt rate, which is sent to a backend database. A frontend server hosts a dashboard which queries the backend database for real time sensor updates.

