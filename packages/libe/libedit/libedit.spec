#
# spec file for package libedit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define pkg_version 20190324-3.1
%define soname 0
%define library_name libedit%{soname}
Name:           libedit
Version:        3.1.snap20180525
Release:        0
Summary:        Command Line Editing and History Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.thrysoee.dk/editline/
Source:         http://thrysoee.dk/editline/libedit-%{pkg_version}.tar.gz
Source1:        README.SUSE
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM libedit-20180525-manpage-conflicts.patch
Patch0:         libedit-20180525-manpage-conflicts.patch
#BuildRequires:  gcc-c++
# For patch0
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)

%description
libedit is a command line editing and history library. It is designed
to be used by interactive programs that allow the user to type commands
at a terminal prompt.

%package -n %{library_name}
Summary:        Command Line Editing and History Library
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}

%description -n %{library_name}
libedit is a command line editing and history library. It is designed
to be used by interactive programs that allow the user to type commands
at a terminal prompt.

%package -n libedit-devel
Summary:        Development files for libedit
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}
Requires:       glibc-devel
Provides:       %{library_name}-devel = %{version}-%{release}

%description -n libedit-devel
libedit is a command line editing and history library. It is designed
to be used by interactive programs that allow the user to type commands
at a terminal prompt.

This package holds the development files for libedit.

%prep
%setup -q -n %{name}-%{pkg_version}
cp %{SOURCE1} .
%patch0 -p1

%build
%configure \
  --disable-static \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files -n %{library_name}
%{_libdir}/libedit.so.%{soname}
%{_libdir}/libedit.so.%{soname}.*
%{_mandir}/man5/editrc.5%{?ext_man}
%license COPYING
%doc ChangeLog

%files -n libedit-devel
%{_libdir}/libedit.so
%{_includedir}/histedit.h
%{_includedir}/editline/
%{_mandir}/man3/*.3%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}
%{_libdir}/pkgconfig/libedit.pc
%doc examples/*c THANKS README.SUSE

%changelog
