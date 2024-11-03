#
# spec file for package neko
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           neko
Version:        2.4.0
Release:        0
Summary:        A cross-platform lightweight virtual machine and language
License:        MIT
Group:          Development/Languages/Other
Url:            https://nekovm.org
Source0:        https://github.com/HaxeFoundation/neko/archive/v2-4-0/neko-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  git
BuildRequires:  apache2-devel
BuildRequires:  gc-devel
BuildRequires:  gtk3-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  pcre2-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel-static
BuildRequires:  mbedtls-devel >= 3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libneko2 = %{version}
Provides:       nekovm = %version
Obsoletes:      nekovm < %version

%description
Neko VM is a virtual machine for the Neko language. Neko is a
high-level dynamically typed programming language. It can be used as
an embedded scripting language.

%package devel
Summary:        Development files for the Neko virtual machine
License:        MIT
Group:          Development/Languages/Other
Requires:       libneko2 = %{version}
Provides:       nekovm-devel = %version
Obsoletes:      nekovm-devel < %version

%description devel
Development files and headers for the Neko virtual machine.

%package -n libneko2
Summary:        Neko virtual machine shared library
License:        MIT
Group:          System/Libraries

%description -n libneko2
Shared library for the Neko virtual machine.

%package mysql
Summary:        Neko virtual machine MySQL library
License:        GPL-2.0+
Group:          System/Libraries
Requires:       %{name} = %{version}
Provides:       nekovm-mysql = %version
Obsoletes:      nekovm-mysql < %version

%description mysql
MySQL library for the Neko virtual machine.

%prep
%setup -q -n neko-2-4-0

%build
%define __builder ninja

# modify CMAKE_C_FLAGS for strict-aliasing-punning
# https://github.com/HaxeFoundation/neko/issues/175
%cmake \
    -G Ninja \
    -DCMAKE_C_FLAGS:STRING="%optflags -fno-strict-aliasing" \
    -DWITH_APACHE=OFF \
    -DRELOCATABLE=OFF \
    -DRUN_LDCONFIG=OFF
# make_jobs macro does not use ninja in openSUSE_13.2 / Leap_42.1
%make_jobs || %__builder -v %{?_smp_mflags}

%check

# ctest macro has not been defined in openSUSE_13.1
%{!?ctest: %define ctest ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}}
%ctest

%install
# cmake_install does not use ninja in openSUSE_13.2 / Leap_42.1
%cmake_install || DESTDIR=%{buildroot} %__builder install -C build

%post -n libneko2 -p /sbin/ldconfig

%postun -n libneko2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%dir %{_libdir}/neko
%{_libdir}/neko/regexp.ndll
%{_libdir}/neko/sqlite.ndll
%{_libdir}/neko/std.ndll
%{_libdir}/neko/ui.ndll
%{_libdir}/neko/zlib.ndll
%{_libdir}/neko/ssl.ndll
%{_libdir}/neko/nekoml.std
%doc LICENSE CHANGES

%files mysql
%defattr(-,root,root)
%{_libdir}/neko/mysql.ndll
%{_libdir}/neko/mysql5.ndll
%doc LICENSE CHANGES

%files -n libneko2
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc LICENSE CHANGES

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%doc LICENSE CHANGES

%changelog
