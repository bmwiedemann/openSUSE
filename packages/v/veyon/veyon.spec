#
# spec file for package veyon
#
# Copyright (c) 2023 SUSE LLC
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


Name:           veyon
Version:        4.7.5
Release:        0
Summary:        Computer monitoring and classroom management
License:        GPL-2.0-or-later
URL:            https://veyon.io/
Source:         https://github.com/veyon/veyon/releases/download/v%{version}/veyon-%{version}-src.tar.bz2
Patch0:         harden_veyon.service.patch
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libfakekey-devel
BuildRequires:  libgsasl
BuildRequires:  libjpeg8-devel
BuildRequires:  libpng16-compat-devel
BuildRequires:  libpng16-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  procps-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-devel
%if 0%{?suse_version} > 1500
BuildRequires:  qca-qt6-plugins
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
%else
BuildRequires:  libqca-qt5-plugins
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(qca2-qt5)
%endif
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libvncclient)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       /usr/bin/pkexec
Requires(post): permissions
%{?systemd_requires}

%description
Veyon is a software for computer monitoring and classroom
management supporting Windows and Linux. It enables teachers to view and
control computer labs and interact with students. Veyon is available in
different languages. The user can:

* see what's going on in computer labs in overview mode and take screenshots
* remote control computers to support and help users
* broadcast the teacher's screen to students in realtime by using demo mode
  (either in fullscreen or in a window)
* lock workstations for attracting attention to teacher
* send text messages to students
* power on/off and rebooting computers remote
* remote logoff and remote execute arbitrary commands/scripts
* do home schooling

%prep
%autosetup -p1

%build
# explicitly enable PIC code and disable COTIRE precompiled headers since they
# somehow break PIC. MINIMUM_NUMBER_OF_TARGET_SOURCES workaround was the only
# I found to disable this without patching.
%cmake  -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
        -DSYSTEMD_SERVICE_INSTALL_DIR:PATH=%{_unitdir} \
        -DCMAKE_VEYON_X11VNC_EXTERNAL:BOOL=ON \
        -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
        -DCOTIRE_MINIMUM_NUMBER_OF_TARGET_SOURCES=9999 \
        -DWITH_PCH:BOOL=OFF \
%if 0%{?suse_version} > 1500
        -DWITH_QT6:BOOL=ON \
%endif
	. ../

%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r -G 'Remote desktop software' veyon-master Network RemoteAccess
%suse_update_desktop_file -r -G 'Remote desktop software' veyon-configurator Network RemoteAccess
mkdir -p %{buildroot}%{_sbindir}
pushd %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service rcveyon
popd

%verifyscript
%verify_permissions -e %{_bindir}/veyon-auth-helper

%pre
%service_add_pre veyon.service

%post
%service_add_post veyon.service
%if 0%{?set_permissions:1}
    %set_permissions %{_bindir}/veyon-auth-helper
%else
    %run_permissions
%endif

%preun
%service_del_preun veyon.service

%postun
%service_del_postun veyon.service

%files
%doc README*
%license COPYING
%{_bindir}/veyon-cli
%{_bindir}/veyon-configurator
%{_bindir}/veyon-master
%{_bindir}/veyon-server
%{_bindir}/veyon-service
%{_bindir}/veyon-worker
%verify(not user group mode) %attr(0711,root,root) %{_bindir}/veyon-auth-helper
%{_sbindir}/rcveyon
%{_libdir}/veyon/
%{_datadir}/applications/veyon-master.desktop
%{_datadir}/applications/veyon-configurator.desktop
%{_datadir}/pixmaps/veyon-*.xpm
%{_datadir}/polkit-1/actions/io.veyon.veyon-configurator.policy
%{_datadir}/icons/hicolor/*/apps/veyon*
%{_datadir}/veyon/
%{_unitdir}/veyon.service

%changelog
