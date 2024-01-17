#
# spec file for package sar2
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


Name:           sar2
Version:        2.5.0
Release:        0
Summary:        Rescue Helicopter Simulator
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Simulation
URL:            https://searchandrescue2.github.io/sar2/
Source:         https://github.com/SearchAndRescue2/sar2/archive/v%{version}.tar.gz
BuildRequires:  Mesa-devel
BuildRequires:  fdupes
BuildRequires:  freealut-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  libXxf86vm-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  scons
BuildRequires:  xorg-x11-libICE-devel
BuildRequires:  xorg-x11-libSM-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  xorg-x11-libXmu-devel
BuildRequires:  xorg-x11-libXpm-devel
Requires:       %{name}-data = %{version}
%if 0%{?suse_version} < 1330
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%endif

%description
Search and Rescue II (SaR II) is an open source helicopter simulator game for
Linux and OSX. In it you can fly several helicopter and airplane models in
some basic scenarios.

SaR II has low graphic requirements while still provides a fun and demanding
gameplay where the player needs to locate, pick-up and rescue victims of all
sorts in steep mountains, burning buildings or in the sea.

%package data
Summary:        Data files for sar2
Group:          Amusements/Games/3D/Simulation
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Data files for Search and Rescue II

%prep
%setup -q

%build
scons --optflags="%{optflags} -DHAVE_LIBXPM"

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -ar data/* %{buildroot}%{_datadir}/%{name}/

mkdir -p %{buildroot}%{_mandir}/man6
cp -a man/* %{buildroot}%{_mandir}/man6

mkdir -p %{buildroot}%{_bindir}
cp -a bin/%{name} %{buildroot}%{_bindir}

install -D -m 0644 extra/sar2.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -m 0644 extra/sar2.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

install -D -m 0644 extra/sar2.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc AUTHORS CHANGELOG.md HACKING README.md
%license LICENSE
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/appdata/%{name}.appdata.xml

%files data
%{_datadir}/%{name}/

%changelog
