#
# spec file for package libbraille
#
# Copyright (c) 2021 SUSE LLC
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


# Python2 is  EOL; let the distro decide if they will want to build py2 support. TW does not
%bcond_without python2
%define libsfx  0-14

Name:           libbraille
Version:        0.19.0
Release:        0
Summary:        Access to Braille Displays and Terminals
License:        LGPL-2.1-only
URL:            https://sourceforge.net/projects/libbraille/files/libbraille/
Source:         http://downloads.sourceforge.net/project/libbraille/libbraille/libbraille-%{version}/libbraille-%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch0:         libbraille-0.19.0-visibility.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
%if %{with python2}
BuildRequires:  pkgconfig(python2)
%endif

%description
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

%package -n libbraille%{libsfx}
Summary:        Access to Braille Displays and Terminals

%description -n libbraille%{libsfx}
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

%package fake%{libsfx}
Summary:        Fake graphical display for libbraille
Requires:       %{name} = %{version}
Supplements:    (%{name} and gtk2)

%description fake%{libsfx}
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

This package contains a fake graphical virtual display.

%package devel
Summary:        Development files for libbraille
Requires:       %{name} = %{version}

%description devel
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

%package -n python2-braille
Summary:        Python bindings for libbraille
Provides:       %{name}-python = %{version}
Obsoletes:      %{name}-python < %{version}
Provides:       python-braille = %{version}-%{release}
Obsoletes:      python-braille < %{version}-%{release}

%description -n python2-braille
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

%prep
%setup -q
%patch0

%build
autoreconf -fi
(cd libltdl; autoreconf -fi)
export CFLAGS="%{optflags} -fno-strict-aliasing "
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
  --disable-static \
  --disable-rpath \
  --enable-hidden-symbols \
  --enable-fake \
  --enable-usb \
%if %{with python2}
  --enable-python \
%endif
  %nil
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libbraille%{libsfx} -p /sbin/ldconfig
%postun -n libbraille%{libsfx}  -p /sbin/ldconfig
%post fake%{libsfx} -p /sbin/ldconfig
%postun fake%{libsfx}  -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%config(noreplace) %{_sysconfdir}/libbraille.conf
%{_bindir}/*
%{_datadir}/libbraille

%files -n libbraille%{libsfx}
%dir %{_libdir}/libbraille
%{_libdir}/libbraille/*.so.*
%exclude %{_libdir}/libbraille/fake-0.so.*
%{_libdir}/*.so.*

%files fake%{libsfx}
%{_libdir}/libbraille/fake-0.so.*

%if %{with python2}
%files -n python2-braille
%{python2_sitearch}/_braille.so*
%{python2_sitelib}/braille.py*
%endif

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/libbraille/*.so

%changelog
