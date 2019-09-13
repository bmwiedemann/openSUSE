#
# spec file for package nsjail
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


Name:           nsjail
Version:        2.8
Release:        0
Summary:        A light-weight process isolation tool
License:        Apache-2.0
Group:          System/GUI/Other
ExclusiveArch:  x86_64
URL:            http://nsjail.com
Source0:        nsjail-%{version}.tar.gz
Source1:        kafel.tar.gz
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glibc-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  protobuf-devel

%description
A light-weight process isolation tool, making use of Linux namespaces and
seccomp-bpf syscall filters (with help of the kafel bpf language) 

%prep
%setup -qa1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
make %{?_smp_mflags} 

%install
mkdir -p %{buildroot}/%{_bindir}/
cp nsjail %{buildroot}/%{_bindir}/

%files 
%defattr(-,root,root)
%{_bindir}/nsjail

%changelog
