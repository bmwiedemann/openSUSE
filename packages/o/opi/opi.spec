#
# spec file for package opi
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


Name:           opi
Version:        0.9.0
Release:        0
Summary:        OBS Package Installer (CLI)
License:        GPL-3.0-only
Group:          System/Packages
URL:            https://github.com/openSUSE/%{name}
Source0:        https://github.com/openSUSE/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  perl
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::LibXML)
Requires:       perl
Requires:       perl(Config::Tiny)
Requires:       perl(LWP)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(URI)
Requires:       perl(XML::LibXML)

%description
OBS Package Installer (CLI)

%prep
%setup -q

%build
help2man ./opi > opi.8.gz
gzip opi.8.gz

%install
mkdir -p %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/metainfo
cp org.openSUSE.opi.appdata.xml %{buildroot}%{_datadir}/metainfo
mkdir -p %{buildroot}%{_datadir}/man/man8
cp opi.8.gz %{buildroot}%{_datadir}/man/man8

%files
%license LICENSE
%doc README.md screenshot.png
%{_bindir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.openSUSE.opi.appdata.xml
%dir %{_datadir}/man
%dir %{_datadir}/man/man8
%{_datadir}/man/man8/opi.8.gz

%changelog
