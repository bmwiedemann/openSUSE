#
# spec file for package checksec
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2013-2021 Fedora Project Authors
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


Name:           checksec
Version:        3.0.0
Release:        0
Summary:        Utility to check binaries for system hardening
License:        BSD-3-Clause
URL:            https://github.com/slimm609/checksec.sh
Source0:        https://github.com/slimm609/checksec.sh/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.bz2
BuildRequires:  golang-packaging
BuildRequires:  golang(API)

%description
Checksec is a GO program to check the properties of executables (like PIE,
RELRO, PaX, Canaries, ASLR, Fortify Source). It has been originally written by
Tobias Klein and the original source is available here:
http://www.trapkit.de/tools/checksec.html

Modern Linux distributions offer some mitigation techniques to make it harder
to exploit software vulnerabilities reliably. Mitigations such as RELRO,
NoExecute (NX), Stack Canaries, Address Space Layout Randomization (ASLR) and
Position Independent Executables (PIE) have made reliably exploiting any
vulnerabilities that do exist far more challenging. The checksec script is
designed to test what *standard* Linux OS and PaX (http://pax.grsecurity.net/)
security features are being used.

%prep
%autosetup -p 1
tar xf %SOURCE1

%build
mkdir build
cd build
go build ..

%install
cd build
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -pm 0755 %{name} %{buildroot}%{_bindir}
cd ..
install -pm 0644 extras/man/%{name}.1 %{buildroot}%{_mandir}/man1

%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
