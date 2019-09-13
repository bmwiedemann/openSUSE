#
# spec file for package tinygettext
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


Name:           tinygettext
Version:        0.1.1469459657.bf66a57
Release:        0
Summary:        A simple gettext replacement
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            https://github.com/tinygettext/tinygettext
Source:         %{name}-%{version}.tar.xz
# PATCH-FEATURE-UPSTREAM create-lib-with-so-ver.patch -- Create library with so version
Patch0:         create-lib-with-so-ver.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
tinygettext is a minimal replacement for gettext written in C++.
It can read .po files directly and doesn't need .mo files generated from .po.
It also can read the .po files from arbitary locations,
so it's better suited for non-Unix systems and situations in which one wants
to store or distribute .po files separately from the software itself.

%package -n lib%{name}0
Summary:        Shared library of %{name}
Group:          System/Libraries

%description -n lib%{name}0
This package contains the shared library of %{name}

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}0 = %{version}

%description devel
This package contains the development files, like headers etc, for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%check
# Copy compiled tests into test dir
cp -l build/test/* test
cd test
# Run test with LD path (since they link against the new library but have no RPATH).
LD_LIBRARY_PATH=../build ./test.sh

%install
%cmake_install

%post -n lib%{name}0 -p /sbin/ldconfig
%postun -n lib%{name}0 -p /sbin/ldconfig

%files -n lib%{name}0
%defattr(-,root,root)
%doc README.md LICENSE.md
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%changelog
