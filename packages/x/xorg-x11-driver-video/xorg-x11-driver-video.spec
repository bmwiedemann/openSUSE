#
# spec file for package xorg-x11-driver-video
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


#
Name:           xorg-x11-driver-video
Version:        7.6_1
Release:        0
Summary:        Compatibility metapackage for X.Org video drivers
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
Source0:        README.meta
Source102:      xorg-confd-snippets.tar.bz2
# For directory ownership
BuildRequires:  xorg-x11-server
Requires:       xorg-x11-server
Supplements:    xorg-x11-server
## Requires of packages that we split away from xorg-x11-driver-video
## and do not require any GPU hardware/emulation
Requires:       xf86-video-fbdev
# vesa X driver dropped from sle15
%if 0%{?suse_version} < 1330
Requires:       xf86-video-vesa
%endif
## End Requires of packages that we split away from xorg-x11-driver-video
## Get rid of old and no longer supported drivers (bnc#873443)
Provides:       xorg-x11-driver-video-radeonhd
Obsoletes:      xorg-x11-driver-video-radeonhd
Provides:       xorg-x11-driver-video-unichrome
Obsoletes:      xorg-x11-driver-video-unichrome
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x

%description
This package is a compatibility metapackage. It used to contain the
X.Org video drivers.

%prep
%setup -c -T
cp %{SOURCE0} .

%build

%install
tar xf $RPM_SOURCE_DIR/xorg-confd-snippets.tar.bz2 -C $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.meta
%config %{_sysconfdir}/X11/xorg.conf.d/50-device.conf
%config %{_sysconfdir}/X11/xorg.conf.d/50-monitor.conf
%config %{_sysconfdir}/X11/xorg.conf.d/50-screen.conf

%changelog
