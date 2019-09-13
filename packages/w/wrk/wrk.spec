#
# spec file for package wrk
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wrk
Version:        4.0.2
Release:        0
Summary:        Modern HTTP benchmarking tool
License:        Apache-2.0
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/wg/wrk
Source:         https://github.com/wg/wrk/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         wrk-3.1.2_distrofixes.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig
#BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openssl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    aarch64 ppc ppc64 ppc64le

%description
wrk is a modern HTTP benchmarking tool capable of generating significant
load when run on a single multi-core CPU. It combines a multithreaded
design with scalable event notification systems such as epoll and kqueue.

An optional LuaJIT script can perform HTTP request generation, response
processing, and custom reporting. Several example scripts are located in
scripts.

%prep
%setup -q
%patch0

%build
# current luajit in TW seems to be broken
# sed -i 's|luajit-2.0|luajit-5_1-2.0|g' src/*
# make %{?_smp_mflags} OPTFLAGS="%{optflags}" WITH_OPENSSL=/usr WITH_LUAJIT=/usr
make %{?_smp_mflags} OPTFLAGS="%{optflags}" WITH_OPENSSL=%{_prefix}

%install
install -D -m 0755 wrk %{buildroot}%{_bindir}/wrk

%files
%defattr(-,root,root)
%doc LICENSE README NOTICE
%doc scripts/
%{_bindir}/wrk

%changelog
