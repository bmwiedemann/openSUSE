#
# spec file for package xonotic
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


%bcond_without systemd
Name:           xonotic
Version:        0.8.2
Release:        0
Summary:        Fast-paced first person shooter
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            http://xonotic.org/
Source0:        http://dl.xonotic.org/%{name}-%{version}.zip
Source1:        xonotic.desktop
Source2:        xonotic.service
Source3:        xonotic.init
Source4:        %{name}.changes
Source100:      xonotic.appdata.xml
BuildRequires:  SDL2-devel
BuildRequires:  alsa-devel
BuildRequires:  d0_blind_id-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  xorg-x11-libXpm
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zlib-devel
Requires:       logrotate
Requires:       xonotic-data = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%endif

%description
Fast-paced first-person shooter that works on Windows, OS X and Linux. The project is geared towards providing addictive arena shooter gameplay which is all spawned and driven by the community itself. Being a direct successor of the Nexuiz project with years of development between them, and it aims to become the best possible open-source FPS (first-person-shooter) of its kind.

%package server
Summary:        Dedicated xonotic server first person shooter
Group:          Amusements/Games/3D/Shoot
Requires(pre):  shadow
Requires:       xonotic-data = %{version}
%if %{with systemd}
 %{?systemd_requires}
%endif

%description server
Xonotic is a free (GPL), fast-paced first-person shooter that works on Windows, OS X and Linux. The project is geared towards providing addictive arena shooter gameplay which is all spawned and driven by the community itself. Xonotic is a direct successor of the Nexuiz project with years of development between them, and it aims to become the best possible open-source FPS (first-person-shooter) of its kind.

Server with dedicated xonotic running as services unter the specific user.
service is handle via systemd or init - depends on your version.

%package data
Summary:        Data for the xonotic first person shooter
Group:          Amusements/Games/3D/Shoot
BuildArch:      noarch

%description data
Xonotic is a free (GPL), fast-paced first-person shooter that works on Windows, OS X and Linux. The project is geared towards providing addictive arena shooter gameplay which is all spawned and driven by the community itself. Xonotic is a direct successor of the Nexuiz project with years of development between them, and it aims to become the best possible open-source FPS (first-person-shooter) of its kind.

Data (textures, maps, sounds and models) required to play xonotic.

%prep
%setup -q -n Xonotic
rm -rf misc/buildfiles/ # use system libs
sed -i \
		-e "/^EXE_/s:darkplaces:%{name}-%{version}:" \
		-e "s:-O3:%{optflags}:" \
		-e '/^STRIP/s/strip/true/' \
		source/darkplaces/makefile.inc
# do not include build time
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE4}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' | xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
make \
  %{?_smp_mflags} \
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
rm -rf %{buildroot}%{_datadir}/%{name}/server/help.cfg

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

%pre -n %{name}-server
%if %{with systemd}
 %service_add_pre %{name}-server.service
%endif

# Create user and group on the system if necessary
# default group: xonotic
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "Xonotic User" %{name}

# only 13.1 is able to work with service* commands:

%post -n %{name}-server
%if %{with systemd}
 %service_add_post %{name}-server.service
%else
 %{fillup_and_insserv -n %{name}-server }
%endif

%preun -n %{name}-server
%if %{with systemd}
 %service_del_preun %{name}-server.service
%else
 %stop_on_removal %{name}-server
%endif

%postun -n %{name}-server
%if %{with systemd}
 %service_del_postun %{name}-server.service
%else
 %restart_on_update %{name}-server
 %insserv_cleanup
%endif

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}-glx
%attr(755,root,root) %{_bindir}/%{name}-sdl
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc COPYING GPL-2 GPL-3

%files data
%defattr(0644, root, root, 0755)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/*
%doc COPYING GPL-2 GPL-3

%files server
%defattr(-,root,root,-)
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
%doc COPYING GPL-2 GPL-3 server/server.cfg server/help.cfg

%changelog
