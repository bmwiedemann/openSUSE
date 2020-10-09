#
# spec file for package ibus-table-chinese
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


Name:           ibus-table-chinese
Version:        1.8.3~pre.1531454400.f1f6a33
Release:        0
Summary:        Various Chinese input method table for the IBus framework
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/definite/ibus-table-chinese
Source:         %{name}-%{version}.tar.xz
Source1:        cmake-fedora-1501567859.7d52977.tar.xz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ibus-table)
BuildArch:      noarch

%description
ibus-table-chinese provides the infrastructure for Chinese input methods.
Input tables themselves are in sub-packages.

%package array
Summary:        The "array" input methods for Chinese
Group:          System/I18n/Chinese
Provides:       ibus-table-array30 = %{version}-%{release}
Provides:       locale(ibus:zh_TW;zh_HK)
Obsoletes:      ibus-table-array30 < 1.3
%{ibus_table_requires}

%description array
Array input method is a character-structured input method, including:
array30: 27489 characters.
array30-big: 27489 characters + Unicode ExtB.

%package cangjie
Summary:        Cangjie based input methods
Group:          System/I18n/Chinese
Provides:       ibus-table-cangjie = %{version}-%{release}
Provides:       locale(ibus:zh_TW;zh_HK)
Obsoletes:      ibus-table-cangjie < 1.3
%{ibus_table_requires}

%description cangjie
Cangjie based input methods, including:
Cangjie3, Canjie5, and Cangjie big tables.

%package cantonese
Summary:        Cantonese input methods
Group:          System/I18n/Chinese
Provides:       ibus-table-cantonese = %{version}-%{release}
Provides:       locale(ibus:zh_TW;zh_HK)
Obsoletes:      ibus-table-cantonese < 1.3
%{ibus_table_requires}

%description cantonese
Cantonese input methods, including:
Cantonese, Hong-Kong version of Cantonese.

%package jyutping
Summary:        Jyutping input method
Group:          System/I18n/Chinese
Provides:       ibus-table-jyutping = %{version}
Provides:       locale(ibus:zh_TW;zh_HK)
Obsoletes:      ibus-table-jyutping <= 1.2.0.20090824
%{ibus_table_requires}

%description jyutping
ibus-table-jyutping provides the Jyutping input method on IBus Table under
the IBus framework.

%package easy
Summary:        The so-called "easy" input method for Chinese
Group:          System/I18n/Chinese
Provides:       ibus-table-easy = %{version}-%{release}
Provides:       locale(ibus:zh_TW;zh_HK)
Obsoletes:      ibus-table-easy < 1.3
%{ibus_table_requires}

%description easy
Easy phrase-wise input method.

%package erbi
Summary:        Erbi input method
Group:          System/I18n/Chinese
Provides:       ibus-table-erbi = %{version}-%{release}
Obsoletes:      ibus-table-erbi < 1.3
%{ibus_table_requires}
Provides:       locale(ibus:zh_CN)

%description erbi
Erbi input methods. Includes:
Super Erbi (as erbi)
and  Erbi Qin-Song (erbi-qs)

%package quick
Summary:        The so-called "Quick-to-learn" input methods for Chinese
Group:          System/I18n/Chinese
Provides:       ibus-table-quick = %{version}-%{release}
Provides:       locale(ibus:zh_TW;zh_HK)
Obsoletes:      ibus-table-quick < 1.3
%{ibus_table_requires}

%description quick
Quick-to-learn is based on the Cangjie input method,
but only needs Cangjie's first and last word-root
to form a character.

Includes:
Quick3, Quick5 and Quick-Classic,
and Smart Cangjie 6.

%package scj
Summary:        Smart Cangjie input method
Group:          System/I18n/Chinese
Provides:       ibus-table-cangjie = %{version}-%{release}
Provides:       locale(ibus:zh_TW;zh_HK)
Obsoletes:      ibus-table-cangjie < 1.3
%{ibus_table_requires}

%description scj
Smart Cangjie is an improved Cangjie base input method
which handles Cangjie, Quick, Cantonese, Chinese punctuation,
Japanese, 3000 frequent words by Hong Kong government,
both Traditional and Simplified Chinese.

This package includes Smart Cangjie 6.

%package stroke5
Summary:        Stroke 5 input method
Group:          System/I18n/Chinese
Provides:       ibus-table-stroke5 = %{version}-%{release}
Obsoletes:      ibus-table-stroke5 < 1.3
%{ibus_table_requires}
Provides:       locale(ibus:zh_CN)

%description stroke5
Stroke 5 input method.

%package wu
Summary:        Wu pronunciation input method
Group:          System/I18n/Chinese
Provides:       ibus-table-wu = %{version}-%{release}
Obsoletes:      ibus-table-wu < 1.3
%{ibus_table_requires}
Provides:       locale(ibus:zh_CN)

%description wu
Wu pronunciation input method.
URL: http://input.foruto.com/wu/

