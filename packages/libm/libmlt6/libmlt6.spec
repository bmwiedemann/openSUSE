#
# spec file for package libmlt6
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


%define _name mlt6
%define libname libmlt
%define lversion 6.26.1
%define sover 6
%define _name_pp mlt++
%define libname_pp lib%{_name_pp}
%define sover_pp 3

Name:           libmlt6
Version:        6.26.1
Release:        0
Summary:        Multimedia framework for television broadcasting
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            http://www.mltframework.org
Source0:        https://github.com/mltframework/mlt/archive/v%{version}.tar.gz#/mlt-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libmlt-fixluma.patch aloisio@gmx.com -- add LD_LIBRARY_PATH so that luma can run
Patch2:         libmlt-fixluma.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(Qt5Core) >= 5.10
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(frei0r)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libdv)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libquicktime)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(movit)
#!BuildIgnore:  opencv-qt5-devel
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavdevice) >= 58
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil) >= 56
BuildRequires:  pkgconfig(libpostproc) >= 55
BuildRequires:  pkgconfig(libswscale) >= 5
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sox)
BuildRequires:  pkgconfig(vidstab)
BuildRequires:  pkgconfig(vorbisfile)

%description
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers. The functionality of the system is
provided via an assortment of tools, XML authoring components, and an
plug-in based API.

#Main package name correct
%if 0
%package -n %{libname}%{sover}
Summary:        C library API for the MLT multimedia framework
Group:          System/Libraries

%description -n %{libname}%{sover}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the C library API for MLT.
%endif

%package devel
Summary:        Development files for MLT's C language API
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{sover} = %{version}

%description devel
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the headers to make use of the MLT C API.

%package -n %{libname_pp}%{sover_pp}
Summary:        C++ library API for the MLT multimedia framework
Group:          System/Libraries

%description -n %{libname_pp}%{sover_pp}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the C++ library API for MLT.

%package -n %{libname_pp}-devel
Summary:        Development files for MLT's C++ language API
Group:          Development/Libraries/C and C++
Requires:       %{libname_pp}%{sover_pp} = %{version}
Requires:       pkgconfig(mlt-framework) = %{version}

%description -n %{libname_pp}-devel
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the headers to make use of the MLT C++ API.

%package -n melt6
Summary:        Multimedia framework for television broadcasting
Group:          Productivity/Multimedia/Video/Editors and Convertors
Provides:       melt = %{version}
Obsoletes:      melt < %{version}
Requires:       %{libname}%{sover}-data = %{version}
Requires:       %{libname}%{sover}-modules = %{version}

%description -n melt6
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

The functionality of the system is provided via an assortment of
tools, XML authoring components, and an plug-in based API.

%package -n %{libname}%{sover}-modules
Summary:        Modules for the MLT multimedia framework
Group:          Productivity/Multimedia/Video/Editors and Convertors
Recommends:     frei0r-plugins
Provides:       mlt(%{sover})(avformat)

%description -n %{libname}%{sover}-modules
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

The functionality of the system is provided via an assortment of
tools, XML authoring components, and an plug-in based API.

%package -n %{libname}%{sover}-data
Summary:        Architecture-independent data files for the MLT multimedia framework
Group:          Productivity/Multimedia/Video/Editors and Convertors
BuildArch:      noarch

%description -n %{libname}%{sover}-data
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

%package -n python3-mlt6
Summary:        Python bindings for the MLT multimedia framework
Group:          Development/Languages/Python
BuildRequires:  python3-devel
BuildRequires:  swig
Requires:       %{libname_pp}%{sover_pp} >= %{version}
Requires:       %{libname}%{sover} >= %{version}
Provides:       python3-mlt = %{version}
Obsoletes:      python3-mlt < %{version}

%description -n python3-mlt6
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.
This package contains python bindings.

%prep
%autosetup -p1 -n mlt-%{version}

%build
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7

# Until boo#1179650 is fixed
%ifarch ppc64le
export CFLAGS="-I%{_includedir}/eigen3"
%endif

