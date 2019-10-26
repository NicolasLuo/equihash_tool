import reverse
import json


def construct_zec_challenge(str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reseverd, str_time_reversed, str_nbits_reversed, str_nonce_reversed, str_soln_reversed):
    return str_version_reversed + str_prev_hash_reversed + str_merkle_root_reversed + str_reseverd + str_time_reversed + str_nbits_reversed + str_nonce_reversed + str_soln_reversed

#[{"hash":"00000000019aa81e55772c61079a061cf41242dd51334b342300f5a577ef97d7","mainChain":true,"size":22817,"height":625193,"transactions":15,"version":4,"merkleRoot":"c670f9c9d172eb0aacc827b14edc5b845769eb38f5790324e7e2995b71f8ac5d","timestamp":1571821238,"time":346,"nonce":"86800440000000000000000000cd000000000000000000008f3c3d0101650e2f","solution":"003631227ee47239f18c5122a42cf8c8839338137b16d5ee303e47774665ab019403371dae343657f41900b2870b5cb31251d83260890926aa8a5c093950e7173b9fdf720962fa7816940c67f96ebed516bf024a00961b223aa698c1c915b2377b4ba399da75f5672815c02ea05a5032d9bd9574a271d620bd75abb42d8a06c5fd6cd9bc421feb69122c5464848624961d1fec1751ef2111150a43bb3d1401d54ac4c98be8d8df3300d51c07081512d160b900ac91a8e61e68ccd6158d1abaf4bf7247759cd85d91c9bc3aee60a86ffc31d904e0cb8e44f09337affb15c7c4edbd69c243355de85e761cc93e991ca7142bd6a966426803257f5a7dd80a677c7173603879e4735116bcf50aaba75bffa24724f7332f9a701a8b9d3a5589d63eec5df17ef62117112e6392899fc07176bdc3200ce16b2317031bc67218425c44895748b760ebd730ec79dafe08dc1b564c00456e00a20fbe6778e2939790432a4728ca9b5da113b8ee9ea6cf920e85ba2247559b1a6e7842f8d67b07d07dd0dd434dc36418424e23caf5e0d5fcdd1b540c3bfdcb98d6c215fda4224316fd3bdb521fbe446d03222ba6328b23f36785c8dc43de4866b661fa742c0b682e8f8604ff9598ff64156cc0527511813eb001133a95bc61ee24bb9cba524aa422d778c2f77a877e278c84edf321b593947c1a75d3e3d11ec06bd6865e01eb4be316b6d6b3fc3de2ca4b265076599edb30ba2d777766cb205e0981e0e332ac5babb6fccefad633035625c46d169442db0a25de9165e831c1ef955be126ee07f92c4b3ca58b55e4dbd5391a6268dc554c7906ab476027856f1f4a6cd226f956c00caf6eefba1426275352f0ca2b4c58eef46536d2e649a118dda53e075bda7cf8142026ee4fe502d57b97bad3413c6b2c42e1d4a901663f65a26046a56449c392c536770bec0100ddb23cf7d7d7e453643f54e8b46d3e81f76e3d305419e90d901fcfc9c359a68878a49f307c3ea0500346a71fa26c15dbb69eb6cde1f9916df4d0184e4c11a86363dc52b08327bad25b2c1740f2471ff853050e74a349dbd24f7963d5aa5749e1b54b513e7b19eb2a7dce4b63116ec48fdf86c4797daf4ace1dbb57ae104482163170f775e8f1a51b3bf03b9f16329cf998147cfc94e647ca6cf5a393f7e7dbcccde97c1f057a12a59a77d160800b40a091fba629829128fff896d0264a524a308ebd750719c2c29ca91b7586360c33d81df95d1f321eed3b721045a0a0517391c274f1b6d34589e4a3e53549cfbc6b349931479f0e5a1c1782d823a42e2509a765336eaac4303c7eefa1302ad4e1a74d131f0ac2205159d4f834dbecf577de2ff85fcebe4733740be5dedca7f9c617a4026573fe44d25297c173f29de4589db7654655e7e4cec88fbae2ba1dfa3b01854cfb9d2f3391aadfc2627db8a718ec5a8e612c34ccbc0e020f853e95c99497d0b1a0f9bea70fab2f328f8cd3b3a99b73d96053d2ef41226513c0f4f49d391812368367a335bb61c6c4a9d0a875bf78df302e115e87bbffe43c9bf30dd7020ef2aefb02febf141b303f948e960e83129790e5425fc12621c05a92ece9146daf06226aa757ea30627948a9c5ae2b6b9b55e345721e8092eed9c9bb67faa5fe7f304eb226b70cfa01efb0b9236359d5e5ca805e307c5cb5285c798a9e38651aa5c3187897e7ae33cb55a026e2558a1b6edf0bdd2d0c9bcbef9f87cc41889c6ca360de77694a4f0f0ebb5491a70fd3d1fd116a77d24a7d6b723205e40ec4966a00d8e10f9126e20318642642cca5f92e4e1df311e838ccb1db3358240bfdec2dade8cdd062c317291f57110a4792d507a4c5c0dc89b1cffb7d54292b2181fea44addd3b48e75593f4b9fcdd73bb4eec9","bits":"1c01cade","difficulty":74879341.49137652,"chainWork":"00000000000000000000000000000000000000000000000001ddb072655ad38e","miner":"t1NkyNR1HQYgQdLEBp3mXTccF4Wat5XvHPC","prevHash":"0000000000c2eeca0dc8951cd448a3bc568a8b417233fc8795bf17ce41a32e7b"}]

