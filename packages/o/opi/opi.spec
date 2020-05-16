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
Version:        0.8.2
Release:        0
Summary:        OBS Package Installer (CLI)
License:        GPL-3.0-only
Group:          System/Packages
URL:            https://github.com/openSUSE-zh/%{name}
Source0:        https://github.com/openSUSE-zh/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
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

%install
mkdir -p %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md screenshot.png
%{_bindir}/%{name}

%changelog
