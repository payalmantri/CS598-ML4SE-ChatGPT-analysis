def convert_weights(wgts:Weights, stoi_wgts:Dict[str,int], itos_new:Collection[str]) -> Weights:
    "Convert the model `wgts` to go with a new vocabulary."
    dec_bias, enc_wgts = wgts.get('1.decoder.bias', None), wgts['0.encoder.weight']
    wgts_m = enc_wgts.mean(0)
    if dec_bias is not None: bias_m = dec_bias.mean(0)
    new_w = enc_wgts.new_zeros((len(itos_new),enc_wgts.size(1))).zero_()
    if dec_bias is not None: new_b = dec_bias.new_zeros((len(itos_new),)).zero_()
    for i,w in enumerate(itos_new):
        r = stoi_wgts[w] if w in stoi_wgts else -1
        new_w[i] = enc_wgts[r] if r>=0 else wgts_m
        if dec_bias is not None: new_b[i] = dec_bias[r] if r>=0 else bias_m
    wgts['0.encoder.weight'] = new_w
    if '0.encoder_dp.emb.weight' in wgts: wgts['0.encoder_dp.emb.weight'] = new_w.clone()
    wgts['1.decoder.weight'] = new_w.clone()
    if dec_bias is not None: wgts['1.decoder.bias'] = new_b
    return wgts