#[{"hash":"00000000019aa81e55772c61079a061cf41242dd51334b342300f5a577ef97d7",
# "mainChain":true,"size":22817,"height":625193,"transactions":15,"version":4,
# "merkleRoot":"c670f9c9d172eb0aacc827b14edc5b845769eb38f5790324e7e2995b71f8ac5d",
# "timestamp":1571821238,"time":346,
# "nonce":"86800440000000000000000000cd000000000000000000008f3c3d0101650e2f",
# "solution":"003631227ee47239f18c5122a42cf8c8839338137b16d5ee303e47774665ab019403371dae343657f41900b2870b5cb31251d83260890926aa8a5c093950e7173b9fdf720962fa7816940c67f96ebed516bf024a00961b223aa698c1c915b2377b4ba399da75f5672815c02ea05a5032d9bd9574a271d620bd75abb42d8a06c5fd6cd9bc421feb69122c5464848624961d1fec1751ef2111150a43bb3d1401d54ac4c98be8d8df3300d51c07081512d160b900ac91a8e61e68ccd6158d1abaf4bf7247759cd85d91c9bc3aee60a86ffc31d904e0cb8e44f09337affb15c7c4edbd69c243355de85e761cc93e991ca7142bd6a966426803257f5a7dd80a677c7173603879e4735116bcf50aaba75bffa24724f7332f9a701a8b9d3a5589d63eec5df17ef62117112e6392899fc07176bdc3200ce16b2317031bc67218425c44895748b760ebd730ec79dafe08dc1b564c00456e00a20fbe6778e2939790432a4728ca9b5da113b8ee9ea6cf920e85ba2247559b1a6e7842f8d67b07d07dd0dd434dc36418424e23caf5e0d5fcdd1b540c3bfdcb98d6c215fda4224316fd3bdb521fbe446d03222ba6328b23f36785c8dc43de4866b661fa742c0b682e8f8604ff9598ff64156cc0527511813eb001133a95bc61ee24bb9cba524aa422d778c2f77a877e278c84edf321b593947c1a75d3e3d11ec06bd6865e01eb4be316b6d6b3fc3de2ca4b265076599edb30ba2d777766cb205e0981e0e332ac5babb6fccefad633035625c46d169442db0a25de9165e831c1ef955be126ee07f92c4b3ca58b55e4dbd5391a6268dc554c7906ab476027856f1f4a6cd226f956c00caf6eefba1426275352f0ca2b4c58eef46536d2e649a118dda53e075bda7cf8142026ee4fe502d57b97bad3413c6b2c42e1d4a901663f65a26046a56449c392c536770bec0100ddb23cf7d7d7e453643f54e8b46d3e81f76e3d305419e90d901fcfc9c359a68878a49f307c3ea0500346a71fa26c15dbb69eb6cde1f9916df4d0184e4c11a86363dc52b08327bad25b2c1740f2471ff853050e74a349dbd24f7963d5aa5749e1b54b513e7b19eb2a7dce4b63116ec48fdf86c4797daf4ace1dbb57ae104482163170f775e8f1a51b3bf03b9f16329cf998147cfc94e647ca6cf5a393f7e7dbcccde97c1f057a12a59a77d160800b40a091fba629829128fff896d0264a524a308ebd750719c2c29ca91b7586360c33d81df95d1f321eed3b721045a0a0517391c274f1b6d34589e4a3e53549cfbc6b349931479f0e5a1c1782d823a42e2509a765336eaac4303c7eefa1302ad4e1a74d131f0ac2205159d4f834dbecf577de2ff85fcebe4733740be5dedca7f9c617a4026573fe44d25297c173f29de4589db7654655e7e4cec88fbae2ba1dfa3b01854cfb9d2f3391aadfc2627db8a718ec5a8e612c34ccbc0e020f853e95c99497d0b1a0f9bea70fab2f328f8cd3b3a99b73d96053d2ef41226513c0f4f49d391812368367a335bb61c6c4a9d0a875bf78df302e115e87bbffe43c9bf30dd7020ef2aefb02febf141b303f948e960e83129790e5425fc12621c05a92ece9146daf06226aa757ea30627948a9c5ae2b6b9b55e345721e8092eed9c9bb67faa5fe7f304eb226b70cfa01efb0b9236359d5e5ca805e307c5cb5285c798a9e38651aa5c3187897e7ae33cb55a026e2558a1b6edf0bdd2d0c9bcbef9f87cc41889c6ca360de77694a4f0f0ebb5491a70fd3d1fd116a77d24a7d6b723205e40ec4966a00d8e10f9126e20318642642cca5f92e4e1df311e838ccb1db3358240bfdec2dade8cdd062c317291f57110a4792d507a4c5c0dc89b1cffb7d54292b2181fea44addd3b48e75593f4b9fcdd73bb4eec9",
# "bits":"1c01cade","difficulty":74879341.49137652,
# "chainWork":"00000000000000000000000000000000000000000000000001ddb072655ad38e",
# "miner":"t1NkyNR1HQYgQdLEBp3mXTccF4Wat5XvHPC",
# "prevHash":"0000000000c2eeca0dc8951cd448a3bc568a8b417233fc8795bf17ce41a32e7b"}]
def get_parameter_from_block_data(block_json_str):
    block_json = json.loads(block_json_str)
    str_version_reversed = "04000000"
    str_prev_hash_reversed = reverse.reverse(block_json[0]['prevHash'])
    str_merkle_root_reversed = reverse.reverse(block_json[0]['merkleRoot'])
    str_reserved = '0000000000000000000000000000000000000000000000000000000000000000'
    str_time_reversed = reverse.reverse(hex(block_json[0]['timestamp'])[2:])
    str_nbits_reversed = reverse.reverse(block_json[0]['bits'])
    str_nonce_reversed = reverse.reverse(block_json[0]['nonce'])
    str_soln_reversed = block_json[0]['solution']
    return str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved, str_time_reversed, \
           str_nbits_reversed, str_nonce_reversed, str_soln_reversed


