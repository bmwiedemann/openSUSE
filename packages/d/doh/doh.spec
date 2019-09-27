#
# spec file for package doh
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.1
Release:        0
Summary:        Simple DoH (DNS-over-HTTPS) client
License:        MIT
Group:          Productivity/Networking/DNS/Utilities
URL:            https://github.com/curl/doh
#Git-Clone:     https://github.com/curl/doh.git
Source:         https://github.com/curl/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)

%description
A libcurl-using application that resolves a host name using
DNS-over-HTTPS (DOH).
This code uses POST requests unconditionally for this.

%prep
%setup -q -n doh-doh-%{version}

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -Dm 0755 doh %{buildroot}%{_bindir}/doh
install -Dm 0644 doh.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/doh
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
