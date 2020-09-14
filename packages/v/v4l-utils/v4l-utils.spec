#
# spec file for package v4l
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qv4l2"
%global psuffix -%{flavor}
%endif
%define _udevdir %(pkg-config --variable udevdir udev)
%define so_ver 0
%define sname v4l-utils
Name:           v4l-utils%{?psuffix}
Version:        1.20.0
Release:        0
Summary:        Utilities for video4linux
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-2.0-only
URL:            https://linuxtv.org/downloads/v4l-utils/
Source0:        https://linuxtv.org/downloads/v4l-utils/%{sname}-%{version}.tar.bz2
Source1:        https://linuxtv.org/downloads/v4l-utils/%{sname}-%{version}.tar.bz2.asc
Source2:        %{sname}.keyring
Source100:      baselibs.conf
Patch0:         sysmacros.patch
Patch1:         use_system_v4l_for_qv4l.patch
Patch2:         v4l-utils-32bitfix.patch
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
Requires:       libv4l = %{version}
%if "%{flavor}" == ""
BuildRequires:  doxygen
BuildRequires:  kernel-headers
%endif
%if "%{flavor}" == "qv4l2"
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4lconvert)
%endif

%description
v4l-utils is a collection of various video4linux (V4L) utilities.

%lang_package

%package devel-tools
Summary:        Utilities for v4l2 / DVB driver development and debugging
License:        GPL-2.0-or-later AND GPL-2.0-only
Requires:       libv4l = %{version}

%description devel-tools
Utilities for v4l2 / DVB driver authors for development and debugging.

%package -n dvb-utils
Summary:        Utilities for DVB devices
License:        GPL-2.0-only
Recommends:     dtv-scan-tables-v5

%description -n dvb-utils
dvb-utils is a collection of various DVB utilities.

%package -n libdvbv5-%{so_ver}
Summary:        Library that provides access to DVB adapter cards
License:        GPL-2.0-only

%description -n libdvbv5-%{so_ver}
libdvbv5 is a library meant to be used by digital TV applications that need to
talk with media hardware.

This package contains shared lib for packages that use libdvbv5.

%package -n libdvbv5-devel
Summary:        Development files for libdvbv5
License:        GPL-2.0-only
Requires:       libdvbv5-%{so_ver} = %{version}

%description -n libdvbv5-devel
The libdvbv5-devel package contains libraries and header files for
developing applications that use libdvbv5.

%package -n libv4l
Summary:        Collection of video4linux support libraries
License:        LGPL-2.1-or-later AND GPL-2.0-only

%description -n libv4l
libv4l is a collection of libraries which adds a thin abstraction layer on
top of video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices without
having to write separate code for different devices in the same class.

%package -n libv4l1-%{so_ver}
Summary:        Video4linux support library
License:        LGPL-2.1-or-later
Requires:       libv4l

%description -n libv4l1-%{so_ver}
libv4l1 offers the (deprecated) v4l1 API on top of v4l2 devices, independent
of the drivers for those devices supporting v4l1 compatibility (which many
v4l2 drivers do not).

This package contains shared lib for packages that use libv4l1.

%package -n libv4l2-%{so_ver}
Summary:        Video4linux support library
License:        LGPL-2.1-or-later
Requires:       libv4l

%description -n libv4l2-%{so_ver}
libv4l2 offers the v4l2 API on top of v4l2 devices, while adding for the
application transparent libv4lconvert conversion where necessary.

This package contains shared lib for packages that use libv4l2.

%package -n libv4l2rds%{so_ver}
Summary:        Video4linux support library
License:        LGPL-2.1-or-later
Requires:       libv4l

%description -n libv4l2rds%{so_ver}
libv4l2rds offers decoding raw RDS data from V4L2 Radio devices and simple ways
to access the received RDS information.

This package contains shared lib for packages that use libv4l2rds.

%package -n libv4lconvert%{so_ver}
Summary:        Video4linux support library
License:        LGPL-2.1-or-later
Requires:       libv4l

%description -n libv4lconvert%{so_ver}
libv4lconvert offers functions to convert from any (known) pixel-format
to V4l2_PIX_FMT_BGR24 or V4l2_PIX_FMT_YUV420.

This package contains shared lib for packages that use libv4lconvert.

%package -n libv4l-devel
Summary:        Development files for libv4l
License:        LGPL-2.1-or-later
Requires:       libv4l1-%{so_ver} = %{version}
Requires:       libv4l2-%{so_ver} = %{version}
Requires:       libv4l2rds%{so_ver} = %{version}
Requires:       libv4lconvert%{so_ver} = %{version}

%description -n libv4l-devel
The libv4l-devel package contains libraries and header files for
developing applications that use libv4l.

%package -n     qv4l2
Summary:        Video4linux test control and streaming test application
License:        GPL-2.0-or-later
Requires:       libv4l = %{version}
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description -n qv4l2
qv4l2 is a test control and streaming test application for video4linux.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -vfi
%configure \
  --disable-static \
  --disable-silent-rules \
%if "%{flavor}" == "qv4l2"
  --disable-libdvb5 \
