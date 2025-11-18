#
# spec file for package ptcpdump
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


Name:           ptcpdump
Version:        0.37.0
Release:        0
Summary:        Process-aware, eBPF-based tcpdump
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            https://github.com/mozillazg/ptcpdump
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz

BuildRequires:  clang >= 15
BuildRequires:  go
BuildRequires:  golang >= 1.23
BuildRequires:  golang-packaging
BuildRequires:  llvm >= 15
BuildRequires:  pkgconfig(libpcap) >= 1.10
%requires_ge libpcap1

%{go_provides}

%description
ptcpdump is an eBPF-based implementation of tcpdump that includes an additional
feature: it adds process information as comments for each packet when available

%prep
%autosetup -p1 -a1

%build
%make_build build-bpf VERSION=%{version}
%make_build build-dynamic-link VERSION=%{version}

%install
install -D -s -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/ptcpdump

%changelog
