#
# spec file for package ffado-mixer
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


%define gcc7 0
%define docs 0
%define tname libffado
Name:           ffado-mixer
Version:        2.4.7
Release:        0
Summary:        FireWire 1394 support for audio devices, svn snapshot
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://www.ffado.org/
# NOTE: download of tarball is taken care of in ffado
Source0:        %{tname}-%{version}.tgz
# No current date and time allowed.
Patch0:         libffado-date_time.patch
# PATCH-FIX-UPSTREAM ffado-nosys.patch davejplater@gmail.com -- No import sys in SConstruct although functions are used.
Patch4:         ffado-nosys.patch
BuildRequires:  alsa-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  ffado = %{version}
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gnome
BuildRequires:  libavc1394-devel
BuildRequires:  libconfig++-devel
BuildRequires:  libdbus-c++-devel
BuildRequires:  libexpat-devel
BuildRequires:  libiec61883-devel >= 1.1.0
BuildRequires:  libraw1394-devel >= 1.3.0
BuildRequires:  pkg-config
BuildRequires:  python3-dbus-python-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  scons
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  xorg-x11-fonts
BuildRequires:  pkgconfig(libffado) = %{version}
BuildRequires:  pkgconfig(libxml++-3.0) >= 3.0.0
Requires:       ffado = %{version}
#Requires:       python-qt4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
FFADO aims to provide a generic, open-source solution
to support FireWire(IEEE1394, iLink) based (semi-)
professional audio interfaces.
It's the successor of the FreeBoB project. FFADO is a
volunteer-based community effort, trying to provide Linux
with at least the same level of functionality that is
present on the other operating systems.
The range of FireWire Audio Devices that we would like
to support is broad: from pure audio interfaces over
mixed audio-control devices to DSP algorithm devices.
This is a snapshot of svn revision 2040

%if %{docs} == 1
%package -n ffado-doc
Summary:        API documentation for ffado
Group:          Documentation/HTML
BuildArch:      noarch

%description -n ffado-doc
This package contains the libffado API documentation.
%endif

%prep
%setup -n %{tname}-%{version} -q
%autopatch -p0

for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

%build
export EXTRA_FLAGS="-Wno-deprecated-declarations -fpermissive --std=gnu++11"
%ifarch %arm
export EXTRA_FLAGS="${EXTRA_FLAGS} -fPIC"
%endif
%if %{gcc7} == 1
export CC=gcc-7
export CPP=cpp-7
export CXX=g++-7
%endif
scons %{_smp_mflags} \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  MANDIR=%{_mandir} \
  ENABLE_GENERICAVC=no \
  SERIALIZE_USE_EXPAT=no \
  DEBUG=no \
  ENABLE_ALL=no \
  DETECT_USERSPACE_ENV=False \
  PYPKGDIR=%{python3_sitelib} \
  ENABLE_OPTIMIZATIONS=yes \
  BUILD_TESTS=no \
  BUILD_MIXER=True \
  COMPILE_FLAGS="%{optflags} -fno-strict-aliasing -ggdb ${EXTRA_FLAGS}" \
  CUSTOM_ENV=True \
  PYTHON_INTERPRETER="%{_bindir}/python3"

%install
mkdir -p %{buildroot}%{python3_sitelib}
export EXTRA_FLAGS="-Wno-deprecated-declarations -fpermissive --std=gnu++11"
%ifarch %arm
export EXTRA_FLAGS="${EXTRA_FLAGS} -fPIC"
%endif
%if %{gcc7} == 1
export CC=gcc-7
export CPP=cpp-7
export CXX=g++-7
%endif

scons   DESTDIR=%{buildroot} install \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  MANDIR=%{_mandir} \
  ENABLE_GENERICAVC=no \
  SERIALIZE_USE_EXPAT=no \
  DEBUG=no \
  ENABLE_ALL=no \
  DETECT_USERSPACE_ENV=False \
  PYPKGDIR=%{python3_sitelib} \
  ENABLE_OPTIMIZATIONS=yes \
  BUILD_TESTS=no \
  BUILD_MIXER=True \
  COMPILE_FLAGS="%{optflags} -fno-strict-aliasing -ggdb ${EXTRA_FLAGS}" \
  CUSTOM_ENV=True \
  PYTHON_INTERPRETER="%{_bindir}/python3"

mv %{buildroot}%{_datadir}/%{tname}/icons %{buildroot}%{_datadir}/
rm %{buildroot}%{_libdir}/%tname.*
rm -r %{buildroot}%{_includedir}/libffado
rm -r %{buildroot}%{_libdir}/pkgconfig

# Remove the useless udev rules and man pages on the mixer package
rm -r %{buildroot}%{_mandir}
rm -r %{buildroot}/lib

rpm -ql ffado | while read file; do
  rm -v "%{buildroot}$file" || true
done

rm -rf %{buildroot}%{_libdir}/libffado

mkdir -p %{buildroot}%{_datadir}/applications/
 mkdir -p %{buildroot}%{_datadir}/pixmaps
 cp support/xdg/hi64-apps-ffado.png %{buildroot}%{_datadir}/pixmaps/ffadomixer.png
%suse_update_desktop_file -c ffadomixer FfadoMixer "Mixer for ffado" ffado-mixer ffadomixer "AudioVideo;Mixer;HardwareSettings;Qt"

# This problem seems to have been fixed in svn builds
%if 0 == 1
chmod 755 %{buildroot}%{_datadir}/%{tname}/python/ffado_configuration.py
chmod 755 %{buildroot}%{_datadir}/%{tname}/python/ffado_panelmanager.py
chmod 755 %{buildroot}%{_datadir}/%{tname}/python/ffado_dbus_util.py
%endif

find ./ -empty -delete
%fdupes -s %{buildroot}%{_datadir}

%python3_fix_shebang

%files
%defattr(-,root,root)
%{_bindir}/ffado-mixer
%{_datadir}/%{tname}/
%{_datadir}/icons/*
%{_datadir}/pixmaps/ffadomixer.png
%{_datadir}/applications/*
%{python3_sitelib}/*
%{_datadir}/metainfo/ffado-mixer.appdata.xml

%if %{docs} == 1
%files -n ffado-doc
%defattr(-,root,root)
%{_docdir}/%{tname}
%endif

%changelog