%else
  --disable-qv4l2 \
%endif
  --with-udevdir=%{_udevdir}

%if "%{flavor}" == "qv4l2"
%make_build -C utils/libmedia_dev
%make_build -C utils/libv4l2util
%make_build -C utils/qv4l2
%else
%make_build
%endif

%install
%if "%{flavor}" == "qv4l2"
%make_install -C utils/qv4l2
%suse_update_desktop_file -N "QV4l2" -G "V4L2 Test Utility" -r qv4l2 Qt AudioVideo Video TV

%else
%make_install
%find_lang "%{name}"

# Not needed (links to plugins in libv4l subdir)
rm %{buildroot}%{_libdir}/{v4l1compat.so,v4l2convert.so}
%endif

find %{buildroot} -type f -name "*.la" -delete -print

%if "%{flavor}" == ""
%post -n libdvbv5-%{so_ver} -p /sbin/ldconfig
%postun -n libdvbv5-%{so_ver} -p /sbin/ldconfig
%post -n libv4l1-%{so_ver} -p /sbin/ldconfig
%postun -n libv4l1-%{so_ver} -p /sbin/ldconfig
%post -n libv4l2-%{so_ver} -p /sbin/ldconfig
%postun -n libv4l2-%{so_ver} -p /sbin/ldconfig
%post -n libv4l2rds%{so_ver} -p /sbin/ldconfig
%postun -n libv4l2rds%{so_ver} -p /sbin/ldconfig
%post -n libv4lconvert%{so_ver} -p /sbin/ldconfig
%postun -n libv4lconvert%{so_ver} -p /sbin/ldconfig
%endif

%if "%{flavor}" == ""
%files
%license COPYING
%doc ChangeLog README TODO
%dir %{_sysconfdir}/rc_keymaps/
%config(noreplace) %{_sysconfdir}/rc_maps.cfg
%{_udevdir}/rc_keymaps
%if 0%{?suse_version} > 1500
%dir %{_unitdir}/systemd-udevd.service.d
%{_unitdir}/systemd-udevd.service.d/50-rc_keymap.conf
%endif
%{_udevrulesdir}/70-infrared.rules
%{_bindir}/cx18-ctl
%{_bindir}/cec-compliance
%{_bindir}/cec-ctl
%{_bindir}/cec-follower
%{_bindir}/ir-ctl
%{_bindir}/ir-keytable
%{_bindir}/ivtv-ctl
%{_bindir}/media-ctl
%{_bindir}/rds-ctl
%{_bindir}/v4l2-ctl
%{_bindir}/v4l2-sysfs-path
%{_mandir}/man5/rc_keymap.5%{?ext_man}
%{_mandir}/man1/ir-keytable.1%{?ext_man}
%{_mandir}/man1/v4l2-ctl.1%{?ext_man}
%{_mandir}/man1/cec-compliance.1%{?ext_man}
%{_mandir}/man1/cec-ctl.1%{?ext_man}
%{_mandir}/man1/cec-follower.1%{?ext_man}
%{_mandir}/man1/ir-ctl.1%{?ext_man}

%files lang -f "%{name}.lang"

%files devel-tools
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/decode_tm6000
%{_bindir}/v4l2-compliance
%{_sbindir}/v4l2-dbg
%{_mandir}/man1/v4l2-compliance.1%{?ext_man}

%files -n dvb-utils
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/dvb-*
%{_bindir}/dvbv5-*
%{_mandir}/man1/dvb-*1%{?ext_man}
%{_mandir}/man1/dvbv5-*1%{?ext_man}

%files -n libdvbv5-%{so_ver}
%{_libdir}/libdvbv5.so.%{so_ver}*

%files -n libdvbv5-devel
%license COPYING.libdvbv5
%doc TODO.libdvbv5
%{_includedir}/libdvbv5/
%{_libdir}/libdvbv5.so
%{_libdir}/pkgconfig/libdvbv5*.pc

%files -n libv4l
%license COPYING.libv4l
%doc ChangeLog README README.libv4l TODO
%{_libdir}/libv4l/

%files -n libv4l1-%{so_ver}
%{_libdir}/libv4l1.so.%{so_ver}*

%files -n libv4l2-%{so_ver}
%{_libdir}/libv4l2.so.%{so_ver}*

%files -n libv4l2rds%{so_ver}
%{_libdir}/libv4l2rds.so.%{so_ver}*

%files -n libv4lconvert%{so_ver}
%{_libdir}/libv4lconvert.so.%{so_ver}*

%files -n libv4l-devel
%license COPYING.libv4l
%doc README.lib-multi-threading
%{_includedir}/libv4l*.h
%{_libdir}/libv4l*.so
%{_libdir}/pkgconfig/libv4l*.pc
%endif

%if "%{flavor}" == "qv4l2"
%files -n qv4l2
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/qv4l2
%{_datadir}/applications/qv4l2.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/??x??
%dir %{_datadir}/icons/hicolor/??x??/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/*/apps/qv4l2.*
%{_mandir}/man1/qv4l2.1%{?ext_man}
%endif

%changelog
