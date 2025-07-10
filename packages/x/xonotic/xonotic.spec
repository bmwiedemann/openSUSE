#
# spec file for package xonotic
#
# Copyright (c) 2025 SUSE LLC
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


# Because "-std=gnu17" we need a c++17 compiler at least
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%global force_gcc_version 13
%endif

%bcond_without systemd
Name:           xonotic
Version:        0.8.6
Release:        0
Summary:        Fast-paced first person shooter
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://xonotic.org/
Source0:        https://dl.xonotic.org/%{name}-%{version}.zip
Source1:        xonotic.desktop
Source2:        xonotic.service
Source3:        xonotic.init
Source4:        %{name}.changes
Source100:      xonotic.appdata.xml
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  libcurl-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(d0_blind_id)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
Requires:       logrotate
Requires:       xonotic-data = %{version}
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%endif
Provides:       group(%{name})
Provides:       user(%{name})

%description
Fast-paced first-person shooter. It provides arena shooter gameplay
and is a direct successor of the Nexuiz project.

%package server
Summary:        Dedicated server for the Xonotic first person shooter
Group:          Amusements/Games/3D/Shoot
Requires:       xonotic-data = %{version}
Requires(pre):  shadow
%if %{with systemd}
 %{?systemd_requires}
%endif

%description server
Fast-paced first-person shooter. It provides arena shooter gameplay
and is a direct successor of the Nexuiz project.

This subpackage contains the server with dedicated xonotic running as
services unter the specific user. The service is handle via systemd or
init, depending on your version.

%package data
Summary:        Data for the xonotic first person shooter
Group:          Amusements/Games/3D/Shoot
BuildArch:      noarch

%description data
Fast-paced first-person shooter. It provides arena shooter gameplay
and is a direct successor of the Nexuiz project.

This subpackage contains data (textures, maps, sounds and models)
required to play xonotic.

%prep
%autosetup -n Xonotic -p1
rm -rf misc/buildfiles/ # use system libs
sed -i \
		-e "/^EXE_/s:darkplaces:%{name}-%{version}:" \
		-e "s:-O3:%{optflags} -std=gnu17:" \
		-e '/^STRIP/s/strip/true/' \
		source/darkplaces/makefile.inc
# do not include build time
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE4}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' | xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{force_gcc_version}"
export CXX="g++-%{force_gcc_version}"
%endif

%make_build \
  DP_LINK_TO_LIBJPEG=1 \
  DP_LINK_CRYPTO=shared \
  DP_FS_BASEDIR="%{_datadir}/xonotic" \
  -C source/darkplaces \
  sv-release \
  cl-release \
  sdl-release

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 source/darkplaces/%{name}-%{version}-glx \
%{buildroot}%{_bindir}/xonotic-glx
install -m 755 source/darkplaces/%{name}-%{version}-sdl \
%{buildroot}%{_bindir}/xonotic-sdl
install -m 755 source/darkplaces/%{name}-%{version}-dedicated \
%{buildroot}%{_bindir}/xonotic-dedicated
install -D -m 644 misc/logos/%{name}_icon.svg \
%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -p -m 644 %{SOURCE100}  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/xonotic
cp -r key_0.d0pk server data %{buildroot}%{_datadir}/%{name}

rm -rf %{buildroot}%{_datadir}/%{name}/server/.gitattributes
rm -rf %{buildroot}%{_datadir}/%{name}/server/readme.txt
rm -rf %{buildroot}%{_datadir}/%{name}/server/server_windows.bat
rm -rf %{buildroot}%{_datadir}/%{name}/server/server.cfg

mkdir -p  %{buildroot}%{_localstatedir}/lib/%{name}

%if %{with systemd}
 install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-server.service
 mkdir %{buildroot}%{_sbindir}
 ln -sv  %{_unitdir}/%{name}-server.service %{buildroot}/%{_sbindir}/rc%{name}-server
%else
 install -D -p -m 0755 %{SOURCE3} %{buildroot}/%{_initddir}/%{name}-server
 mkdir %{buildroot}%{_sbindir}
 ln -sv  %{_initddir}/%{name}-server %{buildroot}/%{_sbindir}/rc%{name}-server
%endif

%if 0%{?suse_version}
 %suse_update_desktop_file -i %{name} Game ActionGame
%endif

%pre server
%if %{with systemd}
 %service_add_pre %{name}-server.service
%endif

# Create user and group on the system if necessary
# default group: xonotic
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "Xonotic User" %{name}

# only 13.1 is able to work with service* commands:

%post server
%if %{with systemd}
 %service_add_post %{name}-server.service
%else
 %{fillup_and_insserv -n %{name}-server }
%endif

%preun server
%if %{with systemd}
 %service_del_preun %{name}-server.service
%else
 %stop_on_removal %{name}-server
%endif

%postun server
%if %{with systemd}
 %service_del_postun %{name}-server.service
%else
 %restart_on_update %{name}-server
 %insserv_cleanup
%endif

%files
%attr(755,root,root) %{_bindir}/%{name}-glx
%attr(755,root,root) %{_bindir}/%{name}-sdl
%license COPYING GPL-2 GPL-3
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files data
%defattr(0644, root, root, 0755)
%license COPYING GPL-2 GPL-3
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/*

%files server
%attr(755,root,root) %{_bindir}/%{name}-dedicated
%if %{with systemd}
%{_unitdir}/%{name}-server.service
%else
%attr(755,root,root) /%{_initddir}/%{name}-server
%endif
%{_sbindir}/rc%{name}-server
%attr(711,xonotic,xonotic) %dir %{_localstatedir}/lib/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/server
%{_datadir}/%{name}/server/rcon2irc
%attr(755,root,root) %{_datadir}/%{name}/server/rcon2irc/rcon2irc.pl
%attr(755,root,root) %{_datadir}/%{name}/server/server_linux.sh
%attr(755,root,root) %{_datadir}/%{name}/server/rcon.pl
%attr(755,root,root) %{_datadir}/%{name}/server/server_mac.sh
%{_datadir}/%{name}/key_0.d0pk
%license COPYING GPL-2 GPL-3
%doc server/server.cfg

%changelog
