#
# spec file for package unixcw
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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

%define soname 8
Name:           unixcw
Version:        3.6.1
Release:        0
Summary:        Libraries and programs for CW
License:        GPL-2.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://unixcw.sourceforge.net/
Source:         https://sourceforge.net/projects/unixcw/files/%{name}-%{version}.tar.gz
Patch0:         unixcw-ncurses.diff
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(ncurses)

%description
Unixcw is a project providing libcw library and a set of programs using the
library: cw, cwgen, cwcp and xcwcp. The programs are intended for people who
want to learn receiving and sending Morse code. unixcw is developed and tested
on GNU/Linux system.

%package -n libcw%{soname}
Summary:        Libraries for CW programs
Group:          Development/Libraries/Other

%description -n libcw%{soname}
Unixcw is a project providing libcw library and a set of programs using the
library: cw, cwgen, cwcp and xcwcp. The programs are intended for people who
want to learn receiving and sending Morse code. unixcw is developed and tested
on GNU/Linux system.

This package contains the shared library.

%package devel
Summary:        Libraries and programs for CW development
Group:          Development/Libraries/Other
Requires:       libcw%{soname} = %{version}

%description devel
Unixcw is a project providing libcw library and a set of programs using the
library: cw, cwgen, cwcp and xcwcp. The programs are intended for people who
want to learn receiving and sending Morse code. unixcw is developed and tested
on GNU/Linux system.

This package contains the file needed for building with %{name}.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%if 0%{?suse_version} >= 1600
%check
%make_build check
%endif

%ldconfig_scriptlets -n libcw%{soname}

%files
%license COPYING
%{_bindir}/cw
%{_bindir}/cwcp
%{_bindir}/cwgen
%{_bindir}/xcwcp
%{_mandir}/man1/*1%{?ext_man}
%{_mandir}/man7/*7%{?ext_man}

%files -n libcw%{soname}
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libcw.so.%{soname}{,.*}
%{_mandir}/man3/libcw.3%{?ext_man}

%files devel
%license COPYING
%{_libdir}/libcw*.so
%{_libdir}/pkgconfig/*
%{_includedir}/libcw.h
%{_includedir}/libcw2.h
%{_includedir}/libcw_debug.h

%changelog
