#
# spec file for package nsjail
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           nsjail
Version:        3.5
Release:        0
Summary:        A light-weight process isolation tool
License:        Apache-2.0
Group:          System/GUI/Other
URL:            https://nsjail.com
Source0:        nsjail-%{version}.tar.gz
Source1:        kafel.tar.xz
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glibc-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  pkgconfig
ExclusiveArch:  x86_64
# Protobuf 25 has added to SLE15 in SP4 Update
%if 0%{?suse_version} > 1500 || (0%{?suse_version} == 1500 && 0%{?sle_version} > 150300)
BuildRequires:  protobuf21-devel
%else
BuildRequires:  protobuf-devel
%endif

%description
A light-weight process isolation tool, making use of Linux namespaces and
seccomp-bpf syscall filters (with help of the kafel bpf language)

%prep
%setup -qb0
pwd
%setup -qa1
pwd

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}/
cp nsjail %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
install -m 644 configs/*.cfg %{buildroot}/%{_sysconfdir}/%{name}

%files
%license LICENSE
%{_bindir}/nsjail
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*

%changelog
