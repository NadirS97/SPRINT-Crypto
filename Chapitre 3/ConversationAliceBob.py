# !/usr/bin/env python3

m1Bob = bytes.fromhex('416c6963652c206a27616920756e20736f7563692061766563206d6120636f6e666967206970736563')
m1Alice = bytes.fromhex('416820626f6e203f')
m2Bob = bytes.fromhex(
    '4f75692c20706f757274616e74206a276169206661697420636f6d6d65207475206d276173206469742e20526567617264652c206a276169206c657320626f6e6e657320636cc3a973203a')
m3Bob = bytes.fromhex(
    '454e4341423d307833633037633733373761353939343538663931626366306462613337323233300a4d414341423d307836326464376435396266383136356538663938343938396632616363633166640a454e4342413d307865643238323638643366343330643535316233336638626365326461333631380a4d414342413d307864656436306666643433643164376533363663336238656530313531306239360a')
m2Alice = bytes.fromhex(
    '456e2065666665742c206c657320636cc3a97320736f6e7420626f6e6e65732c207475206173206dc3a9726974c3a920756e20746f6b656e203a204e4752524e4d4e505542414247505355524c50474e4c44452e')
m3Alice = bytes.fromhex(
    '457420746f6e207363726970742c207475206c276173206164617074c3a920c3a020706172746972206475206d69656e203f')
m4Bob = bytes.fromhex('4f75692021')
m4Alice = bytes.fromhex('4a65207465206c65207265646f6e6e65203a')
m5Alice = bytes.fromhex(
    '232323232323232053544154450a6970207866726d20737461746520666c7573680a6970207866726d2073746174652061646420737263203130302e31302e31302e313020647374203130302e32302e32302e3230205c0a0970726f746f20657370207370692031363634206d6f64652074756e6e656c205c0a09656e632022636263286165732922202224454e43414222205c0a09617574682d7472756e632022686d6163286d643529222022244d41434142222039360a6970207866726d2073746174652061646420737263203130302e32302e32302e323020647374203130302e31302e31302e3130205c0a0970726f746f20657370207370692031333337206d6f64652074756e6e656c205c0a09656e632022636263286165732922202224454e43424122205c0a09617574682d7472756e632022686d6163286d643529222022244d41434241222039360a23232323232320504f4c4943590a6970207866726d20706f6c69637920666c7573680a6970207866726d20706f6c6963792061646420737263203139322e3136382e322e302f323420647374203139322e3136382e312e302f3234205c0a096469722066776420746d706c20737263203130302e32302e32302e323020647374203130302e31302e31302e3130205c0a090970726f746f20657370206d6f64652074756e6e656c0a6970207866726d20706f6c6963792061646420737263203139322e3136382e322e302f323420647374203139322e3136382e312e302f3234205c0a0964697220696e20746d706c20737263203130302e32302e32302e323020647374203130302e31302e31302e3130205c0a090970726f746f20657370206d6f64652074756e6e656c0a6970207866726d20706f6c6963792061646420737263203139322e3136382e312e302f323420647374203139322e3136382e322e302f3234205c0a09646972206f757420746d706c20737263203130302e31302e31302e313020647374203130302e32302e32302e3230205c0a090970726f746f20657370206d6f64652074756e6e656c0a')

m5Bob = bytes.fromhex(
    '4f682e2e2e204a2761692074726f7576c3a92c206a276176616973206f75626c69c3a920642761646170746572206c65206677642e')
m6Alice = bytes.fromhex('426f6e20616c6f7273206f6e20706173736520656e20636869666672c3a92e')
m6Bob = bytes.fromhex(
    '4f75692c206574206a65207465206d6f6e747265206c65732070726f746f636f6c657320717565206a2761692064c3a976656c6f7070c3a9732e')
print(m1Bob, '\n', m1Alice, '\n', m2Bob, '\n', m3Bob, '\n', m2Alice, '\n', m3Alice, '\n', m4Bob, '\n', m4Alice, '\n',
      m5Alice, '\n', m5Bob, '\n', m6Alice, '\n', m6Bob)