#
# spec file for package povray
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


%define maj_version 3.7
%define min_version 0.0
Name:           povray
Version:        %{maj_version}.%{min_version}
Release:        0
Summary:        Ray Tracer
License:        AGPL-3.0 and CC-BY-SA-3.0
Group:          Productivity/Graphics/Visualization/Raytracers
Url:            http://www.povray.org
Source:         https://github.com/POV-Ray/povray/archive/v%{version}.tar.gz
Patch1:         povray-3.6.9.7-ini.patch
Patch2:         povray-3.6.9.7-fix.patch
# make boost link
Patch4:         povray-3.6.9.7-boost-link.patch
# PATCH-FIX-UPSTREAM bmwiedemann
Patch5:         reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXpm-devel
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Persistence of Vision Ray tracer creates three-dimensional,
photo-realistic images using a rendering technique called ray tracing.
It reads in a text file containing information describing the objects
and lighting in a scene and generates an image of that scene from the
view point of a camera also described in the text file. Ray tracing is
not a fast process by any means, (the generation of a complex image can
take several hours) but it produces very high quality images with
realistic reflections, shading, perspective, and other effects.

%prep
%setup -q
%patch1
%patch2
%patch4
%patch5 -p1

# remove inline copies of shared libraries
rm -rf libraries

# add missing standard files
sed -i 's,automake --warnings=all,automake --warnings=all --add-missing,' \
    unix/prebuild.sh

# fix wrong newline encoding
dos2unix -k unix/scripts/*.sh

%build
( cd unix && ./prebuild.sh )
%ifarch %arm
# work around ICE
RPM_OPT_FLAGS="%{optflags} -O1"
%endif
CXXFLAGS="%{optflags} -fno-strict-aliasing -Wno-multichar -std=c++03" CFLAGS="$CXXFLAGS" \
    %configure \
    COMPILED_BY="SUSE LINUX GmbH, Nuernberg, Germany" \
    --disable-strip \
    --disable-optimiz \
    --with-boost-libdir=%{_libdir}

# fix up paths
sed -i -e 's,^DEFAULT_DIR=.*,DEFAULT_DIR=/usr,' scripts/*
sed -i -e 's,^SYSCONFDIR=.*,SYSCONFDIR=/etc,' scripts/*

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} \
     povdocdir=/deleteme \
     install

# this only contains the AUTHORS and changelog files, not the actual
# documentation
rm -rf %{buildroot}/deleteme

# fix wrong permissions
chmod 755 %{buildroot}%{_datadir}/povray-%{maj_version}/scenes/camera/mesh_camera/bake.sh

%fdupes %{buildroot}/%{_datadir}

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md changes.txt revision.txt
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{maj_version}
%config(noreplace) %{_sysconfdir}/%{name}/%{maj_version}/%{name}.*
%{_bindir}/povray
%{_datadir}/povray-%{maj_version}
%{_mandir}/man1/povray.1*

%changelog
