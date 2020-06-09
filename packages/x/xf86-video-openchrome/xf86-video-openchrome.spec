#
# spec file for package xf86-video-openchrome
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


Name:           xf86-video-openchrome
Version:        0.6.0
Release:        0
Summary:        Openchrome driver (VIA GPUs) for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Patch0:         n_xorg-server-1.20.patch
Patch1:         u_gcc10.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xvmc)
ExclusiveArch:  %{ix86} x86_64
%x11_abi_videodrv_req

%description
The OpenChrome project is committed to providing and supporting fully free 
and Open Source drivers that take full advantage of the hardware acceleration 
of VIA chipsets featuring the VIA UniChrome, UniChrome Pro and Chrome9 integrated graphics processors.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README NEWS COPYING
%{_libdir}/libchromeXvMC.so*
%{_libdir}/libchromeXvMCPro.so*
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/openchrome_drv.so
%{_mandir}/man4/openchrome.4%{?ext_man}

%changelog
