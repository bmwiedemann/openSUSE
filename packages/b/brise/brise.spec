#
# spec file for package brise
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           brise
Version:        20230603+git.5fdd2d6
Release:        0
Summary:        Rime Input Schemas Collection
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/rime/brise
Source:         brise-%{version}.tar.xz
Source99:       README
BuildRequires:  golang(API) >= 1.17

%description
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

Brise is the input schemas collection of Rime.

%package -n rime-schema-default
Summary:        Default/Preset collection of rime schemas
Group:          System/I18n/Chinese
Requires:       rime-schema-bopomofo
Requires:       rime-schema-cangjie
Requires:       rime-schema-custom
Requires:       rime-schema-essay
Requires:       rime-schema-luna-pinyin
Requires:       rime-schema-prelude
Requires:       rime-schema-stroke
Requires:       rime-schema-terra-pinyin
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-default
Default/Preset collection of rime schemas.

%package -n rime-schema-extra
Summary:        Extra collection of rime schemas
Group:          System/I18n/Chinese
Requires:       rime-schema-array
Requires:       rime-schema-cantonese
Requires:       rime-schema-combo-pinyin
Requires:       rime-schema-double-pinyin
Requires:       rime-schema-emoji
Requires:       rime-schema-essay-simp
Requires:       rime-schema-ipa
Requires:       rime-schema-middle-chinese
Requires:       rime-schema-pinyin-simp
Requires:       rime-schema-quick
Requires:       rime-schema-scj
Requires:       rime-schema-soutzoe
Requires:       rime-schema-stenotype
Requires:       rime-schema-wubi
Requires:       rime-schema-wugniu
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-extra
Extra collection of rime schemas.

%package -n rime-schema-all
Summary:        All rime input schemas
Group:          System/I18n/Chinese
Requires:       rime-schema-bopomofo
Requires:       rime-schema-cangjie
Requires:       rime-schema-custom
Requires:       rime-schema-essay
Requires:       rime-schema-luna-pinyin
Requires:       rime-schema-prelude
Requires:       rime-schema-stroke
Requires:       rime-schema-terra-pinyin
Requires:       rime-schema-array
Requires:       rime-schema-cantonese
Requires:       rime-schema-combo-pinyin
Requires:       rime-schema-double-pinyin
Requires:       rime-schema-emoji
Requires:       rime-schema-essay-simp
Requires:       rime-schema-ipa
Requires:       rime-schema-middle-chinese
Requires:       rime-schema-pinyin-simp
Requires:       rime-schema-quick
Requires:       rime-schema-scj
Requires:       rime-schema-soutzoe
Requires:       rime-schema-stenotype
Requires:       rime-schema-wubi
Requires:       rime-schema-wugniu
Provides:       brise = %{version}
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-all
All rime input schemas.

%package -n rime-schema-bopomofo
Summary:        bopomofo input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-bopomofo
bopomofo input schema for rime.

%package -n rime-schema-cangjie
Summary:        cangjie input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-cangjie
cangjie input schema for rime.

%package -n rime-schema-custom
Summary:        basic schema to customize rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-custom
basic schema to customize rime.

%package -n rime-schema-essay
Summary:        essay input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-essay
essay input schema for rime.

%package -n rime-schema-essay-simp
Summary:        simplified essay input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-essay-simp
simplified essay input schema for rime.

%package -n rime-schema-luna-pinyin
Summary:        luna-pinyin input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-luna-pinyin
luna-pinyin input schema for rime.

%package -n rime-schema-prelude
Summary:        prelude input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-prelude
prelude input schema for rime.

%package -n rime-schema-stroke
Summary:        stroke input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-stroke
stroke input schema for rime.

%package -n rime-schema-terra-pinyin
Summary:        terra-pinyin input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-terra-pinyin
terra-pinyin input schema for rime.

%package -n rime-schema-array
Summary:        array input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-array
array input schema for rime.

%package -n rime-schema-cantonese
Summary:        cantonese input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch
Provides:       rime-schema-jyutping > 20230528+git.cece251
Obsoletes:      rime-schema-jyutping <= 20230528+git.cece251
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e

%description -n rime-schema-cantonese
cantonese(jyutping) input schema for rime.

%package -n rime-schema-combo-pinyin
Summary:        combo-pinyin input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-combo-pinyin
combo-pinyin input schema for rime.

