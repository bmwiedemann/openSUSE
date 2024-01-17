#
# spec file for package cm-unicode-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           cm-unicode-fonts
Version:        0.7.0
Release:        0
Summary:        Unicode Version of the Computer Modern Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://canopus.iacp.dvo.ru/~panov/cm-unicode/
Source0:        ftp://canopus.iacp.dvo.ru/pub/Font/cm_unicode/cm-unicode-0.7.0-otf.tar.xz
BuildRequires:  fontpackages-devel
BuildRequires:  xz
%reconfigure_fonts_prereq
Provides:       locale(ru;bg;el)
Obsoletes:      cm-unicode <= %{version}
Provides:       cm-unicode = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Computer Modern Unicode fonts were converted from metafont sources
using [1] textrace and [2] pfaedit (030404). Their main purpose is to
create free good quality fonts for use in X Window System applications
supporting many languages. Currently the fonts contain glyphs from
Latin1 (Metafont ec, tc), Cyrillic (la, rx) and Greek (cbgreek when
available) code sets.

%prep
%setup -q -n cm-unicode-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -c -m 644 *.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc Changes FAQ FontLog.txt Fontmap.CMU* OFL* README TODO fonts.scale
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%changelog