# WARNING: building opencv module causes multicore issues - boo#1068792
%configure --disable-opencv \
--enable-sdl2 \
%ifnarch %{ix86} x86_64
  --disable-mmx \
  --disable-sse \
  --disable-sse2 \
%endif
--enable-debug \
--enable-gpl --enable-gpl3 \
--enable-lumas \
%ifarch i586
--disable-mmx \
%endif
--enable-extra-versioning \
--swig-languages=python \

make %{?_smp_mflags}

%install
%make_install
install -Dpm 0644 src/swig/python/_mlt.so '%{buildroot}%{python3_sitearch}/_mlt.so'
install -Dpm 0644 src/swig/python/mlt.py '%{buildroot}%{python3_sitearch}/mlt.py'

# Get the modules that need data
for MODULE in %{buildroot}%{_libdir}/mlt-%{sover}/libmlt*.so; do
  echo $MODULE
  MODULEDIR=%{_datadir}/mlt-%{sover}/$(echo $MODULE | sed 's|%{buildroot}%{_libdir}/mlt-%{sover}/libmlt\(.*\).so|\1|')
  echo $MODULEDIR
  if [ -e %{buildroot}$MODULEDIR ]; then
    echo Done $MODULEDIR
    echo $MODULEDIR >> module_data.dirs
  fi;
done

# Pure data modules
for MODULE in feeds lumas; do
    echo %{_datadir}/mlt-%{sover}/$MODULE >> module_data.dirs
done

# Remove the unversioned symbolic links
rm -f %{buildroot}%{_libdir}/mlt
rm -f %{buildroot}%{_datadir}/mlt

# Remove the melt symlink. This is now used by libmlt7
rm %{buildroot}%{_bindir}/melt

# remove dupes
%fdupes -s %{buildroot}%{_datadir}/mlt-6

%post -n %{libname_pp}%{sover_pp} -p /sbin/ldconfig
%post -n %{libname}%{sover} -p /sbin/ldconfig
%postun -n %{libname_pp}%{sover_pp} -p /sbin/ldconfig
%postun -n %{libname}%{sover} -p /sbin/ldconfig

%files
%defattr(0644, root, root, 0755)
%{_libdir}/libmlt.so.%{sover}
%{_libdir}/libmlt.so.%{lversion}

%files devel
%defattr(0644, root, root, 0755)
%{_libdir}/libmlt.so
%{_includedir}/mlt
%{_libdir}/pkgconfig/mlt-framework.pc

%files -n %{libname_pp}%{sover_pp}
%defattr(0644, root, root, 0755)
%{_libdir}/lib%{_name_pp}.so.%{sover_pp}
%{_libdir}/lib%{_name_pp}.so.%{lversion}

%files -n %{libname_pp}-devel
%defattr(0644, root, root, 0755)
%{_libdir}/lib%{_name_pp}.so
%{_includedir}/%{_name_pp}
%{_libdir}/pkgconfig/%{_name_pp}.pc

%files -n melt6
%defattr(0644, root, root, 0755)
%attr(0755, root, root) %{_bindir}/melt%{sover}

%files -n %{libname}%{sover}-modules -f module_data.dirs
%defattr(0644, root, root, 0755)
%doc AUTHORS NEWS README
%license GPLv3 COPYING GPL
%{_libdir}/mlt-%{sover}/
%dir %{_datadir}/mlt-%{sover}/

%files -n %{libname}%{sover}-data
%defattr(0644, root, root, 0755)
%dir %{_datadir}/mlt-%{sover}/
%{_datadir}/mlt-%{sover}/metaschema.yaml
%{_datadir}/mlt-%{sover}/profiles/
%{_datadir}/mlt-%{sover}/presets/
%{_datadir}/mlt-%{sover}/vid.stab/

%files -n python3-mlt6
%defattr(0644, root, root, 0755)
%{python3_sitearch}/_mlt.so
%{python3_sitearch}/mlt.py

%changelog
