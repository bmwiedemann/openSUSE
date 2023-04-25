#
# spec file for package libgphoto2
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


%{nil <URL:
  https://github.com/gphoto/libgphoto2/issues/408#issuecomment-1472123588 >
  }
%bcond_with vusb
%if %{with:vusb}
%define configure_vusb    --enable-vusb --without-libusb --with-libusb-1.0=no
%else
%define configure_vusb %{nil}
%endif

%if %( pkg-config --modversion udev ) > 190
%define _udevrulesdir /usr/lib/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif

%define major 6

Name:           libgphoto2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libusb-1_0-devel
BuildRequires:  libxml2-devel
BuildRequires:  lockdev-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(udev)
URL:            https://gphoto.sourceforge.io/
# bug437293
%ifarch ppc64
Obsoletes:      libgphoto2-64bit
%endif
#
Summary:        A Digital Camera Library
License:        LGPL-2.1-or-later
Group:          Hardware/Camera
Version:        2.5.30
Release:        0
Source0:        https://downloads.sourceforge.net/project/gphoto/libgphoto/%version/%name-%version.tar.xz
Source1:        https://downloads.sourceforge.net/project/gphoto/libgphoto/%version/%name-%version.tar.xz.asc
Source2:        %name.keyring
Source3:        baselibs.conf
Patch0:         libgphoto2-enable-vusb-ptp.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package -n libgphoto2-%major
Summary:        A Digital Camera Library
Group:          System/Libraries
Requires(pre):  /sbin/ldconfig
Requires(post): /sbin/ldconfig
Requires(post): udev
Requires(postun):udev

%package -n libgphoto2_port12
Summary:        Port drivers for the libgphoto2 digital camera library
Group:          System/Libraries
Requires(pre):  /sbin/ldconfig
Requires(post): /sbin/ldconfig

%package doc
Summary:        Documentation for libgphoto2
Group:          Documentation/Other
BuildArch:      noarch

%package devel
Summary:        Development headers for libgphoto2
Group:          Development/Libraries/C and C++
Requires:       libexif-devel
Requires:       libgphoto2-%major = %version
Requires:       libgphoto2_port12 = %version
Requires:       libusb-1_0-devel

%package devel-doc
Summary:        Development documentation for libgphoto2
Group:          Documentation/HTML
Recommends:     libgphoto2-devel
BuildArch:      noarch

%description
gPhoto (GNU Photo) is a set of libraries for previewing, retrieving,
and capturing images from a range of supported digital cameras to your
local hard drive. It does not support digital cameras based on the USB
storage protocol. Those can be mounted by Linux directly.

As of this time, gPhoto supports around 1700 cameras, listed on:

https://gphoto.sourceforge.io/proj/libgphoto2/support.php

or by running

gphoto2 --list-cameras

%description -n libgphoto2-%major
gPhoto (GNU Photo) is a set of libraries for previewing, retrieving,
and capturing images from a range of supported digital cameras to your
local hard drive. It does not support digital cameras based on the USB
storage protocol as those can be mounted by Linux directly.

As of this time, gPhoto supports around 1700 cameras, listed on:

https://gphoto.sourceforge.io/proj/libgphoto2/support.php

or by running

gphoto2 --list-cameras

%description -n libgphoto2_port12
gPhoto (GNU Photo) is a set of libraries for previewing, retrieving,
and capturing images from a range of supported digital cameras to your
local hard drive. It does not support digital cameras based on the USB
storage protocol as those can be mounted by Linux directly.

This package contains the port drivers (e.g. the USB drivers, the PTP/IP
driver).

%description doc
gPhoto (GNU Photo) is a set of libraries for previewing, retrieving,
and capturing images from a range of supported digital cameras to your
local hard drive.

This is the user documentation.

%description devel
gPhoto (GNU Photo) is a set of libraries for previewing, retrieving,
and capturing images from a range of supported digital cameras to your
local hard drive.

These are its development libraries and headers.

%description devel-doc
gPhoto (GNU Photo) is a set of libraries for previewing, retrieving,
and capturing images from a range of supported digital cameras to your
local hard drive.

This is its API documentation in HTML format.

%lang_package -n libgphoto2-%major

%prep
%setup -q
%patch0 -p1
(cd doc && tar -xaf libgphoto2-api.html.tar.gz)

%build
#AUTOPOINT=true autoreconf -fi
PATH="/usr/X11R6/bin:$PATH"			\
%configure					\
  --with-doc-dir=%_defaultdocdir/%name	\
  --without-hal \
  --with-drivers=all %configure_vusb
