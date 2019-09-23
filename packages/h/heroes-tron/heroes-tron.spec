#
# spec file for package heroes-tron
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


Name:           heroes-tron
BuildRequires:  SDL_mixer-devel
BuildRequires:  autoconf >= 2.68
BuildRequires:  automake
BuildRequires:  xorg-x11
%define myname heroes
%define data_version 1.5
PreReq:         %install_info_prereq
Version:        0.21
Release:        0
Source0:        %{myname}-%{version}.tar.bz2
Source1:        %{myname}-data-%{data_version}.tar.bz2  
Source2:        %{myname}-sound-effects-1.0.tar.bz2  
Source3:        %{myname}-sound-tracks-1.0.tar.bz2
Patch:          %{myname}-%{version}.diff
Patch1:         %{myname}-%{version}-menus.diff
Patch2:         %{myname}-%{version}-gcc4.diff
Patch3:         %{myname}-%{version}-gcc_warning.diff 
Patch4:         heroes-build-fixes.patch 
Patch5:         automake-1.12.patch
Patch6:         heroes-bigendian.patch
Url:            http://heroes.sourceforge.net/download.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Game Like Tron and Nibbles Games
License:        GPL-2.0+
Group:          Amusements/Games/Action/Race

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features.  In it, you
must maneuver a small vehicle around a world and collect powerups while
avoiding obstacles, your opponents' trails, and even your own trail.
Several modes of play are available, including "get-all-the-bonuses",
death match, and "squish-the-pedestrians".

%prep
%setup -q -n %{myname}-%{version} -b 1 -b 2 -b 3
%patch
%patch1
%patch2 -p1
%patch3
%patch4
%patch5 -p1
%patch6 -p1

%build 
%define sharedir %{_prefix}/share
%define datadir  %{sharedir}/games
autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS"
./configure \
		--datadir=%{datadir} \
		--prefix=%{_prefix} \
		--mandir=%{sharedir}/man \
		--infodir=%{sharedir}/info \
		--bindir=%{_bindir} \
		--without-ggi \
		--without-gii \
		--without-mikmod \
		--with-sdl \
		--with-sdl-mixer \
		--disable-joystick 
make %{?_smp_mflags}
cd ../%{myname}-data-%{data_version}
./configure \
		--prefix=%{_prefix} \
		--datadir=%{datadir} 
make %{?_smp_mflags}
cd ../%{myname}-sound-effects-1.0
./configure \
		--prefix=%{_prefix} \
		--datadir=%{datadir}
make %{?_smp_mflags}
cd ../%{myname}-sound-tracks-1.0
./configure \
                --prefix=%{_prefix} \
		--datadir=%{datadir}     
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
#mv $RPM_BUILD_ROOT%{datadir}/locale $RPM_BUILD_ROOT%{sharedir}/locale
pushd ../%{myname}-data-%{data_version}
make DESTDIR=$RPM_BUILD_ROOT install
popd
pushd ../%{myname}-sound-effects-1.0 
make DESTDIR=$RPM_BUILD_ROOT install
popd
pushd ../%{myname}-sound-tracks-1.0 
make DESTDIR=$RPM_BUILD_ROOT install
popd
%find_lang heroes

%post
%install_info --info-dir=%{_infodir} %{_infodir}/heroes.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/heroes.info.gz

%files -f heroes.lang 
%defattr(-, root, root)
%doc COPYING NEWS README THANKS TODO AUTHORS 	 
%{_bindir}/heroes
%{_bindir}/heroeslvl
%{sharedir}/info/heroes.info*
%{sharedir}/man/man6/heroes.6*
%{sharedir}/man/man6/heroeslvl.6*
#%{sharedir}/heroes
%{datadir}/heroes

%changelog
