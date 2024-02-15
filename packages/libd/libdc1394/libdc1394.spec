#
# spec file for package libdc1394
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libdc1394
Version:        2.2.7
Release:        0
Summary:        1394-Based Digital Camera Control Library
License:        LGPL-2.1-or-later
Group:          Hardware/Camera
URL:            https://damien.douxchamps.net/ieee1394/libdc1394/
Source0:        https://downloads.sourceforge.net/project/libdc1394/libdc1394-2/%{version}/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch0:         libdc1394.no-x11.patch
Patch1:         libdc1394.ac.patch
Patch2:         libdc1394-swab_fix.patch
Patch3:         libdc1394-v4l-2.6.38.patch
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libraw1394)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2) >= 0.8.4

%description
This library provides functionality for controlling any camera that
conforms to the 1394-Based Digital Camera Specification. It utilizes
the low-level functionality provided by libraw1394 to communicate with
the camera.

%package -n libdc1394-26
Summary:        1394-based Digital Camera Control library
Group:          System/Libraries

%description -n libdc1394-26
This library provides functionality for controlling any camera that
conforms to the 1394-Based Digital Camera Specification (which can be
found at http://www.1394ta.org/Download/Technology/Specifications/Camera120.pdf).
It utilizes the low-level functionality provided by libraw1394 to
communicate with the camera.

%package devel
Summary:        Development libraries and header files for dc1394
Group:          Development/Libraries/C and C++
Requires:       %{name}-tools = %{version}
Requires:       libdc1394-26 = %{version}
Requires:       pkgconfig(libraw1394)

%description devel
This package contains the header files and libraries for building
programs using the dc1394 library.

%package tools
Summary:        Command-line utilities from libdc1394
# added on 2015-11-14
Group:          Hardware/Camera
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description tools
This subpackage contains a 1394 bus reset utility.

%prep
%setup -q
%autopatch -p1
# Dummy macro for ignored SDL, autoreconf fails otherwise
echo "AC_DEFUN([AM_PATH_SDL], [])" >> m4/dummy_sdl.m4

%build
autoreconf -fvi
%configure \
	--disable-static \
	--disable-xv
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
rm -f %{buildroot}%{_bindir}/dc1394_vloopback %{buildroot}%{_mandir}/man1/dc1394_vloopback.1*
rm -f %{buildroot}%{_mandir}/man1/dc1394_multiview.1*
rm -f %{buildroot}%{_mandir}/man1/grab_*_image.1*
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libdc1394-26 -p /sbin/ldconfig
%postun -n libdc1394-26 -p /sbin/ldconfig

%files tools
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/dc1394_reset_bus
%{_mandir}/man1/dc1394_reset_bus.1%{?ext_man}

%files -n libdc1394-26
%{_libdir}/libdc1394.so.26*

%files devel
%{_includedir}/dc1394
%{_libdir}/libdc1394.so
%{_libdir}/pkgconfig/*.pc

%changelog
