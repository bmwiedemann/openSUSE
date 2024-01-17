#
# spec file for package wrk
#
# Copyright (c) 2023 SUSE LLC
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


Name:           wrk
Version:        4.2.0
Release:        0
Summary:        Modern HTTP benchmarking tool
License:        Apache-2.0
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/wg/wrk
Source:         https://github.com/wg/wrk/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         wrk-4.2.0_distrofixes.patch
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(openssl)
ExcludeArch:    aarch64 ppc ppc64 ppc64le

%description
wrk is a modern HTTP benchmarking tool capable of generating significant
load when run on a single multi-core CPU. It combines a multithreaded
design with scalable event notification systems such as epoll and kqueue.

An optional LuaJIT script can perform HTTP request generation, response
processing, and custom reporting. Several example scripts are located in
scripts.

%prep
%autosetup -p1

%build
%make_build OPTFLAGS="%{optflags}" WITH_OPENSSL=%{_prefix}

%install
install -D -m 0755 wrk %{buildroot}%{_bindir}/wrk

%files
%license LICENSE
%doc README.md NOTICE
%doc scripts/
%{_bindir}/wrk

%changelog
