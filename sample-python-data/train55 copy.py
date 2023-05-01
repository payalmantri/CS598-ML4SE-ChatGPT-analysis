def get_language_model(arch:Callable, vocab_sz:int, config:dict=None, drop_mult:float=1.):
    "Create a language model from `arch` and its `config`, maybe `pretrained`."
    meta = _model_meta[arch]
    config = ifnone(config, meta['config_lm'].copy())
    for k in config.keys(): 
        if k.endswith('_p'): config[k] *= drop_mult
    tie_weights,output_p,out_bias = map(config.pop, ['tie_weights', 'output_p', 'out_bias'])
    init = config.pop('init') if 'init' in config else None
    encoder = arch(vocab_sz, **config)
    enc = encoder.encoder if tie_weights else None
    decoder = LinearDecoder(vocab_sz, config[meta['hid_name']], output_p, tie_encoder=enc, bias=out_bias)
    model = SequentialRNN(encoder, decoder)
    return model if init is None else model.apply(init)