#
# spec file for package xvkbd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.9
Release:        0
Summary:        Virtual Keyboard for the X Window System
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            http://t-sato.in.coocan.jp/xvkbd/
Source0:        http://t-sato.in.coocan.jp/xvkbd/%{name}-%{version}.tar.gz
Source1:        xvkbd.desktop
Source2:        xvkbd.png
Source3:        xvkbd.default
# PATCH-FIX-UPSTREAM xvkbd-3.0-compilerwarnings.diff dkukawka@suse.de -- Avoid warnings with warn_unused_result
Patch0:         xvkbd-3.0-compilerwarnings.diff
%if 0%{?suse_version} > 1210
BuildRequires:  desktop-file-utils
%else
BuildRequires:  update-desktop-files
%endif
%if 0%{?suse_version} > 1210
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
%else
BuildRequires:  xorg-x11-devel
%endif
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
xmkmf -a
make CCOPTIONS="%{optflags}" %{?_smp_mflags}

%install
%make_install
make DESTDIR=%{buildroot} install.man
%if 0%{?suse_version} > 1210
desktop-file-install %{SOURCE1}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/xvkbd.png
%else
%suse_update_desktop_file -i %{name}
%endif
install -Dpm 0644 %{SOURCE3} %{buildroot}%{appdefdir}/xvkbd.default

%files
%doc README
%license COPYING
%{_mandir}/man1/xvkbd.1x%{ext_man}
%{_bindir}/xvkbd
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/xvkbd.png
%dir %{_datadir}/X11/app-defaults/
%{_datadir}/X11/app-defaults/*

%changelog
