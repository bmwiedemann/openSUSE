#
# spec file for package subfinder
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           subfinder
Version:        2.9.0
Release:        0
Summary:        Fast passive subdomain enumeration tool
License:        MIT
URL:            https://github.com/projectdiscovery/subfinder
Source0:        https://github.com/projectdiscovery/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zstd
Patch1:         disable-version-check.patch
BuildRequires:  help2man
BuildRequires:  udev
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.24

%description
subfinder is a subdomain discovery tool that returns valid subdomains for websites, using passive online sources.
It has a simple, modular architecture and is optimized for speed.
subfinder is built for doing one thing only - passive subdomain enumeration, and it does that very well.
We have made it to comply with all the used passive source licenses and usage restrictions.
The passive model guarantees speed and stealthiness that can be leveraged by both penetration testers and bug bounty hunters alike.

%prep
%autosetup -p1 -a1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}
help2man -s8 -N ./subfinder --version-string=%{version} > subfinder.8

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 644 -D -v %{name}.8 %{buildroot}%{_datadir}/man/man8/%{name}.8

%check
./subfinder -h

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/man/man8/%{name}.8%{?ext_man}

%changelog
