#
# spec file for package libbraille
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libbraille
Version:        0.19.0
Release:        0
Summary:        Access to Braille displays and terminals
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/projects/libbraille/files/libbraille/
Source:         http://downloads.sourceforge.net/project/libbraille/libbraille/libbraille-%{version}/libbraille-%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch0:         libbraille-0.19.0-visibility.patch
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  python-devel
BuildRequires:  swig

%description
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

%package fake
Summary:        Fake graphical display for libbraille
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:gtk2)

%description fake
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

This package contains a fake graphical virtual display.

%package devel
Summary:        Development files for libbraille
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

%package -n python-braille
Summary:        Python bindings for libbraille
Group:          Development/Libraries/Python
Provides:       %{name}-python = %{version}
Obsoletes:      %{name}-python < %{version}

%description -n python-braille
Libbraille is a computer shared library which makes it possible to
develop for Braille displays. It provides an API to
write text on the display, directly draw dots, or get the value of
keys pressed on the Braille keyboard.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
(cd libltdl; autoreconf -fi)
CFLAGS="%{optflags} -fno-strict-aliasing"
CXXFLAGS="%{optflags} -fno-strict-aliasing"
%if 0%{?suse_version} > 1000
CFLAGS="$CFLAGS -fstack-protector"
CXXFLAGS="$CXXFLAGS -fstack-protector"
%endif

export CFLAGS
export CXXFLAGS

%configure --disable-static --disable-rpath \
        --enable-hidden-symbols \
        --enable-fake \
        --enable-usb \
        --enable-python
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%license COPYING
%doc AUTHORS ChangeLog README TODO
%config(noreplace) %{_sysconfdir}/libbraille.conf
%{_bindir}/*
%{_libdir}/*.so.*
%dir %{_libdir}/libbraille
%{_libdir}/libbraille/*.so.*
%{_datadir}/libbraille
%exclude %{_libdir}/libbraille/fake-0.so.*

%files fake
%defattr(-, root, root)
%{_libdir}/libbraille/fake-0.so.*

%files -n python-braille
%defattr(-, root, root)
%{python_sitearch}/_braille.so*
%{python_sitelib}/braille.py*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/libbraille/*.so

%changelog
