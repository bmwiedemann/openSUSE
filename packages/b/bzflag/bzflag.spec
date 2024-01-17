#
# spec file for package bzflag
#
# Copyright (c) 2022 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           bzflag
Version:        2.4.26
Release:        0
Summary:        3D Networked Multiplayer Tank Battle Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://www.bzflag.org/
Source:         https://download.bzflag.org/bzflag/source/%{version}/bzflag-%{version}.tar.gz
Source2:        rc.bzflagserver
Source3:        %{name}-maps.tar.bz2
Source4:        sysconfig.bzflagserver-bzflag
Source5:        %{name}.desktop
Source6:        %{name}.png
Source7:        bzflagserver.service
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         %{name}-1.10.4-ncursespollution.patch
BuildRequires:  bc
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libcares-devel
BuildRequires:  libdrm-devel
BuildRequires:  ncurses-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(sdl2)
Requires(pre):  %fillup_prereq
%{?systemd_ordering}
%if 0%{?sles_version}
BuildRequires:  glew-devel
%else
BuildRequires:  pkgconfig(glew)
%endif
BuildRequires:  zlib-devel

%description
BZFlag is a 3D multiplayer tank battle game that allows users to play
against each other in a networked environment. Because it makes heavy
use of 3D graphics (OpenGL), a fast CPU or a supported 3D video card is
heavily recommended.

Find server maps in /usr/share/bzflag/maps.

%prep
%setup -q -a 3
%patch0 -p1
cp %{SOURCE2} .
cp %{SOURCE7} .

%build
%configure \
    --disable-dependency-tracking \
    --libdir=%{_libdir}/%{name} \
    --disable-static
%make_build all

%pre
%service_add_pre bzflagserver.service

%preun
%service_del_preun bzflagserver.service

%post
%fillup_only -an bzflagserver
%service_add_post bzflagserver.service

%postun
%service_del_postun bzflagserver.service

%install
#Init script for the BZFlag server
mkdir -p %{buildroot}%{_datadir}/%{name}/scripts
install -D -m 755 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/scripts/rcbzflagserver
install -D -m 644 %{SOURCE7} %{buildroot}%{_unitdir}/bzflagserver.service
%make_install MKDIR_P="mkdir -p --"
install -D -m 644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.bzflagserver-bzflag
mkdir -p %{buildroot}%{_datadir}/%{name}/maps
install -m 644 maps/*bzmap %{buildroot}%{_datadir}/%{name}/maps
install -D -m 644 %{SOURCE6} %{buildroot}%{_datadir}/pixmaps/bzflag.png
%suse_update_desktop_file -i %{name}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS PORTING README DEVINFO
%doc README.Linux misc/bzfs.conf ChangeLog
%{_datadir}/%{name}/
%{_datadir}/%{name}/scripts/
%{_datadir}/bzflag/scripts/rcbzflagserver
%{_unitdir}/bzflagserver.service
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_fillupdir}/sysconfig.bzflagserver-bzflag
%{_libdir}/%{name}/

%changelog
