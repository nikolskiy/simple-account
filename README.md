# Customer Account

## Install and run using docker-compose
1) `pip install docker-compose` (working Docker is required)
2) `docker-compose up --build`

## Endpoints
1) Methods: GET, POST. URL: http://127.0.0.1/api/customers/ - create new customer records
2) Methods: GET, UPDATE, DELETE. URL: http://127.0.0.1/api/customers/uuid/ - update or delete existing customer records (replace `uuid` with existing uuid)
3) Methods: POST. URL: http://127.0.0.1/api/add/ - Adds funds to existing customer
4) Methods: POST. URL: http://127.0.0.1/api/subtract/ - Places `hold` on a customer account
5) Methods: POST. URL: http://127.0.0.1/api/status/ -  Shows customer account status
6) Methods: GET. URL: http://127.0.0.1/api/ping/ - Service heartbeat 
