#
# spec file for package xf86-video-qxl
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


# Xspice is x86_64 only since spice-server is x86_64 only
%ifarch x86_64
%if %{suse_version} >= 1230
%bcond_without xspice
%else
%bcond_with xspice
%endif
%else
%bcond_with xspice
%endif

Name:           xf86-video-qxl
Version:        0.1.6
Release:        0
Summary:        QXL virtual GPU video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(libcacard)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.2
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.4
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_videodrv_req

%description
qxl is an Xorg driver for QXL virtual GPU as found in the spice project.

%if %{with xspice}
%package -n    xorg-x11-server-Xspice
Summary:        XSpice is an X server that can be accessed by a Spice client
Group:          System/X11/Servers/XF86_4
%x11_abi_videodrv_req
BuildRequires:  pkgconfig(spice-server) >= 0.6.3

%description -n xorg-x11-server-Xspice
XSpice is both an X and a Spice server that can be accessed by a Spice client.
%endif

%prep
%setup -q

%build
autoreconf -fi
%configure \
%if 0%{?with_xspice}
    --enable-xspice \
    --enable-ccid
%endif

make %{?_smp_mflags}

%install
%make_install
%if %{with xspice}
# FIXME: upstream installs this file by default, we install it elsewhere.
# upstream should just not install it and let dist package deal with
# doc/examples.
rm -f $RPM_BUILD_ROOT/usr/share/doc/xf86-video-qxl/spiceqxl.xorg.conf.example
%endif
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/qxl_drv.so

%if %{with xspice}
%files -n xorg-x11-server-Xspice
%defattr(-,root,root)
%doc COPYING README.xspice README.md examples/spiceqxl.xorg.conf.example
%{_bindir}/Xspice
%{_libdir}/xorg/modules/drivers/spiceqxl_drv.so
%dir %{_libdir}/pcsc/
%dir %{_libdir}/pcsc/drivers/
%dir %{_libdir}/pcsc/drivers/serial/
%{_libdir}/pcsc/drivers/serial/libspiceccid.so*
%endif

%changelog
