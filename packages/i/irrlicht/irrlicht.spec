#
# spec file for package irrlicht
#
# Copyright (c) 2021 SUSE LLC
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


#
%define  sover 1_8
%define  libver 1.8
Name:           irrlicht
Version:        1.8.5
Release:        0
Summary:        A realtime 3D engine
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://irrlicht.sourceforge.io/
Source0:        https://downloads.sourceforge.net/irrlicht/%{name}-%{version}.zip
# PATCH-FIX-OPENSUSE irrlicht-1.7.9.3629-config.patch -- use system libraries http://irrlicht.sourceforge.net/phpBB2/viewtopic.php?t=24076
Patch0:         irrlicht-1.7.9.3629-config.patch
# PATCH-FIX-UPSTREAM irrlicht-1.8-directionlight.patch
Patch1:         irrlicht-1.8-directionlight.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  unzip
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xxf86vm)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Irrlicht Engine is a realtime 3D engine written and usable in C++
and also available for .NET languages. It is using Direct3D, OpenGL
and its own software renderer, and has features which can be found in
commercial 3D engines, some of which are:
* Built-in and extensible material library with vertex, pixel, and
  geometry shader support
* Character animation system with skeletal and morph target animation.
* Particle effects, billboards, light maps, environment mapping,
  stencil buffer shadows, and lots of other special effects.
* Direct import of common mesh file formats: Maya (.obj), 3DStudio
  (.3ds), COLLADA (.dae), Blitz3D (.b3d), Milkshape (.ms3d), Quake 3
  levels (.bsp), Quake2 models (.md2), Microsoft DirectX (.X)…

%package devel
Summary:        Development headers and libraries for irrlicht
Group:          Development/Libraries/C and C++
Requires:       libIrrlicht%{sover} = %{version}
Requires:       libstdc++-devel

%description devel
Development headers and libraries for irrlicht.

The Irrlicht Engine is a realtime 3D engine written and usable in C++
and also available for .NET languages. It is using Direct3D, OpenGL
and its own software renderer, and has features which can be found in
commercial 3D engines.

%package data
Summary:        Assorted data for irrlicht
Group:          Development/Libraries/C and C++

%description data
Data files for irrlicht applications

The Irrlicht Engine is a realtime 3D engine written and usable in C++
and also available for .NET languages. It is using Direct3D, OpenGL
and its own software renderer, and has features which can be found in
commercial 3D engines.

%package -n libIrrlicht%{sover}
Summary:        A high performance realtime 3D engine
Group:          System/Libraries

%description -n libIrrlicht%{sover}
The Irrlicht Engine is a realtime 3D engine written and usable in C++
and also available for .NET languages. It is using Direct3D, OpenGL
and its own software renderer, and has features which can be found in
commercial 3D engines.

%prep
%setup -q
%patch -P 0
%patch -P 1 -p1

sed -i 's/\r//' readme.txt
iconv -o readme.txt.iso88591 -f iso88591 -t utf8 readme.txt
mv readme.txt.iso88591 readme.txt
# We don't use any of this. Deleting it to be sure we are using system headers
rm -rf source/Irrlicht/jpeglib source/Irrlicht/zlib source/Irrlicht/libpng
for i in include/*.h doc/upgrade-guide.txt source/Irrlicht/*.cpp source/Irrlicht/*.h; do
	sed -i 's/\r//' $i
	chmod -x $i
	touch -r changes.txt $i
done

%build
cd source/Irrlicht
make %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing -fPIC" \
      ZLIBOBJ= JPEGLIBOBJ= LIBPNGOBJ= \
      CIrrDeviceLinux.cpp
make %{?_smp_mflags} \
     CFLAGS="%{optflags} -fstrict-aliasing -fPIC" \
     CXXFLAGS="%{optflags} -fstrict-aliasing -fno-exceptions -fno-rtti -fPIC" \
     ZLIBOBJ= JPEGLIBOBJ= LIBPNGOBJ= \
     LDFLAGS="-lz -ljpeg -lpng $(pkg-config --libs gl xxf86vm xext x11)" \
     sharedlib

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/irrlicht
make -C source/Irrlicht INSTALL_DIR=%{buildroot}%{_libdir} install \
     ZLIBOBJ= JPEGLIBOBJ= LIBPNGOBJ=
# Cleaning up after the really bad installer...
pushd %{buildroot}%{_libdir}
ln -s -f libIrrlicht.so.%{version} libIrrlicht.so.%{libver}
ln -s -f libIrrlicht.so.%{libver} libIrrlicht.so
popd
# End Makefile mess cleanup
install -d %{buildroot}%{_datadir}/irrlicht
cp -r media %{buildroot}%{_datadir}/irrlicht

%fdupes %{buildroot}%{_includedir}

%post -n libIrrlicht%{sover} -p /sbin/ldconfig
%postun -n libIrrlicht%{sover} -p /sbin/ldconfig

%files -n libIrrlicht%{sover}
%defattr(-,root,root,-)
%doc readme.txt
%{_libdir}/libIrrlicht.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/upgrade-guide.txt
%{_includedir}/irrlicht/
%{_libdir}/libIrrlicht.so

%files data
%defattr(-,root,root,-)
%{_datadir}/irrlicht

%changelog
