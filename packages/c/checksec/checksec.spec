#
# spec file for package checksec
#
# Copyright (c) 2022 SUSE LLC
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
Version:        2.6.0
Release:        0
Summary:        Utility to check binaries for system hardening
License:        BSD-3-Clause
URL:            https://github.com/slimm609/checksec.sh
Source0:        https://github.com/slimm609/checksec.sh/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       binutils
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       procps
Requires:       which
BuildArch:      noarch

%description
Checksec is a bash script to check the properties of executables (like PIE,
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
%autosetup -n %{name}.sh-%{version} -p 1

sed -i 's~^#!%{_bindir}/env bash~#!%{_bindir}/bash~' checksec
sed -i 's/pkg_release=false/pkg_release=true/' checksec

%build
# noop

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -pm 0755 %{name} %{buildroot}%{_bindir}
install -pm 0644 extras/man/%{name}.1 %{buildroot}%{_mandir}/man1

%files
%license LICENSE.txt
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
