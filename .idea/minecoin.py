import reverse
import json

def construct_minecoin_challenge(str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reseverd, str_time_reversed, str_nbits_reversed, str_nonce_reversed, str_soln_reversed):
    return str_version_reversed + str_prev_hash_reversed + str_merkle_root_reversed + str_reseverd + str_time_reversed + str_nbits_reversed + str_nonce_reversed + str_soln_reversed

#{
#  "hash": "0000000006613599275ab99638a1537244983f4ae4ee5e14585d4af9feef387f", "confirmations": 4109, "height": 193911,  "version": 536870912,  "versionHex": "20000000",  "merkleroot": "8af3b5d6b0f4c80160603315246911c0051c39ef764dead150eacc403005dbbd",  "time": 1536348098,  "mediantime": 1536347418,  "nonce": "21579eb500000000000000000000000000000000000000000000000603b99048",
#  "bits": "1c444666",  "difficulty": 3.749485413914944,  "chainwork": "000000000000000000000000000000000000000000000000000922b2af6b0708",  "previousblockhash": "000000000952a2066772826ca5de0bcfef2266377a07a95e5dd9393130d1494c",  "nextblockhash": "0000000015a2adef0ea36a53a51a2b84898162adb8512e17e71df2aa511206fd"
#}

def get_parameter_from_block_data(block_json_str):
    block_json = json.loads(block_json_str)
    str_version_reversed = block_json[0]['versionHex']
    str_prev_hash_reversed = reverse.reverse(block_json[0]['previousblockhash'])
    str_merkle_root_reversed = block_json[0]['merkleroot']
    str_reserved = '0000000000000000000000000000000000000000000000000000000000000000'
    str_time_reversed = reverse.reverse(hex(block_json[0]['time'])[2:])
    str_nbits_reversed = reverse.reverse(block_json[0]['bits'])
    str_nonce_reversed = reverse.reverse(block_json[0]['nonce'])
    str_soln_reversed = block_json[0]['solution']
    return str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved, str_time_reversed, \
           str_nbits_reversed, str_nonce_reversed, str_soln_reversed


if __name__ == '__main__':
    block_json_str = '["hash": "0000000006613599275ab99638a1537244983f4ae4ee5e14585d4af9feef387f", "confirmations": 4109, "height": 193911,  "version": 536870912,  "versionHex": "20000000",  "merkleroot": "8af3b5d6b0f4c80160603315246911c0051c39ef764dead150eacc403005dbbd",  "time": 1536348098,  "mediantime": 1536347418,  "nonce": "21579eb500000000000000000000000000000000000000000000000603b99048","bits": "1c444666",  "difficulty": 3.749485413914944,  "chainwork": "000000000000000000000000000000000000000000000000000922b2af6b0708",  "previousblockhash": "000000000952a2066772826ca5de0bcfef2266377a07a95e5dd9393130d1494c",  "nextblockhash": "0000000015a2adef0ea36a53a51a2b84898162adb8512e17e71df2aa511206fd"]'
    str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved, str_time_reversed, \
        str_nbits_reversed, str_nonce_reversed, str_soln_reversed = get_parameter_from_block_data(block_json_str)
    print(construct_minecoin_challenge(str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved,
                                  str_time_reversed, str_nbits_reversed, str_nonce_reversed, str_soln_reversed))


