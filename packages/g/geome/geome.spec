#
# spec file for package geome
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           geome
Version:        1.0.0
Release:        0
Summary:        Lightweight CLI tool for geolocation and network metadata
License:        MIT
URL:            https://github.com/GnuJason/geome
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libcurl)
Requires:       ca-certificates-mozilla

%description
Geome is a lightweight, fast CLI tool for retrieving user geolocation and
network metadata, including city, region, country, coordinates, IP address,
and ISP.This tool sends your public IP to a third-party API (ipwho.is) to retrieve geolocation data.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
%make_build check

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/geome
%{_mandir}/man1/geome.1%{?ext_man}

%changelog
