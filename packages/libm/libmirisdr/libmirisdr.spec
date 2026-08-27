#
# spec file for package libmirisdr
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2012-2014 Wojciech Kazubski, wk@ire.pw.edu.pl
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


# The fork numbers its release tags and its library major version
# independently: release 2.0.0 ships SONAME libmirisdr.so.4
%define sover   4
%define libname libmirisdr%{sover}
Name:           libmirisdr
Version:        2.0.0
Release:        0
Summary:        Support programs for Mirics MSi2500 based SDR receivers
# Legal-Review-Notice: every source file compiled into the shared library
# and the command line tools carries a GPL-2.0-or-later header, and COPYING
# is the GPL-2.0 text, so the whole package is tagged GPL-2.0-or-later -
# the same way other distributions declare it.  Two files disagree with
# that in their own headers and are noted here so the finding is not
# re-derived every time: the shipped udev rules file carries a
# GPL-3.0-or-later header, and so does the CMake build system, which is
# build tooling and is not shipped in any binary package at all.
License:        GPL-2.0-or-later
URL:            https://github.com/f4exb/libmirisdr-4
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/libmirisdr-4-%{version}.tar.gz
Patch0:         libmirisdr-release-version.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Programs that control a Mirics MSi2500 based DVB dongle in raw mode, so
that it can be used as an SDR receiver.

%package -n %{libname}
Summary:        SDR driver for Mirics MSi2500 based receivers
Requires:       mirisdr-udev
Provides:       %{name} = %{version}-%{release}
# The upstream fork bumped the SONAME from libmirisdr.so.0 to libmirisdr.so.4
Provides:       libmirisdr0 = %{version}-%{release}
Obsoletes:      libmirisdr0 < %{version}-%{release}

%description -n %{libname}
Library to run a Mirics MSi2500 based DVB dongle as an SDR receiver.

%package -n mirisdr
Summary:        Support programs for Mirics MSi2500 based SDR receivers

%description -n mirisdr
Programs that control a Mirics MSi2500 based DVB dongle in raw mode, so
that it can be used as an SDR receiver.

%package devel
Summary:        Development files for libmirisdr
Requires:       %{libname} = %{version}-%{release}

%description devel
Library headers and other development files for the mirisdr driver.

%package -n mirisdr-udev
Summary:        Udev rules for Mirics MSi2500 based DVB dongles
BuildArch:      noarch

%description -n mirisdr-udev
Udev rules for Mirics MSi2500 based DVB dongles.

%prep
%autosetup -p1 -n libmirisdr-4-%{version}

%build
# Upstream hardcodes an install RPATH of %%{_prefix}/lib
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install
# Only the shared library is shipped
rm %{buildroot}%{_libdir}/libmirisdr.a

install -D -p -m 0644 mirisdr.rules %{buildroot}%{_udevrulesdir}/10-mirisdr.rules

%ldconfig_scriptlets -n %{libname}

%files -n mirisdr
%license COPYING
%doc README.md
%{_bindir}/miri_fm
%{_bindir}/miri_sdr

%files -n %{libname}
%license COPYING
%{_libdir}/libmirisdr.so.%{sover}
%{_libdir}/libmirisdr.so.%{sover}.*

%files -n mirisdr-udev
%license COPYING
%{_udevrulesdir}/10-mirisdr.rules

%files devel
%{_includedir}/mirisdr.h
%{_includedir}/mirisdr_export.h
%{_libdir}/libmirisdr.so
%{_libdir}/pkgconfig/libmirisdr.pc

%changelog
