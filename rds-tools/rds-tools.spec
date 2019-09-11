#
# spec file for package rds-tools
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


Name:           rds-tools
Summary:        Support tools for Reliable Datagram Sockets
License:        BSD-3-Clause or GPL-2.0
Group:          System/Console
Version:        2.0.7
Release:        0
Url:            http://oss.oracle.com/projects/rds/
Source:         %{name}-%{version}.tar.gz
Patch0:         rds-tools-external_cflags.patch
Patch1:         rds-tools-uninitialized_var.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
A collection of support tools for the RDS socket API.


%package        devel
Summary:        Development files for Reliable Datagram Sockets
Group:          Development/Libraries/C and C++

%description devel
This package provides the header needed to use the RDS socket API.

%prep
%setup -q
%patch0
%patch1

%build
export CFLAGS="%{optflags} -Iinclude"
autoconf
%configure
make

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%files devel
%defattr(-,root,root)
%{_includedir}/net/rds.h

%changelog
