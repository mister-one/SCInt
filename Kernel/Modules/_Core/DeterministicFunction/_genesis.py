import os
import json

folder_path = "/Users/alessandro.rea/Desktop/UnitTesting/Queues/_Core"
# encripted_nonce = 'cjhbkhg§2i476239§672'
# pub_key = 'ouyg2§076§2fgvro§u2b3n§0ry237h-12yrhb'
# verification_nonce = 'calippo'
def iexist():
    pass
def genesis(email, geneis_code_id, secret, public_key,):
    # genesis_certificated_issued_step_0
    geneis_code_id = 1000000000000
    secret = ['word_1', 'word_2', 'word_3']
    first_secret = secret[:1]
    last_secret = secret[:2]
    # genesis_certificated_linked_step_1
    email = 'your_email@scint.io'
    iexist('step_1', email, geneis_code_id, first_secret)

    # you receive an email with the temp code
    temp_code = input("Enter the temporary code received via email at Step 1: ")
    
    # private_node_auth_setup_step_2
    return iexist('step_2', temp_code, last_secret)

'''
# step_1
the private node buys a gensis_card

# step_2 (actual code + email you want to link)
use the iexist method and send to the OpenRegistry the following
- 7362 (initial_id_number)
- email che vuoi legare
- the 1st of the word of the genesis code. 

if the first is correct then you con move to the next step

# step_3 (proof of email)
- full encrypted informations (
    pub_key::: NLKHB58P09ULNL4VKUG3414HFCEYKJHLB
    all encripted
    genesis 3 words
    including the email:: reaslessandro95@gmail.com
    temp_code you receivne to email:: nljwe-123jkd-Mkljn31!

    )
- public key you want to link
'''

    