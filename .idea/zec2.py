import reverse
import json
import hashlib

def construct_zec_challenge(str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reseverd, str_time_reversed, str_nbits_reversed, str_nonce_reversed, str_soln_reversed):
    return str_version_reversed + str_prev_hash_reversed + str_merkle_root_reversed + str_reseverd + str_time_reversed + str_nbits_reversed + str_nonce_reversed + str_soln_reversed

#{"hash"(reversed):"0000000004b2b218261ab1294baf33a212c5c62c6c1946e483ab5df0afbe9869",
#"mainChain":true,"size":1619,"height":228942,"transactions":1,"version":4(04000000 reversed),
#"merkleRoot" (reversed):"2ebae32f35205e0ed226aef9875cf4c01ff168aa2feca303b1b29195a02f56e6",
#"timestamp (reversed)":1512097781,"time":14,
#"nonce":"00000000000000000000000000000000000000000000000000dbc60501499c01",
#"solution":"00f32689605e98831d36409c484f967d72e33c0bfb1523a56b8f37693fd7f6e2050f3942c2cc34fa1138034874e0745025f36073a7b2e574b53f69919fe11e1df51927174eb170c983b82a1ad40f264073d3360f020026b2c22a319f5590a18532f700a9e96134745c177dc2be95d0657ac74ca198064ef38ca8ccbd353c04ad91408d987e97e15095f77139acbda19bb82d701ead87711b8e6359143c172d42570d76e01a7f27990b0c05b918138db911e694e48a6c6a65b8675cfde611393ff0cce0108fadc103e189dd2b618bb9d0bb7d3e79ea972c15e26df857580d3ffc4c7b208a1973e53f39f7b9e567ee3d9a2f644564694ae59e32dc867b12ab36420992de71d4a243b165755eda02a7d5f69e1dff40f1acd25702ca1376b922f677ae0b763f9a352b51ae0718616e879563574d093fb429da3dfea2702d22d42c73d18daf7bcab32178b64e231e393931c6044616affe36294fca1b15b2e07e0c3b6af71e863c68371bd5bb36aa77e767c8e747dc19d732fc9e36930565d8ac511bc8b93630243e277917f9b3fef9b94326a18e42658a0fe1a154c27b54e24b5673df7ace2e0656c7538e01e8cd8f1c53c0cb7f9c669659dff87112a732d039b66d49f4eda1c577a833871c6d1cd1d3081a5500c76878b58c3fd5c6f1b00499bc800ef1ff487c2b7ca7f4729fb9b9a774d6fa59226981fbd89805aada767a9308c1f0b890b6a5c2f84593008f2b8c55143e26bcd63199ce14b7f1d9ef5fe276ad1db28234d303d1f88dfc6f167a95124a7c376ec406fb8bb2469d0d3bd5da793139fbbb54f57ed80b4e84fec66d0853ab1f0b729e21af340449c0c083f544ffaf858022ea34aae81f0fa76443d2f8392e86a4cfa2f7fe1d177ff7224aca1a75c23191bfd8cc0878a15fca740e2292471eee90c3af8d2bd4a6d4d5c31a581539e0c701301210bc82233f3ace41bbb3ec6db6bbc27b9aa723ead56548106631e60aa2c517caa741563bbad3a80215f3698c441d18dd115616877f6cd28ac7b9108603e9ee30728ba6acec0550a0f8219111899cda1e2007a89e43338a905dfb1474e281d02ea14321bae67c1db7b95e615a5f99528b3972a56fe55b7ae2ff387a08084cf82b478c20fff40245fb4aefddd25a1d9d041d37fbd4372dac97b46e9481113f6149720f90e2870751edbcc383ab5b7ae562f2f540584636e1bb5eb323c01d52606743bddeff332775732aa96ee2aebb042a86daa0862504a7b915c45d68d1072a12e89aaae669d4450bdc24e51f38ca97178e7e995695f5bfa78017890fbe3a93816b0a2404832346970da6b97d6dfd24443245d6bb4d63e969526e7467ce958f8c5932851ee3133ab84fffc595d94284ea3fbcba56c8547106236a136dd2ac9c4fcfd1d4eeeaf84d29ffe09c9987025a449ba78a980501e1616ef6c2893070bfb11c490cc444f25695eeaddea1a14577be09525d1cd49e6007bb270b1aa595f35df646d21b4aafd21f3811bda908e8d963c0c50f590c0341a8d6354ead0ea41f15361009bae170a18729520672f2392d02cecc0ff74f40138fc7f1b247bde2bc3d23d8ef5d617b2e79fb289f24a316fb9c9df399bc16d79067514f9bc24ddf31f82f7477e5c64c9b6b4828038dbb39bba764db5cb07a1105ac0bb2dd5c8afb70b18185bf9c78b3cf92610f1d5c631efb550be7cb5264af7e2826bdfcb3bb1a871408eac6140de64a7b78283ed2e3801a699bf9cd063e519cd1c992558aaecb65bdc57b3b6a31dcb710251718bebccc1a4149f7fa5704f5ee5006386d53e949199405d1a6e4cb05f1dfc607b13ffe9602c4f74fb71ae0b6ab446cc4a3ccf97226ddee7508d82d393d742adb3c83f35a3545763043d6587747faf5b0fb23dd",
#"bits"(reversed):"1c14460a","difficulty":6620311.02622361,"chainWork":"0000000000000000000000000000000000000000000000000012ba3a78f34bd3",
#"miner":"t1VpYecBW4UudbGcy4ufh61eWxQCoFaUrPs",
#"prevHash"(reversed):"0000000012dfc1e02bbdda46500ffac92741f729a6d386bb5c91319dca52f3f5",
#"nextHash":"0000000001261d7847d65a7f4566cdd7852737f738171c6f5e3f769830b36ca3"}

