# spec file for package cil
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           cil
Version:        3.5
Release:        0
Summary:        SELinux Common Intermediate Language compiler
License:        BSD-2-Clause
Group:          Development/Languages/Other
URL:            https://github.com/SELinuxProject/selinux
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/se%{name}c-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/se%{name}c-%{version}.tar.gz.asc
Source2:        cil.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libsepol-devel
BuildRequires:  flex
BuildRequires:  xmlto
Obsoletes:      %name-doc  
Provides:       %name-doc  

%description
The SELinux Common Intermediate Language (CIL) is designed to be a language that sits between one or more high level
policy languages (such as the current module language) and the low-level kernel policy representation.

This is a compiler for CIL.

%prep
%setup -q -n secilc-%{version}/

%build
make 

%install
%make_install

%files 
%defattr(-,root,root,-)
%{_bindir}/secilc
%doc %{_mandir}/man8/*
/usr/bin/secil2conf
/usr/bin/secil2tree

%changelog
