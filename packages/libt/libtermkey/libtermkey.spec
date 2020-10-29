#
# spec file for package libtermkey
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 1
Name:           libtermkey
Version:        0.22
Release:        0
Summary:        Library for processing of keyboard entry from terminal-based programs
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.leonerd.org.uk/code/libtermkey/
Source:         http://www.leonerd.org.uk/code/libtermkey/libtermkey-%{version}.tar.gz
Patch0:         fix-syntax.patch
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig

%description
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognise special keys, UTF-8
combining, and so on, with a simple interface.

%package -n %{name}%{sover}
Summary:        Library for processing of keyboard entry from terminal-based programs
Group:          System/Libraries

%description -n %{name}%{sover}
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognise special keys, UTF-8
combining, and so on, with a simple interface.

%package devel
Summary:        Development files for libtermkey, a keyboard entry processing library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       ncurses-devel
Requires:       pkgconfig

%description devel
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognise special keys, UTF-8
combining, and so on, with a simple interface.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} \
    CFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    LIBDIR="%{_libdir}" \
    INCDIR="%{_includedir}" \
    MANDIR="%{_mandir}"

%install
make \
    CFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    LIBDIR="%{_libdir}" \
    INCDIR="%{_includedir}" \
    MANDIR="%{_mandir}" \
    DESTDIR=%{buildroot} \
    install

# Remove unneeded files.
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a"  -delete -print

%post   -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%license LICENSE
%{_libdir}/libtermkey.so.%{sover}
%{_libdir}/libtermkey.so.%{sover}.*

%files devel
%defattr(-,root,root)
%{_includedir}/termkey.h
%{_libdir}/libtermkey.so
%{_libdir}/pkgconfig/termkey.pc
%{_mandir}/man3/termkey*.3%{ext_man}
%{_mandir}/man7/termkey.*

%changelog