def get_parameter_from_block_data(block_json_str):
    block_json = json.loads(block_json_str)
    str_version_reversed = "04000000"
    str_prev_hash_reversed = reverse.reverse(block_json[0]['prevHash'])
    str_merkle_root_reversed = reverse.reverse(block_json[0]['merkleRoot'])
    str_reserved = '0000000000000000000000000000000000000000000000000000000000000000'
    str_time_reversed = reverse.reverse(hex(block_json[0]['timestamp'])[2:])
    str_nbits_reversed = reverse.reverse(block_json[0]['bits'])
    str_nonce_reversed = block_json[0]['nonce']
    str_soln_reversed = block_json[0]['solution']
    return str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved, str_time_reversed, \
           str_nbits_reversed, str_nonce_reversed, str_soln_reversed

def hash(hexstr):
    hash_func = hashlib.sha256()
    hash_func.update(bytes.fromhex(hexstr))
    return hash_func.hexdigest()


if __name__ == '__main__':
    block_json_str = '[{"hash":"0000000004b2b218261ab1294baf33a212c5c62c6c1946e483ab5df0afbe9869","mainChain":true,"size":1619,"height":228942,"transactions":1,"version":4,"merkleRoot":"2ebae32f35205e0ed226aef9875cf4c01ff168aa2feca303b1b29195a02f56e6","timestamp":1512097781,"time":14,"nonce":"00000000000000000000000000000000000000000000000000dbc60501499c01",\
                        "solution":"00f32689605e98831d36409c484f967d72e33c0bfb1523a56b8f37693fd7f6e2050f3942c2cc34fa1138034874e0745025f36073a7b2e574b53f69919fe11e1df51927174eb170c983b82a1ad40f264073d3360f020026b2c22a319f5590a18532f700a9e96134745c177dc2be95d0657ac74ca198064ef38ca8ccbd353c04ad91408d987e97e15095f77139acbda19bb82d701ead87711b8e6359143c172d42570d76e01a7f27990b0c05b918138db911e694e48a6c6a65b8675cfde611393ff0cce0108fadc103e189dd2b618bb9d0bb7d3e79ea972c15e26df857580d3ffc4c7b208a1973e53f39f7b9e567ee3d9a2f644564694ae59e32dc867b12ab36420992de71d4a243b165755eda02a7d5f69e1dff40f1acd25702ca1376b922f677ae0b763f9a352b51ae0718616e879563574d093fb429da3dfea2702d22d42c73d18daf7bcab32178b64e231e393931c6044616affe36294fca1b15b2e07e0c3b6af71e863c68371bd5bb36aa77e767c8e747dc19d732fc9e36930565d8ac511bc8b93630243e277917f9b3fef9b94326a18e42658a0fe1a154c27b54e24b5673df7ace2e0656c7538e01e8cd8f1c53c0cb7f9c669659dff87112a732d039b66d49f4eda1c577a833871c6d1cd1d3081a5500c76878b58c3fd5c6f1b00499bc800ef1ff487c2b7ca7f4729fb9b9a774d6fa59226981fbd89805aada767a9308c1f0b890b6a5c2f84593008f2b8c55143e26bcd63199ce14b7f1d9ef5fe276ad1db28234d303d1f88dfc6f167a95124a7c376ec406fb8bb2469d0d3bd5da793139fbbb54f57ed80b4e84fec66d0853ab1f0b729e21af340449c0c083f544ffaf858022ea34aae81f0fa76443d2f8392e86a4cfa2f7fe1d177ff7224aca1a75c23191bfd8cc0878a15fca740e2292471eee90c3af8d2bd4a6d4d5c31a581539e0c701301210bc82233f3ace41bbb3ec6db6bbc27b9aa723ead56548106631e60aa2c517caa741563bbad3a80215f3698c441d18dd115616877f6cd28ac7b9108603e9ee30728ba6acec0550a0f8219111899cda1e2007a89e43338a905dfb1474e281d02ea14321bae67c1db7b95e615a5f99528b3972a56fe55b7ae2ff387a08084cf82b478c20fff40245fb4aefddd25a1d9d041d37fbd4372dac97b46e9481113f6149720f90e2870751edbcc383ab5b7ae562f2f540584636e1bb5eb323c01d52606743bddeff332775732aa96ee2aebb042a86daa0862504a7b915c45d68d1072a12e89aaae669d4450bdc24e51f38ca97178e7e995695f5bfa78017890fbe3a93816b0a2404832346970da6b97d6dfd24443245d6bb4d63e969526e7467ce958f8c5932851ee3133ab84fffc595d94284ea3fbcba56c8547106236a136dd2ac9c4fcfd1d4eeeaf84d29ffe09c9987025a449ba78a980501e1616ef6c2893070bfb11c490cc444f25695eeaddea1a14577be09525d1cd49e6007bb270b1aa595f35df646d21b4aafd21f3811bda908e8d963c0c50f590c0341a8d6354ead0ea41f15361009bae170a18729520672f2392d02cecc0ff74f40138fc7f1b247bde2bc3d23d8ef5d617b2e79fb289f24a316fb9c9df399bc16d79067514f9bc24ddf31f82f7477e5c64c9b6b4828038dbb39bba764db5cb07a1105ac0bb2dd5c8afb70b18185bf9c78b3cf92610f1d5c631efb550be7cb5264af7e2826bdfcb3bb1a871408eac6140de64a7b78283ed2e3801a699bf9cd063e519cd1c992558aaecb65bdc57b3b6a31dcb710251718bebccc1a4149f7fa5704f5ee5006386d53e949199405d1a6e4cb05f1dfc607b13ffe9602c4f74fb71ae0b6ab446cc4a3ccf97226ddee7508d82d393d742adb3c83f35a3545763043d6587747faf5b0fb23dd",\
                        "bits":"1c14460a","difficulty":6620311.02622361,"chainWork":"0000000000000000000000000000000000000000000000000012ba3a78f34bd3","miner":"t1VpYecBW4UudbGcy4ufh61eWxQCoFaUrPs","prevHash":"0000000012dfc1e02bbdda46500ffac92741f729a6d386bb5c91319dca52f3f5","nextHash":"0000000001261d7847d65a7f4566cdd7852737f738171c6f5e3f769830b36ca3"}]'
    str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved, str_time_reversed, \
        str_nbits_reversed, str_nonce_reversed, str_soln_reversed = get_parameter_from_block_data(block_json_str)
    chanllenge = construct_zec_challenge(str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved,
                                  str_time_reversed, str_nbits_reversed, str_nonce_reversed, str_soln_reversed)
    print(chanllenge[:280])
    print("chanllenge len is %d"%(chanllenge.__len__()/2 -1344))
    hash_str = hash(chanllenge)
    print(hash_str)
    hash_str = hash(hash_str)
    print(hash_str)


