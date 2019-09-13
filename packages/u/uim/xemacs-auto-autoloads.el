;; -*- no-byte-compile: t -*-

(autoload 'uim-leim-activate "uim-leim")

;; candidate display style of this buffer
(defvar uim-candidate-display-inline t
  "If non-nil, a candidate list is displayed below the
preedit string in vertical direction.  Otherwise, it is 
displayed at the echo area.")

(register-input-method "ascii-direct-uim" "English"
                       'uim-leim-activate "uim"
                       "ASCII uim direct")

(register-input-method "ascii-latin-uim" "English"
                       'uim-leim-activate "uim"
                       "ASCII uim latin")

(register-input-method "ascii-ipa-x-sampa-uim" "IPA"
                       'uim-leim-activate "uim"
                       "ASCII uim ipa-x-sampa")

(register-input-method "vietnamese-viqr-uim" "Vietnamese"
                       'uim-leim-activate "uim"
                       "Vietnamese uim viqr")

(register-input-method "korean-romaja-uim" "Korean"
                       'uim-leim-activate "uim"
                       "Korean uim romaja")

(register-input-method "korean-hangul3-uim" "Korean"
                       'uim-leim-activate "uim"
                       "Korean uim hangul3")

(register-input-method "korean-hangul2-uim" "Korean"
                       'uim-leim-activate "uim"
                       "Korean uim hangul2")

(register-input-method "korean-byeoru-uim" "Korean"
                       'uim-leim-activate "uim"
                       "Korean uim byeoru")

(register-input-method "japanese-tutcode-uim" "Japanese"
                       'uim-leim-activate "uim"
                       "Japanese uim tutcode")

(register-input-method "japanese-skk-uim" "Japanese"
                       'uim-leim-activate "uim"
                       "Japanese uim skk")

(register-input-method "japanese-canna-uim" "Japanese"
                       'uim-leim-activate "uim"
                       "Japanese uim canna")

(register-input-method "japanese-anthy-uim" "Japanese"
                       'uim-leim-activate "uim"
                       "Japanese uim anthy")

(register-input-method "chinese-big5-pinyin-big5-uim" "Chinese Big5"
                       'uim-leim-activate "uim"
                       "Chinese Big5 uim pinyin-big5")

(register-input-method "chinese-gb-pyunihan-uim" "Chinese GB"
                       'uim-leim-activate "uim"
                       "Chinese GB uim pyunihan")

(register-input-method "chinese-gb-py-uim" "Chinese GB"
                       'uim-leim-activate "uim"
                       "Chinese GB uim py")




