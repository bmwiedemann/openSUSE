#
# spec file for package libsigrok
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


Name:           libsigrok
Version:        0.5.2
Release:        0
%define libname %{name}4
%define libcxxname libsigrokcxx4
Summary:        API for talking to logic analyzer hardware
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            http://sigrok.org
Source0:        http://sigrok.org/download/source/libsigrok/%{name}-%{version}.tar.gz
Source1:        sigrok-mime.xml
Patch0:         0001-Use-pkg-config-for-rpc-library-detection.patch
Patch1:         LTO-linking-fix.patch
Patch2:         0001-tests-strutil-use-ck_assert.patch
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bluez-devel
BuildRequires:  check-devel >= 0.9.4
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  hicolor-icon-theme
BuildRequires:  libftdi1-devel >= 1.0
BuildRequires:  libhidapi-devel
BuildRequires:  libserialport-devel >= 0.1.1
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libusb-1_0-devel
BuildRequires:  libzip-devel >= 0.10
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(libudev)

%description
libsigrok is a shared library written in C which provides the basic API
for talking to logic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

%package     -n %{libname}
Summary:        API for talking to logic analyzer hardware
Group:          System/Libraries
Requires:       %{name}-data >= %{version}
Recommends:     sigrok-firmware-fx2lafw

%description -n %{libname}
libsigrok is a shared library written in C which provides the basic API
for talking to logic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

%package     -n %{libcxxname}
Summary:        API for talking to logic analyzer hardware
Group:          System/Libraries
Requires:       %{libname} >= %{version}
Requires:       %{name}-data >= %{version}

%description -n %{libcxxname}
libsigrok is a shared library written in C which provides the basic API
for talking to logic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

%package        data
Summary:        Data files for libsigrok
Group:          Productivity/Scientific/Electronics
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires(post):    shared-mime-info
Requires(postun):  shared-mime-info

%description    data
libsigrok is a shared library written in C which provides the basic API
for talking to logic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

%package        devel
Summary:        Development files for libsigrok, an API for talking to logic analyzer hardware
Group:          Development/Libraries/C and C++
Requires:       %{libcxxname} = %{version}
Requires:       %{libname} = %{version}

%description    devel
libsigrok is a shared library written in C which provides the basic API
for talking to logic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

This subpackage contains the headers to make use of the sigrok shared
libraries.

%prep
%autosetup -p1
# avoid autoconf/automake rerun
touch aclocal.m4 Makefile.in configure

%build
%configure \
        --disable-static \
        --enable-fx2lafw
%make_build

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%define mm_ignore ENV{ID_MM_DEVICE_IGNORE}="1"
install -d -m 755 %{buildroot}%{_udevrulesdir}
install -m 644 contrib/60-libsigrok.rules %{buildroot}%{_udevrulesdir}
install -m 644 contrib/61-libsigrok-uaccess.rules %{buildroot}%{_udevrulesdir}
sed -i '/ID_SIGROK/ p; s/TAG.*/%{mm_ignore}/' %{buildroot}%{_udevrulesdir}/61-libsigrok-uaccess.rules

install -m 644 -D %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/vnd.sigrok.session.xml
install -m 644 -D contrib/libsigrok.png %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/libsigrok.png
install -m 644 -D contrib/libsigrok.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/libsigrok.svg

%check
%ifnarch %{ix86}
# Fails on i586, https://sigrok.org/bugzilla/show_bug.cgi?id=1475
make check
%endif

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libcxxname} -p /sbin/ldconfig

%postun -n %{libcxxname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*
%exclude %{_libdir}/*cxx.so.*

%files -n %{libcxxname}
%{_libdir}/*cxx.so.*

%files data
%license COPYING
%{_udevrulesdir}/*
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*/mimetypes/libsigrok*

%files devel
%doc README HACKING NEWS
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
