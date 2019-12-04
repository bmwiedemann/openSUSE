#
# spec file for package libsigrok4DSL
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


Name:           libsigrok4DSL
Version:        1.01
Release:        0
%define sover   1
%define libname %{name}%{sover}
Summary:        API for talking to DSLogic analyzer hardware
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
Url:            https://www.dreamsourcelab.com
Source0:        https://github.com/DreamSourceLab/DSView/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libftdi)
BuildRequires:  pkgconfig(libserialport)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libzip)

%description
libsigrok4DSL is a shared library written in C which provides the basic API
for talking to DSLogic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

%package     -n %{libname}
Summary:        API for talking to DSLogic analyzer hardware
Group:          System/Libraries

%description -n %{libname}
libsigrok4DSL is a shared library written in C which provides the basic API
for talking to DSLogic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

%package        devel
Summary:        Development files for libsigrok4DSL, an API for talking to DSLogic
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
libsigrok4DSL is a shared library written in C which provides the basic API
for talking to DSLogic analyzer hardware and reading/writing the acquired data
into various input/output file formats.

This subpackage contains the headers to make use of the sigrok4DSL shared
libraries.

%prep
%setup -q -n DSView-%{version}

%build
pushd %{name}
autoreconf --force --install
%configure \
        --disable-static

%make_build
popd

%install
pushd %{name}
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# fix executable docs
chmod 644 README
popd

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.%{sover}*

%files devel
%license %{name}/COPYING
%doc %{name}/README
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
