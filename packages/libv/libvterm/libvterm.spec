#
# spec file for package libvterm
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


%define sover 0
%{?!make_build:%define make_build %{__make} %{_make_output_sync} %{?_smp_mflags} %{_make_verbose}}
%{?!_make_output_sync:%define _make_output_sync %(! %{__make} --version -O >/dev/null 2>&1 || echo -O)}
%{?!_make_verbose:%define _make_verbose V=1 VERBOSE=1}

Name:           libvterm
Version:        0.3.1
Release:        0
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://launchpad.net/libvterm
Source:         https://launchpad.net/libvterm/trunk/v0.3/+download/libvterm-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
An abstract C99 library which implements a VT220 or xterm-like terminal
emulator.

%package -n %{name}%{sover}
Summary:        Shared library package of libvterm
Group:          System/Libraries

%description -n %{name}%{sover}
An abstract C99 library which implements a VT220 or xterm-like
terminal emulator. It does not use any particular graphics toolkit or
output system. Instead, it invokes callback function pointers that
its embedding program should provide it to draw on its behalf.

%package devel
Summary:        Development files of libvterm
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
This package contains the development files of libvterm.

%package tools
Summary:        Tools for libvterm
Group:          System/Console

%description tools
This package contains tools for libvterm.

%prep
%setup -q

%build
%make_build PREFIX=%{_prefix} \
     LIBDIR=%{_libdir} \
     CFLAGS="%{optflags}"

%install
make PREFIX=%{_prefix} \
     LIBDIR=%{_libdir} \
     DESTDIR=%{buildroot} \
     install

# Remove libtool files.
find %{buildroot} -type f -name "*.la" -delete -print

# Remove static library file.
rm -vf %{buildroot}%{_libdir}/%{name}.a

%check
make test

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/vterm*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/vterm.pc

%files tools
%{_bindir}/unterm
%{_bindir}/vterm-ctrl
%{_bindir}/vterm-dump

%changelog
