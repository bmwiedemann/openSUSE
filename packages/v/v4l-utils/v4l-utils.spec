#
# spec file for package v4l-utils
#
# Copyright (c) 2025 SUSE LLC
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

%ifarch armv7l armv7hl aarch64
# Qt6 doesn't have gl support in these archs
%bcond_with qvidcap
%else
%if 0%{?suse_version} == 1500
# Neither does Qt in SLE15
%bcond_with qvidcap
%else
%bcond_without qvidcap
%endif
%endif

%endif
%define _udevdir %(pkg-config --variable udevdir udev)
%define so_ver 0
%define sname v4l-utils
Name:           v4l-utils%{?psuffix}
Version:        1.28.1
Release:        0
Summary:        Utilities for video4linux
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://linuxtv.org/downloads/v4l-utils/
Source0:        https://linuxtv.org/downloads/v4l-utils/%{sname}-%{version}.tar.xz
Source1:        https://linuxtv.org/downloads/v4l-utils/%{sname}-%{version}.tar.xz.asc
Source2:        %{sname}.keyring
Source100:      baselibs.conf
Patch0:         use_system_v4l_for_qv4l.patch
Patch1:         v4l-utils-32bitfix.patch
BuildRequires:  alsa-devel
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       libv4l = %{version}
%if "%{flavor}" == ""
BuildRequires:  doxygen
BuildRequires:  kernel-headers
%endif
%if "%{flavor}" == "qv4l2"
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Platform)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4lconvert)
%endif

%description
v4l-utils is a collection of various video4linux (V4L) utilities.

%lang_package

%package devel-tools
Summary:        Utilities for v4l2 / DVB driver development and debugging
License:        GPL-2.0-only AND GPL-2.0-or-later
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

%package -n libdvbv5-gconv
Summary:        Gconv files with the charsets For Digital TV
License:        GPL-2.0-only
Requires:       libdvbv5-%{so_ver} = %{version}

%description -n libdvbv5-gconv
Some digital TV standards define their own charsets. Add library
support for them: EN 300 468 and ARIB STD-B24

%package -n libv4l
Summary:        Collection of video4linux support libraries
License:        GPL-2.0-only AND LGPL-2.1-or-later

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

%description -n qv4l2
qv4l2 is a test control and streaming test application for video4linux.

%prep
%autosetup -p1 -n %{sname}-%{version}

%build
%if 0%{?suse_version} == 1500
export CC=gcc-13
export CXX=g++-13
%endif

%meson \
  -Dudevdir=%{_udevdir} \
  -Ddoxygen-doc=disabled \
  -Ddoxygen-man=false \
  -Ddoxygen-html=false \
  -Dbpf=disabled \
%if "%{flavor}" == "qv4l2"
  -Dqv4l2=enabled \
%if %{with qvidcap}
  -Dqvidcap=enabled \
%else
  -Dqvidcap=disabled \
%endif
  -Dlibdvbv5=disabled \
  -Dv4l-plugins=false \
  -Dv4l-utils=false \
  -Dv4l-wrappers=false \
  -Dv4l2-compliance-libv4l=false \
  -Dv4l2-ctl-libv4l=false \
  -Dv4l2-ctl-stream-to=false \
%else
  -Dqv4l2=disabled \
  -Dqvidcap=disabled \
  -Dlibdvbv5=enabled \
%endif
  %{nil}
%meson_build

%install
%meson_install
%if "%{flavor}" == ""
install -dm 0755 %{buildroot}%{_libdir}/gconv/gconv-modules.d
mv %{buildroot}%{_libdir}/gconv/gconv-modules %{buildroot}%{_libdir}/gconv/gconv-modules.d/libdvbv5.conf
%find_lang "%{name}"
%find_lang libdvbv5
%endif

find %{buildroot} -type f -name "*.la" -delete -print

%if "%{flavor}" == ""
%post -n libdvbv5-%{so_ver} -p /sbin/ldconfig
%postun -n libdvbv5-%{so_ver} -p /sbin/ldconfig
%post -n libdvbv5-gconv -p %{_sbindir}/iconvconfig
%postun -n libdvbv5-gconv -p %{_sbindir}/iconvconfig
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
%doc ChangeLog README.md TODO
%dir %{_sysconfdir}/rc_keymaps/
%config(noreplace) %{_sysconfdir}/rc_maps.cfg
%{_udevdir}/rc_keymaps
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
%doc ChangeLog README.md TODO
%{_bindir}/decode_tm6000
%{_bindir}/v4l2-compliance
%{_bindir}/v4l2-tracer
%{_sbindir}/v4l2-dbg
%{_mandir}/man1/v4l2-compliance.1%{?ext_man}
%{_mandir}/man1/v4l2-tracer.1%{?ext_man}

%files -n dvb-utils
%license COPYING
%doc ChangeLog README.md TODO
%{_bindir}/dvb-*
%{_bindir}/dvbv5-*
%{_mandir}/man1/dvb-*1%{?ext_man}
%{_mandir}/man1/dvbv5-*1%{?ext_man}

%files -n libdvbv5-%{so_ver} -f libdvbv5.lang
%{_libdir}/libdvbv5.so.%{so_ver}*

%files -n libdvbv5-devel
%license COPYING.libdvbv5
%doc TODO.libdvbv5
%{_includedir}/libdvbv5/
%{_libdir}/libdvbv5.so
%{_libdir}/pkgconfig/libdvbv5*.pc

%files -n libdvbv5-gconv
%{_libdir}/gconv/*.so
%{_libdir}/gconv/gconv-modules.d/libdvbv5.conf

%files -n libv4l
%license COPYING.libv4l
%doc ChangeLog README.md README.libv4l TODO
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
%doc ChangeLog README.md TODO
%{_bindir}/qv4l2
%{_datadir}/applications/qv4l2.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/??x??
%dir %{_datadir}/icons/hicolor/??x??/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/*/apps/qv4l2.*
%{_mandir}/man1/qv4l2.1%{?ext_man}
%if %{with qvidcap}
%{_bindir}/qvidcap
%{_datadir}/applications/qvidcap.desktop
%{_datadir}/icons/hicolor/*/apps/qvidcap.*
%{_mandir}/man1/qvidcap.1%{?ext_man}
%endif

%endif

%changelog
