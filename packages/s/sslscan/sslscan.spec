#
# spec file for package sslscan
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


Name:           sslscan
Version:        2.0.1
Release:        0
Summary:        SSL cipher scanning tool
License:        SUSE-GPL-3.0+-with-openssl-exception
Group:          Productivity/Networking/Diagnostic
Source:         https://github.com/rbsec/sslscan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patches copied from Debian package
Patch1:         fedora-sslscan-patents.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl) >= 1.1.1

%description
SSLScan determines what ciphers are supported on SSL-based services,
such as HTTPS. Furthermore, SSLScan will determine the preferred
ciphers of the SSL service.

%prep
%setup -q
%if %{defined fedora}
%patch1 -p1
%endif

%build
%make_build CFLAGS="%{optflags} -fPIE"

%install
install -d "%{buildroot}%{_bindir}"
install -d "%{buildroot}%{_mandir}/man1"
make install PREFIX="%{buildroot}%{_prefix}"

%files
%defattr(0644,root,root)
%doc README.md
%license LICENSE
%attr(0755,root,root) %{_bindir}/sslscan
%{_mandir}/man1/sslscan.1%{?ext_man}

%changelog
