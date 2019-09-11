#
# spec file for package FlightGear
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


%define main_version 2018.3
Name:           FlightGear
Version:        %{main_version}.2
Release:        0
Summary:        Flight Simulator
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Simulation
Url:            http://www.flightgear.org/
Source0:        https://sourceforge.net/projects/flightgear/files/release-%{main_version}/flightgear-%{version}.tar.bz2
Source1:        %{name}.desktop

BuildRequires:  SimGear-devel = %{version}
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  plib-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
# Required for screensaver inhibition
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
%if 0%{?suse_version} > 1330
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

# Additional dependencies to enable FlightGear's new Qt launcher interface
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)

Recommends:     FlightGear-data = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The FlightGear project is working to create a sophisticated flight
simulator framework for the development and pursuit of interesting
flight simulator ideas. We are developing a solid basic sim that can be
expanded and improved upon by anyone interested in contributing

%prep
%setup -q -n flightgear-%{version}

# remove some unneeded doc files
for ext in Cygwin IRIX Joystick Linux MSVC MSVC8 MacOS SimGear Unix Win32-X autoconf mingw plib src xmlsyntax; do
  rm -f docs-mini/README.${ext}
done

%build
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
# sed -i -e "s@__DATE__@$DATE@g" -e "s@__TIME__@$TIME@g" utils/fgcom/fgcom.cxx src/FDM/JSBSim/FGJSBBase.cpp

# remove FlightGear's default .desktop file (we ship our own)
rm package/org.flightgear.FlightGear.desktop
echo "# .desktop file removed for openSUSE" > package/CMakeLists.txt

%cmake \
    -DFG_DATA_DIR:STRING="%{_datadir}/flightgear" \
    -DSYSTEM_SQLITE:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_TESTING:BOOL=OFF \
    -DENABLE_JS_DEMO:BOOL=OFF \
    -DENABLE_GPSSMOOTH:BOOL=OFF \
    -DENABLE_FGVIEWER:BOOL=OFF \
    -DENABLE_FGELEV:BOOL=OFF \
    -DENABLE_METAR:BOOL=OFF
make %{?_smp_mflags}

%install
%cmake_install
# install icons
install -m 0755 -d %{buildroot}%{_datadir}/icons/hicolor/
pushd icons
cp -r -t %{buildroot}%{_datadir}/icons/hicolor/ 16x16 32x32 48x48 64x64 128x128 scalable
popd
# install desktop file
%suse_update_desktop_file -i %{name}
# remove obsolete utilities
cd %{buildroot}%{_bindir} && rm -f GPSsmooth MIDGsmooth UGsmooth metar yasim yasim-proptest

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README Thanks docs-mini/*
%license COPYING
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/it/man1/*
%{_mandir}/it/man5/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/bash-completion/completions/fgfs
%{_datadir}/zsh/site-functions/_fgfs

%changelog
