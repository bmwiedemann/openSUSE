#
# spec file for package xf86-video-freedreno
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xf86-video-freedreno
Summary:        X.Org X server -- freedreno display driver
License:        MIT and BSD-3-Clause
Group:          System/X11/Servers/XF86_4
Version:        1.4.0
Release:        0.0
ExclusiveArch:  %arm
Url:            https://github.com/freedreno/xf86-video-freedreno
Source0:        http://xorg.freedesktop.org/releases/individual/driver/xf86-video-freedreno-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/driver/xf86-video-freedreno-%{version}.tar.bz2.sig
Patch1:         https://github.com/freedreno/xf86-video-freedreno/commit/5c82dc7874b6eaff39dc8c8575e72e5a40f13ea6.patch#/xf86-video-freedreno-abi-23.patch
Patch2:         https://github.com/freedreno/xf86-video-freedreno/commit/5f60ca4fe99199183dced955de0206acb5a5ebe9.patch#/xf86-video-freedreno-notifyfd.patch
Patch3:         https://github.com/freedreno/xf86-video-freedreno/commit/6c8e21c686578f22d973a243a09c838943ddbadd.patch#/xf86-video-freedreno-notifyfd-more.patch
Requires:       xorg-x11-server
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libdrm-devel >= 2.4.54
BuildRequires:  libdrm2 >= 2.4.54
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)

%x11_abi_videodrv_req

%description
Open-source X.org graphics driver for Qualcomm Adreno graphics

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
export CFLAGS="%{optflags}"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root,-)
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/*.so
%doc %{_mandir}/man4/freedreno.4.gz
/usr/share/X11/xorg.conf.d/42-freedreno.conf

%changelog
