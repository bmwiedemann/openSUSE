#
# spec file for package lomt-raleway-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           lomt-raleway-fonts
Version:        4.101
Release:        0
Summary:        Elegant sans-serif typeface family
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/theleagueof/raleway
Source:         https://github.com/theleagueof/raleway/releases/download/%version/Raleway-%version.tar.xz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildArch:      noarch
BuildRequires:  unzip
Obsoletes:      raleway-fonts
Provides:       raleway-fonts

%description
Raleway is a sans-serif typeface. It is a display face that features
both old style and lining numerals, standard and discretionary
ligatures, diacritics, as well as stylistic alternates inspired by
more geometric sans-serif typefaces than it's neo-grotesque inspired
default character set.

%prep
%autosetup -n Raleway-%version

%build
chmod 644 FONTLOG.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 static/OTF/*.otf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%doc OFL.md FONTLOG.txt
%{_ttfontsdir}

%changelog
