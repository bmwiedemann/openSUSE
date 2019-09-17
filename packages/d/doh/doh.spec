#
# spec file for package doh
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           doh
Version:        0.0.0+git.20190908
Release:        0
Summary:        Simple DoH (DNS-over-HTTPS) client
License:        MIT
Group:          Productivity/Networking/DNS/Utilities
URL:            https://github.com/curl/doh
#Git-Clone:     https://github.com/curl/doh.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)

%description
A libcurl-using application that resolves a host name using
DNS-over-HTTPS (DOH).
This code uses POST requests unconditionally for this.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -Dm 0755 doh %{buildroot}%{_bindir}/doh

%files
%license LICENSE
%doc README.md
%{_bindir}/doh

%changelog
