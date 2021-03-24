#
# spec file for package crun
#
# Copyright (c) 2021 SUSE LLC
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

Summary:	OCI runtime written in C
Name:		crun
Version:	0.18
Release:	0
Source0:	https://github.com/containers/crun/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	crun-rpmlintrc
License:	GPL-2.0-or-later
URL:		https://github.com/containers/crun
ExclusiveArch:	x86_64 aarch64
# We always run autogen.sh
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	python
BuildRequires:	git-core
BuildRequires:	libcap-devel
BuildRequires:	systemd-devel
BuildRequires:	libyajl-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libselinux-devel
BuildRequires:	python3-libmount
BuildRequires:	libtool
BuildRequires:	go-md2man
BuildRequires:	glibc-devel-static
BuildRequires:	libkrun-devel >= 0.1.4	
%ifnarch %ix86
BuildRequires:	criu-devel >= 3.15
%endif
Requires:	libkrun0 >= 0.1.4

%description
crun is a runtime for running OCI containers. It is built with libkrun support

%prep
%autosetup

%build
./autogen.sh
%configure --disable-silent-rules --with-libkrun CFLAGS='-I /usr/include/libseccomp'
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/lib*

%files
%defattr(-,root,root)
%license COPYING
%doc README.md
%doc SECURITY.md
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
