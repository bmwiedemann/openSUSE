#
# spec file for package lmdbxx
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


Name:           lmdbxx
Version:        1.0.0
Release:        0
Summary:        C++ wrapper for the LMDB embedded B+ tree database library
License:        PDDL-1.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/hoytech/lmdbxx
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Header-only %{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       lmdb-devel
Provides:       %{name}-static = %{version}

%description devel
Header-only %{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build. Header-only library.

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 -p lmdb++.h %{buildroot}%{_includedir}

%files devel
%doc README.md TODO FUNCTIONS.rst AUTHORS
%license UNLICENSE
%{_includedir}/lmdb++.h

%changelog
