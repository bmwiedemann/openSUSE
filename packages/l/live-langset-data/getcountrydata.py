import langtable

# Originally from YaST's list
locales = ["af_ZA", "ar_EG", "ast_ES", "bg_BG", "bn_BD", "bs_BA", "ca_ES", "cs_CZ", "cy_GB",
           "da_DK", "de_DE", "el_GR", "en_GB", "en_US", "es_ES", "et_EE", "fa_IR", "fi_FI",
           "fr_FR", "gl_ES", "gu_IN", "he_IL", "hi_IN", "hr_HR", "hu_HU", "id_ID", "it_IT",
           "ja_JP", "ka_GE", "km_KH", "ko_KR", "lt_LT", "mk_MK", "mr_IN", "nb_NO", "nl_NL",
           "nn_NO", "pa_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "si_LK", "sk_SK",
           "sl_SI", "sr_RS", "sv_SE", "ta_IN", "tg_TJ", "th_TH", "tr_TR", "uk_UA", "vi_VN",
           "wa_BE", "xh_ZA", "zh_CN", "zh_TW", "zu_ZA"]

for locale in locales:
    consolefont = langtable.list_consolefonts(languageId=locale)[0]
    keytable = langtable.list_keyboards(languageId=locale)[0]
    keytable = keytable.translate(str.maketrans('(', '-', ')'))  # fr(oss) -> fr-oss
    timezone = langtable.list_timezones(languageId=locale)[0]
    with open(locale, "w") as f:
        f.write(f"""RC_LANG='{locale}.UTF-8'
CONSOLE_FONT='{consolefont}'
KEYTABLE='{keytable}'
TIMEZONE='{timezone}'
""")
