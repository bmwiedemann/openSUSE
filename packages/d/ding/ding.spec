#
# spec file for package ding
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


Name:           ding
Version:        1.8.1
Release:        0
Summary:        An X Window System Dictionary Tool
License:        GPL-2.0+
Group:          Productivity/Office/Dictionary
Url:            http://www-user.tu-chemnitz.de/~fri/ding/
Source:         ftp://ftp.tu-chemnitz.de/pub/Local/urz/%{name}/%{name}-%{version}.tar.gz
Source1:        ding.desktop
Patch0:         ding-install.diff
Patch1:         ding-tk-version.diff
BuildRequires:  tk
BuildRequires:  update-desktop-files
Requires:       ding-dict-de_en
Requires:       tcl
Requires:       tk
Recommends:     agrep
Recommends:     ispell
Recommends:     ispell-american
Recommends:     ispell-ngerman
Suggests:       fortune
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Ding is a graphical frontend to an English-to-German dictionary
lookup and word spell checking. For full functionality, agrep and
ispell should be installed.

%package -n ding-dict-de_en
Summary:        German<->English word dictionary in DING syntax
Group:          Productivity/Office/Dictionary

%description -n ding-dict-de_en
This package contains the German<->English dictionary/wordlist from
TU Chemnitz in an easy markup language suitable for use with grep.
A recommended graphical frontend for using this dictionary is "ding".

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%install
mkdir -p "%{buildroot}/%{_bindir}" "%{buildroot}/%{_datadir}/dict" \
	"%{buildroot}/%{_datadir}/applications"
./install.sh <<EOF
%{buildroot}/%{_bindir}
%{buildroot}/%{_datadir}/dict
y
EOF
install -m 644 %{SOURCE1} "%{buildroot}/%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file %{name} Office Dictionary

%files
%defattr(-,root,root)
%doc COPYING README CHANGES
%{_bindir}/ding
%{_datadir}/applications/%{name}.desktop

%files -n ding-dict-de_en
%defattr(-,root,root)
%{_datadir}/dict/de-en.txt

%changelog
