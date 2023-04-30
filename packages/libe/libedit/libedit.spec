#
# spec file for package libedit
#
# Copyright (c) 2023 SUSE LLC
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


%define pkg_version 20210910-3.1
%define sover 0
Name:           libedit
Version:        20210910.3.1
Release:        0
Summary:        Command Line Editing and History Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.thrysoee.dk/editline/
Source0:        https://www.thrysoee.dk/editline/libedit-%{pkg_version}.tar.gz
Source1:        README.SUSE
Source2:        baselibs.conf
Patch0:         libedit-20180525-manpage-conflicts.patch
Patch1:         libedit-hidden-symbols.patch
# For patch0
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)

%description
libedit is a command line editing and history library. It is designed
to be used by interactive programs that allow the user to type commands
at a terminal prompt.

%package -n libedit%{sover}
Summary:        Command Line Editing and History Library
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}

%description -n libedit%{sover}
libedit is a command line editing and history library. It is designed
to be used by interactive programs that allow the user to type commands
at a terminal prompt.

%package -n libedit-devel
Summary:        Development files for libedit
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libedit%{sover} = %{version}
Provides:       libedit%{sover}-devel = %{version}-%{release}

%description -n libedit-devel
libedit is a command line editing and history library. It is designed
to be used by interactive programs that allow the user to type commands
at a terminal prompt.

This package holds the development files for libedit.

%prep
%autosetup -p1 -n %{name}-%{pkg_version}
cp %{SOURCE1} .

%build
autoreconf -fiv
%configure \
  --disable-static \
  --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libedit%{sover} -p /sbin/ldconfig
%postun -n libedit%{sover} -p /sbin/ldconfig

%files -n libedit%{sover}
%{_libdir}/libedit.so.%{sover}
%{_libdir}/libedit.so.%{sover}.*
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
