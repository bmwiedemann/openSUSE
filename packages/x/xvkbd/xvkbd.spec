#
# spec file for package xvkbd
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


Name:           xvkbd
Version:        4.1
Release:        0
Summary:        Virtual Keyboard for the X Window System
License:        GPL-2.0-or-later
URL:            http://t-sato.in.coocan.jp/xvkbd/
Source0:        http://t-sato.in.coocan.jp/xvkbd/%{name}-%{version}.tar.gz
Source1:        xvkbd.desktop
Source2:        xvkbd.png
# PATCH-FIX-UPSTREAM xvkbd-3.0-compilerwarnings.diff dkukawka@suse.de -- Avoid warnings with warn_unused_result
Patch0:         xvkbd-3.0-compilerwarnings.diff
BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  xaw3d-devel

%description
Xvkbd is a virtual (graphical) keyboard program for the X Window System
which provides a facility to enter characters onto other clients
(software) by clicking on an on-screen keyboard.

%prep
%setup -q
%patch0 -p1

# Remove build time references so build-compare can do its work
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/g" xvkbd.c

%build
%configure
%make_build

%install
install -dm 0755 %{buildroot}%{_datadir}/X11/app-defaults
%make_install
desktop-file-install %{SOURCE1}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/xvkbd.png

%files
%doc ChangeLog README
%license COPYING
%{_mandir}/man1/xvkbd.1%{?ext_man}
%{_bindir}/xvkbd
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/xvkbd.png
%{_datadir}/xvkbd/
%dir %{_datadir}/X11/app-defaults/
%{_datadir}/X11/app-defaults/*

%changelog
