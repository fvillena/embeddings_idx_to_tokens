import utils

translator = utils.Translator(
    r'../data/raw/corpus_ids_no_punct_single_line_ap_dd_fc_nc.vec',
    r'../data/raw/idx_to_tokens.pickle',
    r'../data/processed/corpus_words_no_punct_single_line_ap_dd_fc_nc.vec'
)
translator.translate()