%package -n rime-schema-double-pinyin
Summary:        double-pinyin input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-double-pinyin
double-pinyin input schema for rime.

%package -n rime-schema-emoji
Summary:        emoji input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-emoji
emoji input schema for rime.

%package -n rime-schema-ipa
Summary:        ipa input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-ipa
ipa input schema for rime.

%package -n rime-schema-middle-chinese
Summary:        middle-chinese input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-middle-chinese
middle-chinese input schema for rime.

%package -n rime-schema-pinyin-simp
Summary:        pinyin-simp input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-pinyin-simp
pinyin-simp input schema for rime.

%package -n rime-schema-quick
Summary:        quick input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-quick
quick input schema for rime.

%package -n rime-schema-scj
Summary:        scj input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-scj
scj input schema for rime.

%package -n rime-schema-soutzoe
Summary:        soutzoe input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-soutzoe
soutzoe input schema for rime.

%package -n rime-schema-stenotype
Summary:        stenotype input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-stenotype
stenotype input schema for rime.

%package -n rime-schema-wubi
Summary:        wubi input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-wubi
wubi input schema for rime.

%package -n rime-schema-wugniu
Summary:        wugniu input schema for rime
Group:          System/I18n/Chinese
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e
BuildArch:      noarch

%description -n rime-schema-wugniu
wugniu input schema for rime.

%prep
%setup -q
echo %{_builddir}

%build

%install
mkdir -p %{buildroot}%{_datadir}/rime-data
cp -r package/rime/custom/*.recipe.yaml %{buildroot}%{_datadir}/rime-data
rm -rf package
rm -rf config.txt
cp -r * %{buildroot}%{_datadir}/rime-data

%files -n rime-schema-default
%dir %{_datadir}/rime-data

%files -n rime-schema-extra
%dir %{_datadir}/rime-data

%files -n rime-schema-all
%dir %{_datadir}/rime-data

%files -n rime-schema-bopomofo
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/bopomofo*.yaml
%{_datadir}/rime-data/zhuyin.yaml

%files -n rime-schema-cangjie
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/cangjie*.yaml

%files -n rime-schema-custom
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/add.recipe.yaml
%{_datadir}/rime-data/clear_schema_list.recipe.yaml
%{_datadir}/rime-data/set.recipe.yaml
%{_datadir}/rime-data/use_key_bindings.recipe.yaml
%{_datadir}/rime-data/use_switch_key.recipe.yaml
%{_datadir}/rime-data/use_symbols.recipe.yaml

%files -n rime-schema-essay
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/essay.txt
%{_datadir}/rime-data/essay-cantonese.txt

%files -n rime-schema-essay-simp
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/essay-zh-hans.txt

%files -n rime-schema-luna-pinyin
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/luna_pinyin*.yaml
%{_datadir}/rime-data/pinyin.yaml
%{_datadir}/rime-data/luna_quanpin*.yaml

%files -n rime-schema-prelude
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/default.yaml
%{_datadir}/rime-data/key_bindings.yaml
%{_datadir}/rime-data/punctuation.yaml
%{_datadir}/rime-data/symbols.yaml

%files -n rime-schema-stroke
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/stroke*.yaml

%files -n rime-schema-terra-pinyin
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/terra_pinyin*.yaml

%files -n rime-schema-array
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/array*.yaml

%files -n rime-schema-cantonese
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/jyut6ping3*.yaml
%{_datadir}/rime-data/symbols_cantonese.yaml

%files -n rime-schema-combo-pinyin
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/combo_pinyin*.yaml

%files -n rime-schema-double-pinyin
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/double_pinyin*.yaml

%files -n rime-schema-emoji
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/emoji*.yaml

%files -n rime-schema-ipa
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/ipa*.yaml

%files -n rime-schema-middle-chinese
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/sampheng*.yaml
%{_datadir}/rime-data/zyenpheng*.yaml

%files -n rime-schema-pinyin-simp
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/pinyin_simp*.yaml

%files -n rime-schema-quick
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/quick*.yaml

%files -n rime-schema-scj
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/scj*.yaml

%files -n rime-schema-soutzoe
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/soutzoe*.yaml

%files -n rime-schema-stenotype
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/stenotype*.yaml

%files -n rime-schema-wubi
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/wubi*.yaml

%files -n rime-schema-wugniu
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/wugniu*.yaml

%changelog
