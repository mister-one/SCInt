import os
import json
from google.cloud import bigquery


class OpenRegistryConnector:

    def __init__(self) -> None:
        self.client = bigquery.Client.from_service_account_info(json.loads(os.environ['open_registry_auth_key']))

    def post(self, location=(-3.2765753, 54.7023545), data={}, 
                tag_1=None, tag_2=None, tag_3=None, tag_n=None):
        longitude, latitude = location
        query = f'''
            INSERT INTO `cb-data-dev.opre.uk_post` (
                post_id,
                source,
                created_at_tstamp,
                expires_at_tstamp,
                location,
                data,
                tag_1,
                tag_2,
                tag_3,
                tag_n
            )
            VALUES
            (
                DEFAULT, -- post_id, 
                DEFAULT, -- source
                DEFAULT, -- created_at_tstamp
                NULL, -- expires_at_tstamp
                ST_GeogPoint({longitude}, {latitude}), -- location GEOGRAPHY (longitude, latitude)
                JSON '{json.dumps(data)}', -- data JSON
                { f"'{tag_1}'" if tag_1 else 'NULL' }, -- tag_1 STRING
                { f"'{tag_2}'" if tag_2 else 'NULL' }, -- tag_2 STRING
                { f"'{tag_3}'" if tag_3 else 'NULL' }, -- tag_3 STRING
                { f"'{tag_n}'" if tag_n else 'NULL' } -- tag_n STRING
            )        
        '''
        query_job = self.client.query(query)

        if query_job.errors:
        # Handle errors
            for error in query_job.errors:
                print(f"Error: {error['message']}")
        else:
            print("Insertion successful!")

        return query_job.result()
    
    def generate_truth_certificate(self, encription_pub_key, statement_type, statement, supporting_evidence=None, encription_verification_type=None):
        query = f'''
            INSERT INTO `cb-data-dev.opre.uk_t0_certify_request_queue` (
                certify_request_id, 
                `source`, 
                created_at_tstamp, 
                request_expires_at_tstamp, 
                encription_pub_key, 
                encription_verification_type,
                statement_type, 
                statement, 
                supporting_evidence 
            )
            VALUES
            (
                DEFAULT, -- certify_request_id, 
                DEFAULT, -- source
                DEFAULT, -- created_at_tstamp
                NULL, -- request_expires_at_tstamp
                '{encription_pub_key}', -- encription_pub_key STRING
                { f"'{encription_verification_type}'" if encription_verification_type else 'DEFAULT' }, -- encription_verification_type STRING
                { f"'{statement_type}'" if statement_type else 'DEFAULT' }, -- statement_type STRING
                JSON '{json.dumps(statement)}', -- statement JSON
                { f"JSON '{json.dumps(supporting_evidence)}'" if supporting_evidence else 'NULL' } -- supporting_evidence JSON
            )        
        '''
        query_job = self.client.query(query)
        if query_job.errors:
        # Handle errors
            for error in query_job.errors:
                print(f"Error: {error['message']}")
        else:
            print("Insertion successful!")
        return query_job.result()




_or = OpenRegistryConnector()

_or.post()

public_key_bytes = b"-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwhbQFTR+J7Rp6yoyCQ2EOSyyv0wgKaGCagdb/J3NaTnXSxWbxdOVHxhAkkReQR268yeta0WQ4o8Fui2mFe7oqaft0ogYOEYUii/J64A64YHJDt44uwhlqQLvxi5MXZbRLltmBgzHj105o962eWOTcze3XCovjOn4qSp0pT5y5FVTo2XQxWFNvqt/+MTcVT0yRxo8uiJw/Zz5vRhrmb+otuX8a1tzq4g6IXmhDUQIO1LbOkaVkUJXfhsKlC4BMF4vr3d4j8tfEoVPkqHBVuF/S0MTgXVHAUu6bU3hR5GpbFJSwCnxDeHA6KP9eYQtQvXFzB+7yeCG3r+6fch3kQeS2QIDAQAB-----END PUBLIC KEY-----"
a =  public_key_bytes.decode('utf-8')
encription_pub_key = a.replace("'", "''")

_or.generate_truth_certificate(a,2,3)

if __name__ == '__main__':
    pass


