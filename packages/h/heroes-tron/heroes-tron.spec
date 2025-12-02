#
# spec file for package heroes-tron
#
# Copyright (c) 2021 SUSE LLC
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


%define myname heroes
%define data_version 1.5
Name:           heroes-tron
Version:        0.21
Release:        0
Summary:        Game Like Tron and Nibbles Games
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Race
URL:            http://heroes.sourceforge.net/download.html
Source0:        %{myname}-%{version}.tar.bz2
Source1:        %{myname}-data-%{data_version}.tar.bz2
Source2:        %{myname}-sound-effects-1.0.tar.bz2
Source3:        %{myname}-sound-tracks-1.0.tar.bz2
Patch0:         %{myname}-%{version}.diff
Patch1:         %{myname}-%{version}-menus.diff
Patch2:         %{myname}-%{version}-gcc4.diff
Patch3:         %{myname}-%{version}-gcc_warning.diff
Patch4:         heroes-build-fixes.patch
Patch5:         automake-1.12.patch
Patch6:         heroes-bigendian.patch
%if 0%{?suse_version} > 1500
BuildRequires:  gcc13
%endif
BuildRequires:  SDL_mixer-devel
BuildRequires:  autoconf >= 2.68
BuildRequires:  automake
BuildRequires:  xorg-x11
BuildRequires:  pkgconfig(allegro)
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features.  In it, you
must maneuver a small vehicle around a world and collect powerups while
avoiding obstacles, your opponents' trails, and even your own trail.
Several modes of play are available, including "get-all-the-bonuses",
death match, and "squish-the-pedestrians".

%prep
%setup -q -n %{myname}-%{version} -b 1 -b 2 -b 3
%patch -P 0
%patch -P 1
%patch -P 2 -p1
%patch -P 3
%patch -P 4
%patch -P 5 -p1
%patch -P 6 -p1

%build
%if 0%{?suse_version} > 1500
export CC=gcc-13
%endif
autoreconf -fiv
export CFLAGS="%{optflags}"
%if 0%{?suse_version} > 1500
export CFLAGS="$CFLAGS -fcommon"
%endif
%configure \
    --datadir=%{_datadir}/%{name} \
    --without-ggi \
    --without-gii \
    --without-mikmod \
    --with-sdl \
    --with-sdl-mixer \
    --disable-joystick
%make_build
cd ../%{myname}-data-%{data_version}
%configure --datadir=%{_datadir}/%{name}
%make_build
cd ../%{myname}-sound-effects-1.0
%configure --datadir=%{_datadir}/%{name}
%make_build
cd ../%{myname}-sound-tracks-1.0
%configure --datadir=%{_datadir}/%{name}
%make_build

%install
%make_install
pushd ../%{myname}-data-%{data_version}
%make_install
popd
pushd ../%{myname}-sound-effects-1.0
%make_install
popd
pushd ../%{myname}-sound-tracks-1.0
%make_install
popd
%find_lang heroes

%post
%install_info --info-dir=%{_infodir} %{_infodir}/heroes.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/heroes.info.gz

%files -f heroes.lang
%doc NEWS README THANKS TODO
%license COPYING AUTHORS
%{_bindir}/heroes
%{_bindir}/heroeslvl
%{_infodir}/heroes.info*%{?ext_info}
%{_mandir}/man6/heroes.6%{?ext_man}
%{_mandir}/man6/heroeslvl.6%{?ext_man}
%{_datadir}/%{name}

%changelog
