#
# spec file for package conky
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_with    audacious
%bcond_without cmus
%ifarch %ix86 x86_64 aarch64
%bcond_without libXNVCtrl
%else
%bcond_with libXNVCtrl
%endif
Name:           conky
Version:        1.21.7
Release:        0
Summary:        A System Monitor
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT
URL:            https://github.com/brndnmtthws/conky
Source:         https://github.com/brndnmtthws/conky/archive/v%{version}.tar.gz#/conky-%{version}.tar.gz
Source1:        conkyconf.SUSE
Source2:        conky.conf.SUSE
Source3:        README.SUSE
Patch1:         conky-1.10.1-avoid-git.patch
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook2x
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  libiw-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libmysqld-devel
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  lua53-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PyYAML
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.52
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
Requires:       fontawesome-fonts
# This is required for imlib2 function properly.
Requires:       imlib2-loaders
Provides:       conky-cairo = %{version}
Obsoletes:      conky-cairo < %{version}
Provides:       conky-imlib2 = %{version}
Obsoletes:      conky-imlib2 < %{version}
%if %{with audacious}
BuildRequires:  pkgconfig(audacious)
BuildRequires:  pkgconfig(audclient)
BuildRequires:  pkgconfig(dbus-glib-1)
Provides:       conky-feature-audacious = %{version}
Obsoletes:      conky-feature-audacious < %{version}
%endif
%if %{with libXNVCtrl}
BuildRequires:  libXNVCtrl-devel
Provides:       conky-feature-nvidia = %{version}
Obsoletes:      conky-feature-nvidia < %{version}
%endif
%if 0%{?is_opensuse}
%if 0%{?suse_version} >= 1315
BuildRequires:  libircclient-devel
BuildRequires:  libtolua++-5_1-devel
%else
BuildRequires:  tolua++
%endif
%endif

%description
Conky is an configurable system monitor.

%package doc
Summary:        Documentation for conky
BuildArch:      noarch

%description doc
Conky is an configurable system monitor for X.

This package provides additional documentation about conky.

%package -n vim-plugin-conky
Summary:        Conky Configuration File Support for Vim
BuildArch:      noarch
Requires:       vim-base
Provides:       conky-vim = %{version}
Obsoletes:      conky-vim < %{version}

%description -n vim-plugin-conky
Conky is an configurable system monitor for X.

This package provides syntax highlighting support for conky
configuration files in vim.

%package -n nano-plugin-conky
Summary:        Conky Configuration File Support for nano
BuildArch:      noarch
Provides:       conky-nano = %{version}
Obsoletes:      conky-nano < %{version}

%description -n nano-plugin-conky
Conky is an configurable system monitor for X.

This package provides syntax highlighting support for conky
configuration files in nano.

%prep
%setup -q
%autopatch -p1

%build
%cmake -G Ninja \
	-DBUILD_APCUPSD=ON \
	-DBUILD_ARGB=ON \
%if %{with audacious}
	-DBUILD_AUDACIOUS=ON \
%else
    -DBUILD_AUDACIOUS=OFF \
%endif
	-DBUILD_BMPX=OFF \
%if %{with cmus}
	-DBUILD_CMUS=ON \
%else
    -DBUILD_CMUS=OFF \
%endif
	-DBUILD_CURL=ON \
	-DBUILD_DOCS=ON \
	-DBUILD_EVE=ON \
	-DBUILD_HDDTEMP=ON \
	-DBUILD_HTTP=ON \
	-DBUILD_I18N=ON \
	-DBUILD_IBM=ON \
	-DBUILD_ICAL=ON \
	-DBUILD_ICONV=ON \
   	-DBUILD_LUA_CAIRO=ON \
	-DBUILD_IMLIB2=ON \
    -DBUILD_LUA_IMLIB2=ON \
   	-DBUILD_LUA_RSVG=ON \
%if 0%{?is_opensuse}
    -DBUILD_IRC=ON \
%else
    -DBUILD_IRC=OFF \
%endif
	-DBUILD_XMMS2=OFF \
	-DBUILD_IOSTATS=ON \
	-DBUILD_IPV6=ON \
	-DBUILD_MATH=ON \
	-DBUILD_MOC=ON \
	-DBUILD_MPD=ON \
	-DBUILD_MYSQL=ON \
	-DBUILD_NCURSES=ON \
%if %{with libXNVCtrl}
	-DBUILD_NVIDIA=ON \
%else
    -DBUILD_NVIDIA=OFF \
%endif
	-DBUILD_PORT_MONITORS=ON \
	-DBUILD_PULSEAUDIO=ON \
	-DBUILD_RSS=ON \
	-DBUILD_OLD_CONFIG=ON \
	-DBUILD_WEATHER_METAR=ON \
	-DBUILD_WEATHER_XOAP=ON \
	-DBUILD_WLAN=ON \
	-DBUILD_X11=ON \
	-DBUILD_XDAMAGE=ON \
	-DBUILD_XDBE=ON \
	-DBUILD_XFT=ON \
	-DBUILD_XSHAPE=ON \
	-DOWN_WINDOW=ON

%ninja_build

%install
%ninja_install -C build

mkdir -p %{buildroot}%{_datadir}/vim/site/ftdetect/conkyrc.vim
install -m 644 extras/vim/ftdetect/conkyrc.vim %{buildroot}%{_datadir}/vim/site/ftdetect/conkyrc.vim
mkdir -p %dir %{buildroot}%{_datadir}/nano
install -m 644 extras/nano/conky.nanorc.j2 %{buildroot}%{_datadir}/nano/conky.nanorc.j2

# config
mkdir -p %{buildroot}%{_sysconfdir}/conky
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/conky/conky.conf
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/conkyconf
cp %{SOURCE3} .
sed -i "1d" extras/convert.lua
sed -i "1s/^/#!\/usr\/bin\/lua5.1\\n/" extras/convert.lua
install -m 0755 extras/convert.lua %{buildroot}%{_sysconfdir}/conky/
install -m 0644 data/conky_no_x11.conf data/conky.conf %{buildroot}%{_sysconfdir}/conky/
# clean
rm -rf %{buildroot}%{_libdir}/conky/*.{a,la}

%files
%license COPYING
%doc AUTHORS README.md README.SUSE
%dir %{_sysconfdir}/conky
%{_sysconfdir}/conky/convert.lua
%config(noreplace) %{_sysconfdir}/conky/conky.conf
%config(noreplace) %{_sysconfdir}/conky/conky_no_x11.conf
%{_bindir}/conky
%{_bindir}/conkyconf
%dir %{_libdir}/conky
%{_libdir}/conky/libcairo.so
%{_libdir}/conky/libcairo_imlib2_helper.so
%{_libdir}/conky/libcairo_xlib.so
%{_libdir}/conky/libimlib2.so
%{_libdir}/conky/librsvg.so
%{_datadir}/applications/conky.desktop
%{_datadir}/icons/hicolor/scalable/apps/conky-logomark-violet.svg
%{_datadir}/doc/conky-%{version}/
%{_libdir}/libtcp-portmon.so

%files doc
%doc %{_mandir}/man1/conky.1%{?ext_man}

%files -n vim-plugin-conky
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{_datadir}/vim/site/ftdetect
%{_datadir}/vim/site/ftdetect/conkyrc.vim

%files -n nano-plugin-conky
%dir %{_datadir}/nano
%{_datadir}/nano/conky.nanorc.j2

%changelog
