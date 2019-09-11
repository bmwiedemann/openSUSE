#
# spec file for package xmoto
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xmoto
Version:        0.5.11
Release:        0
Summary:        2D motocross platform game
License:        GPL-2.0+
Group:          Amusements/Games/Action/Other
Url:            http://xmoto.tuxfamily.org/
Source0:        http://download.tuxfamily.org/%{name}/%{name}/%{version}/%{name}-%{version}-src.tar.gz
Source1:        %{name}.appdata.xml
# PATCH-FIX-UPSTREAM xmoto-0.5.5-basedir.patch adam@mizerski.pl -- Fix implicit declaration of function 'mkdir'
Patch0:         %{name}-0.5.5-basedir.patch
# PATCH-FIX-OPENSUSE xmoto-0.5.11-pointer-comparison.patch boo#1041253 wbauer@tmo.at -- Fix build with GCC7
Patch1:         %{name}-0.5.11-pointer-comparison.patch
# PATCH-FIX-OPENSUSE xmoto-nobuild_date.patch dimstar@opensuse.org -- Do not add build time and date: it's useless information
Patch100:       %{name}-nobuild_date.patch

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(lua5.1)
%else
BuildRequires:  pkgconfig(lua)
%endif
BuildRequires:  pkgconfig(ode)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}

%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike to
its limit, if you want to have a chance finishing the more difficult of
the challenges.  First you'll try just to complete the levels, while
later you'll compete with yourself and others, racing against the
clock.

%package data
Summary:        Xmoto architecture independent data
Group:          Amusements/Games/Action/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Xmoto translations and some other architecture independent data.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch100 -p1
# Let's always use system's ode:
rm -rf src/ode
ln -s %{_includedir}/ode src/ode

%build
CXXFLAGS="%{optflags} -fno-strict-aliasing" \
%configure \
	--with-asian-ttf-file=%{_datadir}/fonts/truetype/bkai00mp.ttf \
	--with-internal-xdg=1
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes %{buildroot}%{_datadir}/locale
install -p -D -m 644 extra/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%suse_update_desktop_file -i %{name}
%find_lang %{name}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/pixmaps/xmoto.xpm
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%files data -f %{name}.lang
%defattr(-, root, root)
%{_datadir}/%{name}

%changelog
