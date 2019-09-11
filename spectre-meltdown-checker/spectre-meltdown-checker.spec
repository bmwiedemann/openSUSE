#
# spec file for package spectre-meltdown-checker
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           spectre-meltdown-checker
Version:        0.42
Release:        0
Summary:        Spectre & Meltdown Vulnerability Checker
License:        GPL-3.0-only
Group:          Productivity/Security
Url:            https://github.com/speed47/spectre-meltdown-checker
Source:         https://github.com/speed47/spectre-meltdown-checker/archive/v%version.tar.gz
ExclusiveArch:  %ix86 x86_64

%description
A shell script to tell if your Linux installation is vulnerable
against the three "speculative execution" CVEs that were made public
in early 2018.

Without options, the script inspects the currently running kernel.
Alternatively, a kernel image can be specify on the command line to
analyze a non-running kernel.

The script tries to detect mitigations, including backported
non-vanilla patches, regardless of the advertised kernel version
number.

%prep
%setup -q

%build

%install
mkdir -p %buildroot/usr/bin
install -m 0755 spectre-meltdown-checker.sh %buildroot/usr/bin/

%check
exec bash -n spectre-meltdown-checker.sh

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
