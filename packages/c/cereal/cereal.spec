#
# spec file for package cereal
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Christoph Junghans
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


Name:           cereal
Version:        1.2.2
Release:        0
Summary:        A header-only C++11 serialization library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://uscilab.github.io/cereal/
Source0:        https://github.com/USCiLab/cereal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/USCiLab/cereal/issues/338
# PATCH-FIX-UPSTREAM - 8b8f5814e292e03bb5b07333a0e634ef0481c85b.patch - fix unstable test
Patch0:         https://github.com/USCiLab/cereal/commit/8b8f5814e292e03bb5b07333a0e634ef0481c85b.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++ >= 4.8
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake

%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary 
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast, 
light-weight, and easy to extend - it has no external dependencies and can be 
easily bundled with other code or used standalone.

%package devel
Summary:        Development headers and libraries for cereal library
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description devel
cereal is a header-only C++11 serialization library. cereal takes arbitrary 
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast, 
light-weight, and easy to extend - it has no external dependencies and can be 
easily bundled with other code or used standalone.

This package contains development headers and libraries for the cereal library

%prep
%setup -q
%patch0 -p1

%build
%{cmake} -DSKIP_PORTABILITY_TEST=ON -DWITH_WERROR=OFF
make %{?_smp_mflags}

%install
make -C build install DESTDIR=%{buildroot}

%check
make -C build test

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_includedir}/cereal
%{_datadir}/cmake/cereal

%changelog
