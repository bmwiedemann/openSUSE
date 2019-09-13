#
# spec file for package darts
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


Name:           darts
Version:        0.32
Release:        0
Summary:        Double Array Trie System
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://chasen.org/~taku/software/darts/
Source0:        http://chasen.org/~taku/software/darts/src/darts-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Darts is a simple C++ template library to construct 
Double-Arrays [Aoe 1989]. Double-Arrays are data 
structures to represent Trie. These are faster than 
other Trie implementations.

Darts is used by Chasen.

%prep
%setup -q

%build
%configure
make CXXFLAGS="%{optflags}"

%check
make check

%install
%make_install

%files
%defattr(-, root, root)
%doc AUTHORS COPY* ChangeLog README*
%{_includedir}/*
%{_libexecdir}/%{name}/

%changelog