%package wubi-haifeng
Summary:        Haifeng Wubi input method
Group:          System/I18n/Chinese
Provides:       ibus-table-wubi = %{version}-%{release}
Provides:       locale(ibus:zh_CN)
Obsoletes:      ibus-table-wubi < 1.3
%{ibus_table_requires}

%description wubi-haifeng
Haifeng Wubi input methods. Current includes:
Haifeng Wubi 86.

%package wubi-jidian
Summary:        Jidian Wubi input method
Group:          System/I18n/Chinese
Provides:       ibus-table-wubi = %{version}-%{release}
Provides:       locale(ibus:zh_CN)
Obsoletes:      ibus-table-wubi < 1.3
%{ibus_table_requires}

%description wubi-jidian
Jidian Wubi input methods. Current includes:
Wubi 86.

%package yong
Summary:        YongMa input method
Group:          System/I18n/Chinese
Provides:       ibus-table-yong = %{version}-%{release}
Obsoletes:      ibus-table-yong < 1.3
%{ibus_table_requires}
Provides:       locale(ibus:zh_CN)

%description yong
YongMa input method.

%prep
%setup -q
# fix for cmake-fedora
rm -rf cmake-fedora
mkdir -p cmake-fedora
tar -xf %{S:1} --strip-components=1 -C cmake-fedora
cp -r cmake-fedora/Modules .
sed -i 's/\r//' tables/wubi-haifeng/COPYING
touch .gitignore

%build
export PYTHON=python3
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DDATA_DIR=%{_datadir} \
      -DPRJ_DOC_DIR=%{_docdir}/%{name} \
      -DCMAKE_FEDORA_TMP_DIR=. .
make -j1 V=1

%install
%make_install
rm -rf %{buildroot}%{_docdir}/%{name}

%post array
%ibus_table_index_post array30
%ibus_table_index_post array30-big

%post cangjie
%ibus_table_index_post cangjie3
%ibus_table_index_post cangjie5
%ibus_table_index_post cangjie-big

%post cantonese
%ibus_table_index_post cantonese
%ibus_table_index_post cantonhk

%post jyutping
%ibus_table_index_post jyutping

%post easy
%ibus_table_index_post easy-big

%post erbi
%ibus_table_index_post erbi
%ibus_table_index_post erbi-qs

%post quick
%ibus_table_index_post quick3
%ibus_table_index_post quick5
%ibus_table_index_post quick-classic

%post scj
%ibus_table_index_post scj6

%post stroke5
%ibus_table_index_post stroke5

%post wu
%ibus_table_index_post wu

%post wubi-haifeng
%ibus_table_index_post wubi-haifeng86

%post wubi-jidian
%ibus_table_index_post wubi-jidian86

%post yong
%ibus_table_index_post yong

%files array
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/array30.*
%{_ibus_tabledir}/array30.db
%{_ibus_icondir}/array30-big.*
%{_ibus_tabledir}/array30-big.db

%files cangjie
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/cangjie3.*
%{_ibus_tabledir}/cangjie3.db
%{_ibus_icondir}/cangjie5.*
%{_ibus_tabledir}/cangjie5.db
%{_ibus_icondir}/cangjie-big.*
%{_ibus_tabledir}/cangjie-big.db

%files cantonese
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/cantonese.*
%{_ibus_tabledir}/cantonese.db
%{_ibus_icondir}/cantonhk.*
%{_ibus_tabledir}/cantonhk.db
%{_ibus_icondir}/cantonyale.*
%{_ibus_tabledir}/cantonyale.db

%files jyutping
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/jyutping.*
%{_ibus_tabledir}/jyutping.db

%files easy
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/easy-big.*
%{_ibus_tabledir}/easy-big.db

%files erbi
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/erbi.*
%{_ibus_tabledir}/erbi.db
%{_ibus_icondir}/erbi-qs.*
%{_ibus_tabledir}/erbi-qs.db

%files quick
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/quick3.*
%{_ibus_tabledir}/quick3.db
%{_ibus_icondir}/quick5.*
%{_ibus_tabledir}/quick5.db
%{_ibus_icondir}/quick-classic.*
%{_ibus_tabledir}/quick-classic.db

%files scj
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/scj6.*
%{_ibus_tabledir}/scj6.db

%files stroke5
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/stroke5.*
%{_ibus_tabledir}/stroke5.db

%files wu
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/wu.*
%{_ibus_tabledir}/wu.db

%files wubi-haifeng
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%license tables/wubi-haifeng/COPYING
%doc tables/wubi-haifeng/README
%{_ibus_icondir}/wubi-haifeng86.*
%{_ibus_tabledir}/wubi-haifeng86.db

%files wubi-jidian
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/wubi-jidian86.*
%{_ibus_tabledir}/wubi-jidian86.db

%files yong
%license COPYING
%doc ChangeLog AUTHORS NEWS README RELEASE-NOTES.txt
%{_ibus_icondir}/yong.*
%{_ibus_tabledir}/yong.db

%changelog
