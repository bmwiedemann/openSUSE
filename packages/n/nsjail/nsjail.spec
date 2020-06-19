#
# spec file for package nsjail
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


Name:           nsjail
Version:        2.9
Release:        0
Summary:        A light-weight process isolation tool
License:        Apache-2.0
Group:          System/GUI/Other
URL:            https://nsjail.com
Source0:        nsjail-%{version}.tar.gz
Source1:        kafel.tar.gz
Patch0:         remove_werror.patch
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glibc-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
ExclusiveArch:  x86_64

%description
A light-weight process isolation tool, making use of Linux namespaces and
seccomp-bpf syscall filters (with help of the kafel bpf language)

%prep
%setup -qa1
%patch0 -p1

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}/
cp nsjail %{buildroot}/%{_bindir}/

%files
%license LICENSE
%{_bindir}/nsjail

%changelog
