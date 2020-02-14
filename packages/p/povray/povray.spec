#
# spec file for package povray
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


%define maj_version 3.7
%define min_version 0.8
Name:           povray
Version:        %{maj_version}.%{min_version}
Release:        0
Summary:        Persistence of Vision Raytracer
License:        AGPL-3.0-or-later AND CC-BY-SA-3.0
Group:          Productivity/Graphics/Visualization/Raytracers
URL:            http://www.povray.org
Source:         https://github.com/POV-Ray/povray/archive/v%{version}.tar.gz
Patch1:         povray-3.6.9.7-ini.patch
Patch2:         povray-3.6.9.7-fix.patch
# PATCH-FIX-UPSTREAM bmwiedemann
Patch5:         reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXpm-devel
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(zlib)
Recommends:     povray-doc

%description
The Persistence of Vision Ray tracer creates three-dimensional,
photo-realistic images using a rendering technique called ray tracing.
It reads in a text file containing information describing the objects
and lighting in a scene and generates an image of that scene from the
view point of a camera also described in the text file. Ray tracing is
not a fast process by any means, (the generation of a complex image can
take several hours) but it produces very high quality images with
realistic reflections, shading, perspective, and other effects.

%package doc
Summary:        Documentation for POV-Ray
Group:          Documentation/HTML

%description doc
This package contains the Povray documentation.

%prep
%setup -q
%patch1
%patch2
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
%configure \
    COMPILED_BY=%{vendor} \
    --disable-strip \
    --disable-optimiz \
    --with-boost-libdir=%{_libdir}

# fix up paths
sed -i -e 's,^DEFAULT_DIR=.*,DEFAULT_DIR=/usr,' scripts/*
sed -i -e 's,^SYSCONFDIR=.*,SYSCONFDIR=/etc,' scripts/*

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} \
     povdocdir=%{_defaultdocdir}/povray \
     install

# fix wrong permissions
chmod 755 %{buildroot}%{_datadir}/povray-%{maj_version}/scenes/camera/mesh_camera/bake.sh

%fdupes %{buildroot}/%{_datadir}

%files
%doc AUTHORS README.md changes.txt revision.txt
%doc %{_defaultdocdir}/povray/{ChangeLog,NEWS}
%license LICENSE
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{maj_version}
%config(noreplace) %{_sysconfdir}/%{name}/%{maj_version}/%{name}.*
%{_bindir}/povray
%{_datadir}/povray-%{maj_version}
%{_mandir}/man1/povray.1*
%exclude %{_defaultdocdir}/povray/html

%files doc
%{_defaultdocdir}/povray/html

%changelog
