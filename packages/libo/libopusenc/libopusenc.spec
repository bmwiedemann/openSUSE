#
# spec file for package libopusenc
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


%define sover  0
Name:           libopusenc
Version:        0.2.1
Release:        0
Summary:        A way to encode Ogg Opus files
License:        BSD-3-Clause
Group:          System/Libraries
URL:            http://opus-codec.org/
Source0:        https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(opus) >= 1.1

%description
A library that provides a way to encode Ogg Opus files.

%package  -n libopusenc%{sover}
Summary:        Library package for libopusenc
Group:          System/Libraries

%description -n libopusenc%{sover}
A library that provides a way to encode Ogg Opus files.

%package  devel
Summary:        Development package for libopusenc
Group:          Development/Libraries/Other
Requires:       %{name}%{sover} = %{version}

%description devel
Files for development with libopusenc.

%prep
%autosetup

%build
%configure \
	--disable-static \
	--disable-doc \
	--disable-examples \
	%{nil}
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
# Remove duplicate COPYING etc.
rm -rf %{buildroot}%{_datadir}/doc/libopusenc/

%post -n libopusenc%{sover} -p /sbin/ldconfig
%postun -n libopusenc%{sover} -p /sbin/ldconfig

%files -n libopusenc%{sover}
%license COPYING
%{_libdir}/libopusenc.so.*

%files devel
%doc AUTHORS README.md
%{_includedir}/opus/opusenc.h
%{_libdir}/libopusenc.so
%{_libdir}/pkgconfig/libopusenc.pc

%changelog