if __name__ == '__main__':
    #str_version_reversed = "04000000"
    #str_prev_hash_reversed = reverse.reverse('000000056123f72012a98c71125eddf97da4fe360cdeb6db17609818ed559eae')
    #str_merkle_root_reversed = reverse.reverse('fa49460f0c4f39ce1c74187c23283f1f085fb941b824253a78e5dccfa31541d8')
    #str_reserved = '0000000000000000000000000000000000000000000000000000000000000000'
    #str_time_reversed = reverse.reverse('581697b2')
    #str_nbits_reversed = reverse.reverse('1d0946d2')
    #str_nonce_reversed = reverse.reverse('040000000000000000000000000006523d04002000000000000000002000043c')
    #str_soln_reversed = '0039833cbf13a7cb06ec34d771ae72c20a5c7bef6e5749bd69c3e381bd51e6f63b933b889e1a80fbdf4704566423345fd16907856586b632c2f1cd9cbdb2b017cd5633c589ce9db6aea58984f4e45dfeee35aee217d15d83189ed0bb6d55c2d631f35b76064edc2f0c187e3d22601f2eff317695b03175ed019e5b9095a11c3889c047a11127fef82563c47a1201cb0ef5b8921c544f14a0b5f389ec21c298ad97afd557819909a0056338457a145b0d27a650ae77d2a2b53a95bc62fb49ce4e5bf8e1d58b54860a8531d91ffec35c76979127654cbef8d6d5dccf6d779828d7e67397f9fd7fd8368146e452166e59fb9d76cbecfb8cce889ed9a67105f771bae086876288b0e3196e323358cd2a29ee4e659dbe57323b8663fa6dd76c91d0435a4ef23b090506ce5313409697b9f32aa7a2d3e64b9a42effe076c264f7a23c4586460edae292594626f466fd8da191a01c576b8004f37652ea3b36cc87ed2756688709a4017d69b97dc470037298d44d9f7e330b239e6783e820b3852fd429102bbb682524ba0936d08e24c47a68c261df4ca6fca403fe43054b0ddef27f13b329be50d08e465f08c9f27d1bbe7de536f79ef9b97219f93f857555e80e8790f29ec85d7bc9ce83976cee7bf8ead15b8f97c94722921d85574faa9f22f7b2d1b9aa3a71dad2ac17ad30dc506d223072ccca4093a4e6e83e903fdea0164f62901b88ae8051ce63776ceb5ded2a42a894c221191934d9edcf79e70468b5a6caf33d9761127156242c73b536e701422102975596b9dd0b9373e7d6f1c8e63c3f52b7fca34c952b7c37c8a1d3e81063879990b5bcd4796fe007235f35145781fbe4f620fe78612000edbe728c83a9b76fb05fea7e318cb280e8a7c8f5ce0c46d39d1b46eb7b1ff5b7b077d09204af9ffa4e418c7aaffed05fdff59d051cdd9b3455d016fc6f60bc67237ae3734b10faf7e2d8115adbbac12b8c3fd772f29219391018c83febdbd0d08542ee9098ba404fb8ddf5fb8e5964db7bbfef9c0acf0108d420c4459b9d7064b7e7ec4d8b07a39027303f8c1360bac48e146637f77cabd857044bde8b651723838761d591c0775e0d3b76120224787ffa106d4b9bda3921b09676ef121e6f58464542a1f6f988626d1989d4a1fd6715d9194eab1e6f494c87cec630dbd571bc84706ce088e0249a92654ae62169ecea3d763533b6da20f02c581cb5acbd6ffb4b1f893cc3ad89f0fc9aaf61560b53f881953c8e072325355c0467d01427190a61ed883486f52f8189bfae5045cb57352c81759a9b309c8fae5bdc550a5c02393e6a95eb5459e5a1a8f241ee80bdd3c4c951994de0359d55b5851196373acd50d24e9e6b4dc13a950a976cd20b9a6e5e1863769b31b34ec29c8dc42e30012c2427419429afe4218be32041b6ff58a0e9cebd8a2505561dbbc2ce21c7d526a1798a7b1da66b7abf988b51cb253e262e35f1db019049b0390b2200729529d8074a19529cefc3b18e0bb31ab0bf4a1255449af6c5349275de55dad3039e03d1c3c62d260b97647d9b53c27ddf7376f1b1a7e825161379b836ae2c29b5f5577464578044a7ff49f889e2235795eb1a785c19fa363883aca86437bac3d6b9e641e96e19024f5cf46f2f6b243e632eb66b07bf7fb063800e6ee458ed26e18d25ce02419076155ded66009ae43b3d2c26da9342ae3e41cebba0e2dfe1de79306da4478ed482a69223bb37694a5173f821c9e8f37431e543f2e1567a7f13c652939472d7216beb99dd216313a9bd8dddd4970101863dc6aa9aa2906573bc1515e36a1e6242559269f575458f9f5b5f2f3591ed018f137350b19e8c1cc5f62755538a7e135b3b369b71c81962cff9c73294a0b13be1f2dc0df13c6bd33e0'
    block_json_str = '[{"hash":"00000000019aa81e55772c61079a061cf41242dd51334b342300f5a577ef97d7","mainChain":true,"size":22817,"height":625193,"transactions":15,"version":4,"merkleRoot":"c670f9c9d172eb0aacc827b14edc5b845769eb38f5790324e7e2995b71f8ac5d","timestamp":1571821238,"time":346,"nonce":"86800440000000000000000000cd000000000000000000008f3c3d0101650e2f","solution":"003631227ee47239f18c5122a42cf8c8839338137b16d5ee303e47774665ab019403371dae343657f41900b2870b5cb31251d83260890926aa8a5c093950e7173b9fdf720962fa7816940c67f96ebed516bf024a00961b223aa698c1c915b2377b4ba399da75f5672815c02ea05a5032d9bd9574a271d620bd75abb42d8a06c5fd6cd9bc421feb69122c5464848624961d1fec1751ef2111150a43bb3d1401d54ac4c98be8d8df3300d51c07081512d160b900ac91a8e61e68ccd6158d1abaf4bf7247759cd85d91c9bc3aee60a86ffc31d904e0cb8e44f09337affb15c7c4edbd69c243355de85e761cc93e991ca7142bd6a966426803257f5a7dd80a677c7173603879e4735116bcf50aaba75bffa24724f7332f9a701a8b9d3a5589d63eec5df17ef62117112e6392899fc07176bdc3200ce16b2317031bc67218425c44895748b760ebd730ec79dafe08dc1b564c00456e00a20fbe6778e2939790432a4728ca9b5da113b8ee9ea6cf920e85ba2247559b1a6e7842f8d67b07d07dd0dd434dc36418424e23caf5e0d5fcdd1b540c3bfdcb98d6c215fda4224316fd3bdb521fbe446d03222ba6328b23f36785c8dc43de4866b661fa742c0b682e8f8604ff9598ff64156cc0527511813eb001133a95bc61ee24bb9cba524aa422d778c2f77a877e278c84edf321b593947c1a75d3e3d11ec06bd6865e01eb4be316b6d6b3fc3de2ca4b265076599edb30ba2d777766cb205e0981e0e332ac5babb6fccefad633035625c46d169442db0a25de9165e831c1ef955be126ee07f92c4b3ca58b55e4dbd5391a6268dc554c7906ab476027856f1f4a6cd226f956c00caf6eefba1426275352f0ca2b4c58eef46536d2e649a118dda53e075bda7cf8142026ee4fe502d57b97bad3413c6b2c42e1d4a901663f65a26046a56449c392c536770bec0100ddb23cf7d7d7e453643f54e8b46d3e81f76e3d305419e90d901fcfc9c359a68878a49f307c3ea0500346a71fa26c15dbb69eb6cde1f9916df4d0184e4c11a86363dc52b08327bad25b2c1740f2471ff853050e74a349dbd24f7963d5aa5749e1b54b513e7b19eb2a7dce4b63116ec48fdf86c4797daf4ace1dbb57ae104482163170f775e8f1a51b3bf03b9f16329cf998147cfc94e647ca6cf5a393f7e7dbcccde97c1f057a12a59a77d160800b40a091fba629829128fff896d0264a524a308ebd750719c2c29ca91b7586360c33d81df95d1f321eed3b721045a0a0517391c274f1b6d34589e4a3e53549cfbc6b349931479f0e5a1c1782d823a42e2509a765336eaac4303c7eefa1302ad4e1a74d131f0ac2205159d4f834dbecf577de2ff85fcebe4733740be5dedca7f9c617a4026573fe44d25297c173f29de4589db7654655e7e4cec88fbae2ba1dfa3b01854cfb9d2f3391aadfc2627db8a718ec5a8e612c34ccbc0e020f853e95c99497d0b1a0f9bea70fab2f328f8cd3b3a99b73d96053d2ef41226513c0f4f49d391812368367a335bb61c6c4a9d0a875bf78df302e115e87bbffe43c9bf30dd7020ef2aefb02febf141b303f948e960e83129790e5425fc12621c05a92ece9146daf06226aa757ea30627948a9c5ae2b6b9b55e345721e8092eed9c9bb67faa5fe7f304eb226b70cfa01efb0b9236359d5e5ca805e307c5cb5285c798a9e38651aa5c3187897e7ae33cb55a026e2558a1b6edf0bdd2d0c9bcbef9f87cc41889c6ca360de77694a4f0f0ebb5491a70fd3d1fd116a77d24a7d6b723205e40ec4966a00d8e10f9126e20318642642cca5f92e4e1df311e838ccb1db3358240bfdec2dade8cdd062c317291f57110a4792d507a4c5c0dc89b1cffb7d54292b2181fea44addd3b48e75593f4b9fcdd73bb4eec9","bits":"1c01cade","difficulty":74879341.49137652,"chainWork":"00000000000000000000000000000000000000000000000001ddb072655ad38e","miner":"t1NkyNR1HQYgQdLEBp3mXTccF4Wat5XvHPC","prevHash":"0000000000c2eeca0dc8951cd448a3bc568a8b417233fc8795bf17ce41a32e7b"}]'
    str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved, str_time_reversed, \
        str_nbits_reversed, str_nonce_reversed, str_soln_reversed = get_parameter_from_block_data(block_json_str)
    print(construct_zec_challenge(str_version_reversed, str_prev_hash_reversed, str_merkle_root_reversed, str_reserved,
                                  str_time_reversed, str_nbits_reversed, str_nonce_reversed, str_soln_reversed))


