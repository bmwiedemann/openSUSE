#
# spec file for package libabigail
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libabigail
%define lname   libabigail0
Version:        1.0~rc6+git185
Release:        0
Summary:        Application Binary Interface Generic Analysis and Instrumentation Library
License:        GPL-3.0+ and LGPL-2.0+ and LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://sourceware.org/libabigail/

Source:         %name-%version.tar.xz
Patch1:         no-tests.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.63
BuildRequires:  automake >= 1.11.1
BuildRequires:  dpkg
BuildRequires:  gcc-c++ >= 4.7
BuildRequires:  libdw-devel >= 0.160
BuildRequires:  libebl-devel
BuildRequires:  libtool >= 2.2
BuildRequires:  libzip-devel
BuildRequires:  makeinfo
BuildRequires:  pkg-config
BuildRequires:  python-sphinx
BuildRequires:  xz
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.22
BuildRequires:  pkgconfig(libzip) >= 0.10
PreReq:         %install_info_prereq

%description
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program.

%package -n %lname
Summary:        Application Binary Interface Generic Analysis and Instrumentation Library
License:        LGPL-3.0+
Group:          System/Libraries

%description -n %lname
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program. The
library provides a way to compare two ABI corpuses, provide detailed
information about their differences, and help build tools to infer
interesting conclusions about these differences.

%package devel
Summary:        Development files for the ABI-relevant artifact library
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program. The
library provides a way to compare two ABI corpuses, provide detailed
information about their differences.

This subpackage contains the files needed to build programs with ABIGAIL.

%package tools
Summary:        Utilities to inspect ABI-relevant artifacts
License:        LGPL-3.0+
Group:          Development/Tools/Other

%description tools
ABIGAIL constructs, manipulates, (de-)serializes ABI-relevant
artifacts, such as types, variable, fonctions and declarations
(collectively, the ABI corpus) of a given library or program.

This subpackage contains the ABIGAIL utilities allowing to infer
interesting conclusions about these differences.

%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fiv
%configure --includedir="%_includedir/%name" --docdir="%_docdir/%name" \
	--disable-static --enable-cxx11 --disable-silent-rules
make %{?_smp_mflags}
pushd doc/manuals
make man info
popd

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

pushd doc/manuals
make DESTDIR=%buildroot install-man-and-info-doc
popd

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%post tools %install_info abigail
%postun tools %install_info abigail

%files -n %lname
%defattr(-,root,root)
%_libdir/libabigail.so.0*

%files devel
%defattr(-,root,root)
%_includedir/%name/
%_libdir/libabigail.so
%_libdir/pkgconfig/*.pc
%_datadir/aclocal/
%_mandir/man7/libabigail.7.gz

%files tools
%defattr(-,root,root)
%doc COPYING*
%_bindir/abi*
%_bindir/kmidiff
%_mandir/man1/abi*.1*
%_infodir/abigail.info.gz
%_libdir/%name/

%changelog
