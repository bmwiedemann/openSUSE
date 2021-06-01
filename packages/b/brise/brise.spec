#
# spec file for package brise
#
# Copyright (c) 2020 SUSE LLC
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
Version:        20210525+git.4f7fc2a
Release:        0
Summary:        Rime Input Schemas Collection
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/rime/brise
Source:         brise-%{version}.tar.xz
Source1:        rime-plum-go-%{version}.tar.xz
Source99:       README
BuildRequires:  golang(API) >= 1.13

%description
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

Brise is the input schemas collection of Rime.

%package -n rime-plum
Summary:        Rime's configuration manager
Group:          System/I18n/Chinese

%description -n rime-plum
Plum is rime's configuration manager.

%package -n rime-schema-default
Summary:        Default/Preset collection of rime schemas
Group:          System/I18n/Chinese
BuildArch:      noarch
Requires:       rime-schema-bopomofo
Requires:       rime-schema-cangjie
Requires:       rime-schema-essay
Requires:       rime-schema-luna-pinyin
Requires:       rime-schema-prelude
Requires:       rime-schema-stroke
Requires:       rime-schema-terra-pinyin

%description -n rime-schema-default
Default/Preset collection of rime schemas.

%package -n rime-schema-extra
Summary:        Extra collection of rime schemas
Group:          System/I18n/Chinese
BuildArch:      noarch
Requires:       rime-schema-array
Requires:       rime-schema-cantonese
Requires:       rime-schema-combo-pinyin
Requires:       rime-schema-double-pinyin
Requires:       rime-schema-emoji
Requires:       rime-schema-ipa
Requires:       rime-schema-jyutping
Requires:       rime-schema-middle-chinese
Requires:       rime-schema-pinyin-simp
Requires:       rime-schema-quick
Requires:       rime-schema-scj
Requires:       rime-schema-soutzoe
Requires:       rime-schema-stenotype
Requires:       rime-schema-wubi
Requires:       rime-schema-wugniu

%description -n rime-schema-extra
Extra collection of rime schemas.

%package -n rime-schema-all
Summary:        All rime input schemas
Group:          System/I18n/Chinese
BuildArch:      noarch
Requires:       rime-schema-default
Requires:       rime-schema-extra
Provides:       brise = %{version}
Obsoletes:      brise <= 0.39+git20190120.8d5bc2e

%description -n rime-schema-all
All rime input schemas.

%package -n rime-schema-bopomofo
Summary:        bopomofo input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-bopomofo
bopomofoinput schema for rime.

%package -n rime-schema-cangjie
Summary:        cangjie input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-cangjie
cangjieinput schema for rime.

%package -n rime-schema-essay
Summary:        essay input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-essay
essayinput schema for rime.

%package -n rime-schema-luna-pinyin
Summary:        luna-pinyin input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-luna-pinyin
luna-pinyininput schema for rime.

%package -n rime-schema-prelude
Summary:        prelude input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-prelude
preludeinput schema for rime.

%package -n rime-schema-stroke
Summary:        stroke input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-stroke
strokeinput schema for rime.

%package -n rime-schema-terra-pinyin
Summary:        terra-pinyin input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-terra-pinyin
terra-pinyininput schema for rime.

%package -n rime-schema-array
Summary:        array input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-array
arrayinput schema for rime.

%package -n rime-schema-cantonese
Summary:        cantonese input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-cantonese
cantoneseinput schema for rime.

%package -n rime-schema-combo-pinyin
Summary:        combo-pinyin input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-combo-pinyin
combo-pinyininput schema for rime.

%package -n rime-schema-double-pinyin
Summary:        double-pinyin input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-double-pinyin
double-pinyininput schema for rime.

%package -n rime-schema-emoji
Summary:        emoji input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-emoji
emojiinput schema for rime.

%package -n rime-schema-ipa
Summary:        ipa input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-ipa
ipainput schema for rime.

%package -n rime-schema-jyutping
Summary:        jyutping input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-jyutping
jyutpinginput schema for rime.

%package -n rime-schema-middle-chinese
Summary:        middle-chinese input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-middle-chinese
middle-chineseinput schema for rime.

%package -n rime-schema-pinyin-simp
Summary:        pinyin-simp input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-pinyin-simp
pinyin-simpinput schema for rime.

%package -n rime-schema-quick
Summary:        quick input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-quick
quickinput schema for rime.

%package -n rime-schema-scj
Summary:        scj input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-scj
scjinput schema for rime.

%package -n rime-schema-soutzoe
Summary:        soutzoe input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-soutzoe
soutzoeinput schema for rime.

%package -n rime-schema-stenotype
Summary:        stenotype input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-stenotype
stenotypeinput schema for rime.

%package -n rime-schema-wubi
Summary:        wubi input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-wubi
wubiinput schema for rime.

%package -n rime-schema-wugniu
Summary:        wugniu input schema for rime
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n rime-schema-wugniu
wugniuinput schema for rime.

%prep
%setup -q
echo %{_builddir}
mkdir -p %{_builddir}/go/src/github.com/marguerite
tar -xf %{SOURCE1} -C %{_builddir}/go/src/github.com/marguerite
cp -r %{_builddir}/go/src/github.com/marguerite/rime-plum-go-%{version}/vendor/* %{_builddir}/go/src/

%build
pushd %{_builddir}/go/src/github.com/marguerite/rime-plum-go-%{version}
export GOPATH=%{_builddir}/go
go build
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/go/src/github.com/marguerite/rime-plum-go-%{version}/rime-plum-go %{buildroot}%{_bindir}/rime-plum
mkdir -p %{buildroot}%{_datadir}/rime-data
rm -rf package
rm -rf config.txt
#touch %{buildroot}%{_datadir}/rime-data/presets
cp -r * %{buildroot}%{_datadir}/rime-data

%files -n rime-plum
%{_bindir}/rime-plum

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

%files -n rime-schema-essay
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/essay.txt

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

%files -n rime-schema-jyutping
%dir %{_datadir}/rime-data
%{_datadir}/rime-data/jyutping*.yaml
%{_datadir}/rime-data/yale*.yaml
%{_datadir}/rime-data/hkcantonese*.yaml

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
