#
# spec file for package gdouros-analecta-fonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gdouros-analecta-fonts
Version:        5.17
Release:        0
Summary:        An Ecclesiastic Scripts Font
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://greekfonts.teilar.gr
# Download source:
# http://users.teilar.gr/~g1951d/Analecta.zip
Source0:        Analecta-%{version}.zip
Source1:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      analecta-fonts < 4.01
Provides:       analecta-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Analecta is an ecclesiastic scripts font, covering Basic Latin, Greek and Coptic, some Punctuation and other Symbols, Coptic, typographica varia, Specials, Gothic and Deseret.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
install -m 0644 %{SOURCE1} .

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE Analecta.pdf
%{_ttfontsdir}

%changelog
