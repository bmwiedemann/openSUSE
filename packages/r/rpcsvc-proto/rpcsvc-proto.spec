#
# spec file for package rpcsvc-proto
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rpcsvc-proto
Version:        1.4
Release:        0
Summary:        RPC protocol definitions
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://github.com/thkukuk/rpcsvc-proto
Source:         %{name}-%{version}.tar.xz

%description
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package devel
Summary:        RPC protocol definitions
Group:          Development/Libraries/C and C++

%description devel
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package -n rpcgen
Summary:        RPC protocol compiler
Group:          Development/Tools/Other
Provides:       glibc-devel:%{_bindir}/rpcgen

%description -n rpcgen
rpcgen is a tool that generates C code to implement an RPC protocol.
The input to rpcgen is a language similar to C known as RPC Language
(Remote Procedure Call Language).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files devel
%license COPYING
%dir %{_includedir}/rpcsvc
%{_includedir}/rpcsvc/*

%files -n rpcgen
%license COPYING
%{_bindir}/rpcgen
%{_mandir}/man1/rpcgen.1*

%changelog
