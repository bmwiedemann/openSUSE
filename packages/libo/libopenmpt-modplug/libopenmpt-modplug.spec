#
# spec file for package libopenmpt-modplug
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
%define libname libopenmpt_modplug

Name:           libopenmpt-modplug
Version:        0.8.9.0
Release:        0
Summary:        A compatibility Layer For libmodplug
License:        BSD-3-Clause
URL:            https://lib.openmpt.org/libopenmpt/
Source0:        https://lib.openmpt.org/files/libopenmpt-modplug/%{name}-%{version}-openmpt1.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig

%description
libopenmpt is a cross-platform C++ and C library to decode tracked
music files (modules) into a raw PCM audio stream. openmpt123 is a
cross-platform command-line or terminal based module file player.

%package    -n  %{libname}%{sover}
Summary:        Openmpt's libmodplug

%description    -n %{libname}%{sover}
The ModPlug mod file playing library (emulated via libopenmpt).

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname}%{sover}   = %{version}
Requires:       pkgconfig(libopenmpt)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}-openmpt1

# WARNING:
#--enable-libmodplug       Enable libmodplug replacement library based on
#                          libopenmpt. WARNING: This will replace your current
#                          libmodplug installation. CAUTION: The emulation of
#                          the libmodplug interface is not complete as
#                          libmodplug exposes lots of internal implementation
#                          details. If any of those is used by an application,
#                          the emulation via libopenmpt will fail and/or crash.
%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -rf  %{buildroot}%{_datadir}
find %{buildroot} -type f -name "*.la" -delete -print
mkdir %{buildroot}%{_libdir}/pkgconfig
cp -v %{libname}.pc %{buildroot}%{_libdir}/pkgconfig/

%post -n %{libname}%{sover}   -p /sbin/ldconfig
%postun -n %{libname}%{sover}   -p /sbin/ldconfig

%files -n %{libname}%{sover}
%license LICENSE
  %{_libdir}/%{libname}.so.%{sover}*

%files devel
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