make %{?_smp_mflags}

%check
make check

%install
# skip-check-libtool-deps
export LIBRARY_PATH="%buildroot/%_libdir"
%make_install

# .la files are not needed
rm %buildroot/%_libdir/*.la
rm %buildroot/%_libdir/libgphoto2/%version/*.la
rm %buildroot/%_libdir/libgphoto2_port/0.12.1/*.la

rm -rf %buildroot/usr/share/doc/libgphoto2_port

%find_lang libgphoto2-%major
%find_lang libgphoto2_port-12
cat libgphoto2-%major.lang libgphoto2_port-12.lang >libgphoto2-all.lang
pushd packaging/generic
	export CAMLIBS="%buildroot/%_libdir/libgphoto2/%version/"
	# new style UDEV rules (gudev) which will obsolete HAL fdi files
	if [ ! -d "%_udevrulesdir" ] ; then
		echo "*** The udev rules file location has changed. Fix the build."
		exit 1
	fi
%if 0%{?suse_version} > 1230
	install -m 0755 -d        %buildroot/%_udevhwdbdir
	./print-camera-list hwdb >%buildroot/%_udevhwdbdir/20-gphoto.hwdb
	# We still need UDEV rules for /dev/sg* and /dev/sd* for picture frames.
	# We also need it for PTP cameras that we do not know to appear in GVFS.
	install -m 0755 -d                          %buildroot/%_udevrulesdir
	./print-camera-list udev-rules version 201 >%buildroot/%_udevrulesdir/40-libgphoto2.rules
%else
	install -m 0755 -d                          %buildroot/%_udevrulesdir
	./print-camera-list udev-rules version 175 >%buildroot/%_udevrulesdir/40-libgphoto2.rules
%endif
popd
# udev helpers not used here.
rm %buildroot/usr/%_lib/udev/check-ptp-camera
mv doc/libgphoto2-api.html apidocs
mv doc/README.apidocs .
find apidocs -type f -name "*.md5" -delete
fn="%buildroot/%_libdir/pkgconfig/libgphoto2_port.pc"
grep -v driverdir= $fn > $fn.new
mv $fn.new $fn

find "%buildroot/%_libdir" -type f -name "*.la" -delete
%fdupes %buildroot/%_prefix

%files -n libgphoto2-%major
%defattr(-,root,root)
%doc AUTHORS NEWS README
%_libdir/libgphoto2
# support files for konica camlib
%_datadir/%name
%_libdir/libgphoto2.so.*
%if 0%{?suse_version} > 1230
%_udevhwdbdir/20-gphoto.hwdb
%endif
%_udevrulesdir/40-libgphoto2.rules

%files -n libgphoto2_port12
%defattr(-,root,root)
%doc libgphoto2_port/README libgphoto2_port/AUTHORS libgphoto2_port/NEWS
%_libdir/libgphoto2_port
%_libdir/libgphoto2_port.so.*
%_datadir/libgphoto2_port

%files -n libgphoto2-doc
%defattr(-,root,root)
%dir /usr/share/doc/%name
/usr/share/doc/%name/*
%_mandir/man3/libgphoto2.3*
%_mandir/man3/libgphoto2_port.3*

%files -n libgphoto2-%major-lang -f libgphoto2-all.lang

%files devel
%defattr(-,root,root)
%_includedir/gphoto2
%_bindir/gphoto2-config
%_bindir/gphoto2-port-config
%_libdir/libgphoto2.so
%_libdir/libgphoto2_port.so
%_libdir/pkgconfig/libgphoto2.pc
%_libdir/pkgconfig/libgphoto2_port.pc

%files devel-doc
%defattr(-,root,root)
%doc apidocs README.apidocs

%post   -n libgphoto2_port12 -p /sbin/ldconfig
%postun -n libgphoto2_port12 -p /sbin/ldconfig

%post -n %name-%major
/sbin/ldconfig
%if 0%{?suse_version} > 1230
%udev_hwdb_update
%endif
udevadm control --reload >/dev/null 2>&1 || :

%postun -n %name-%major
/sbin/ldconfig
if [ $1 -eq 0 ]; then
%if 0%{?suse_version} > 1230
        %udev_hwdb_update
        %udev_rules_update
%endif
udevadm control --reload 2>&1 > /dev/null || :
fi

%changelog
