#
# spec file for package kicad-i18n
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


Name:           kicad-i18n
Version:        5.1.7
Release:        0
Summary:        Localization for KiCad
# license same as KiCad package
License:        GPL-3.0-or-later AND AGPL-3.0-or-later
Group:          System/Localization
URL:            https://kicad-pcb.org
Source:         https://gitlab.com/kicad/code/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gettext
BuildArch:      noarch

%description
KiCad is a software suite used for Electronic Design Automation (EDA).

This package contains translations for KiCad

%package     -n kicad-lang-bg
Summary:        Bulgarian translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:bg)

%description -n kicad-lang-bg
This package contains Bulgarian translations for KiCad

%package     -n kicad-lang-ca
Summary:        Catalan translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:ca)

%description -n kicad-lang-ca
This package contains Catalan translations for KiCad

%package     -n kicad-lang-cs
Summary:        Czech translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:cs)

%description -n kicad-lang-cs
This package contains Czech translations for KiCad

%package     -n kicad-lang-de
Summary:        German translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:de)

%description -n kicad-lang-de
This package contains German translations for KiCad

%package     -n kicad-lang-el
Summary:        Greek translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:el)

%description -n kicad-lang-el
This package contains Greek translations for KiCad

%package     -n kicad-lang-en
Summary:        English translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:en)

%description -n kicad-lang-en
This package contains English translations for KiCad

%package     -n kicad-lang-es
Summary:        Spanish translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:es)

%description -n kicad-lang-es
This package contains Spanish translations for KiCad

%package     -n kicad-lang-fi
Summary:        Finnish translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:fi)

%description -n kicad-lang-fi
This package contains Finnish translations for KiCad

%package     -n kicad-lang-fr
Summary:        French translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:fr)

%description -n kicad-lang-fr
This package contains French translations for KiCad

%package     -n kicad-lang-hu
Summary:        Hungarian translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:hu)

%description -n kicad-lang-hu
This package contains Hungarian translations for KiCad

%package     -n kicad-lang-it
Summary:        Italian translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:it)

%description -n kicad-lang-it
This package contains Italian translations for KiCad

%package     -n kicad-lang-ja
Summary:        Japanese translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:ja)

%description -n kicad-lang-ja
This package contains Japanese translations for KiCad

%package     -n kicad-lang-ko
Summary:        Korean translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:ko)

%description -n kicad-lang-ko
This package contains Korean translations for KiCad

%package     -n kicad-lang-lt
Summary:        Lithuanian translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:lt)

%description -n kicad-lang-lt
This package contains Lithuanian translations for KiCad

%package     -n kicad-lang-nl
Summary:        Netherlandian translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:nl)

%description -n kicad-lang-nl
This package contains Netherlandian translations for KiCad

%package     -n kicad-lang-pl
Summary:        Polish translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:pl)

%description -n kicad-lang-pl
This package contains Polish translations for KiCad

%package     -n kicad-lang-pt
Summary:        Portuguese translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:pt)

%description -n kicad-lang-pt
This package contains Portuguese translations for KiCad

%package     -n kicad-lang-ru
Summary:        Russian translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:ru)

%description -n kicad-lang-ru
This package contains Russian translations for KiCad

%package     -n kicad-lang-sk
Summary:        Slovak translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:sk)

%description -n kicad-lang-sk
This package contains Slovak translations for KiCad

%package     -n kicad-lang-sl
Summary:        Slovene translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:sl)

%description -n kicad-lang-sl
This package contains Slovene translations for KiCad

%package     -n kicad-lang-sv
Summary:        Swedish translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:sv)

%description -n kicad-lang-sv
This package contains Swedish translations for KiCad

%package     -n kicad-lang-zh_CN
Summary:        Simplified Chinese translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:zh_CN)

%description -n kicad-lang-zh_CN
This package contains Simplified Chinese translations for KiCad

%package     -n kicad-lang-zh_TW
Summary:        Traditional Chinese translations for KiCad
Group:          System/Localization
Provides:       locale(kicad:zh_TW)

%description -n kicad-lang-zh_TW
This package contains Traditional Chinese translations for KiCad


%prep
%setup -q

%build
%cmake \
    -DKICAD_I18N_UNIX_STRICT_PATH=ON
%cmake_build

%install
%cmake_install

%files -n kicad-lang-bg
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/kicad.mo

%files -n kicad-lang-ca
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/kicad.mo

%files -n kicad-lang-cs
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/kicad.mo

%files -n kicad-lang-de
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/kicad.mo

%files -n kicad-lang-el
%lang(es) %{_datadir}/locale/el/LC_MESSAGES/kicad.mo

%files -n kicad-lang-en
%lang(es) %{_datadir}/locale/en/LC_MESSAGES/kicad.mo

%files -n kicad-lang-es
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/kicad.mo

%files -n kicad-lang-fi
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/kicad.mo

%files -n kicad-lang-fr
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/kicad.mo

%files -n kicad-lang-hu
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/kicad.mo

%files -n kicad-lang-it
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/kicad.mo

%files -n kicad-lang-ja
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/kicad.mo

%files -n kicad-lang-ko
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/kicad.mo

%files -n kicad-lang-lt
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/kicad.mo

%files -n kicad-lang-nl
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/kicad.mo

%files -n kicad-lang-pl
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/kicad.mo

%files -n kicad-lang-pt
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/kicad.mo

%files -n kicad-lang-ru
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/kicad.mo

%files -n kicad-lang-sk
%lang(sl) %{_datadir}/locale/sk/LC_MESSAGES/kicad.mo

%files -n kicad-lang-sl
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/kicad.mo

%files -n kicad-lang-sv
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/kicad.mo

%files -n kicad-lang-zh_CN
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/kicad.mo

%files -n kicad-lang-zh_TW
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/kicad.mo

%changelog
