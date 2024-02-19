import os
import json
from google.cloud import bigquery


def _post(location, data, tag_1, tag_2, tag_3, tag_n):
    # Create a BigQuery client
    client = bigquery.Client.from_service_account_info(json.loads(os.environ['open_registry_auth_key']))
    query_job = client.query(
    f'''
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
            '{location}', -- location STRING
            JSON '{json.dumps(data)}', -- data JSON
            '{tag_1}',-- tag_1 STRING
            '{tag_2}',-- tag_2 STRING
            '{tag_3}',-- tag_3 STRING
            '{tag_n}'-- tag_n STRING
        )        
    '''
    )

    return query_job.result()



location = "London"
data = {"company": "Onsi", "type": "b2b"}
tag_1 = "tag1"
tag_2 = "tag2"
tag_3 = "tag3"
tag_n = "tagN"


_post(location, data, tag_1, tag_2, tag_3, tag_n)
