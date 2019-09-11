#
# spec file for package sslscan
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sslscan
Version:        1.11.10
Release:        0
Summary:        SSL cipher scanning tool
License:        SUSE-GPL-3.0+-with-openssl-exception
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/rbsec/sslscan
Source:         https://github.com/rbsec/sslscan/archive/%{version}-rbsec.tar.gz#/%{name}-%{version}-rbsec.tar.gz
#Patches copied from Debian package
Patch1:         fedora-sslscan-patents.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl) < 1.1.0
%if 0%{?sle_version}
%ifarch x86_64
BuildRequires:  glibc-devel-32bit(x86-32)
%endif
%endif

%description
SSLScan determines what ciphers are supported on SSL-based services,
such as HTTPS. Furthermore, SSLScan will determine the preferred
ciphers of the SSL service.

%prep
%setup -q -n %{name}-%{version}-rbsec
%if %{defined fedora}
%patch1 -p1
%endif

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -d "%{buildroot}%{_bindir}"
install -d "%{buildroot}%{_mandir}/man1"
make install PREFIX="%{buildroot}%{_prefix}"

%files
%defattr(0644,root,root)
%doc LICENSE README.md
%attr(0755,root,root) %{_bindir}/sslscan
%{_mandir}/man1/sslscan.1%{ext_man}

%changelog
