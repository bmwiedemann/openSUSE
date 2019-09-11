#
# spec file for package librepilot
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           librepilot
Version:        16.09
Release:        0
Summary:        Software to control multicopter and other RC models
License:        GPL-3.0-only
Group:          Development/Tools/IDE
Url:            https://www.librepilot.org
Source:         %name-%{version}.tar.xz
Patch:          fix_build_with_qt59.patch
%if 0%{?fedora_version}
BuildRequires:  python2
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd-devel
%else
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libudev-devel
BuildRequires:  python < 3
%endif
BuildRequires:  SDL-devel
BuildRequires:  libusb-devel
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
LibrePilot is a software suite to control multicopter and other RC
(remote controlled) models.
It is a fork of the prior OpenPilot project.
While supporting the new flight controllers, it supports also the older again:
 CopterControl, CC3D, Atom, Revolution, Revolution Nano, Platinum GPS (V9) and OPLink Modems

Documentation can be found at
http://opwiki.readthedocs.org/en/latest/user_manual/index.html

%prep
%setup -q
%if 0%{?suse_version} >= 1330
%patch -p0
%endif
mkdir build

%build
cd build
qmake-qt5 PREFIX=/usr LIBDIR=%_libdir ../ground/ground.pro
make %{?_smp_mflags}

%install
cd build
mkdir -p %{buildroot}/usr
cp -av gcs/{bin,lib,share} %{buildroot}/usr/
# install icon
mkdir -p %{buildroot}/usr/share/{applications,pixmaps}/
install -m 0644 ../package/linux/gcs.desktop %{buildroot}/usr/share/applications/
install -m 0644 ../artwork/Logo/LP_logo_square.png %{buildroot}/usr/share/pixmaps/org.png
sed -i -e 's/^Categories=.*/Categories=Building;Development;/' %{buildroot}/usr/share/applications/*desktop

%if "%{_lib}" == "lib64" 
# workaround wrong built in defaults for now
mv %{buildroot}/usr/lib %{buildroot}%{_prefix}/lib64
mkdir -p %{buildroot}%{_prefix}/lib
ln -sf ../lib64/gcs %buildroot%{_prefix}/lib/gcs 
%endif

%files
%license GPLv3.txt LICENSE.txt
%doc README.md WHATSNEW.txt CREDITS.txt
%_bindir/*
%if "%{_lib}" == "lib64" 
%{_prefix}/lib/gcs
%endif
%_libdir/gcs
%_datadir/applications/*
%_datadir/pixmaps/*
%_datadir/gcs/

%changelog
