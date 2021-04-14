#
# spec file for package libmlt
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


%define _name mlt
%define libname lib%{_name}
%define lversion 6.26.1
%define soname 6
%define _name_pp %{_name}++
%define libname_pp lib%{_name_pp}
%define soname_pp 3

Name:           %{libname}
Version:        6.26.1
Release:        0
Summary:        Multimedia framework for television broadcasting
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.mltframework.org
Source0:        https://github.com/mltframework/mlt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libmlt-fixluma.patch aloisio@gmx.com -- add LD_LIBRARY_PATH so that luma can run
Patch2:         libmlt-fixluma.patch
BuildRequires:  fdupes
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
#!Buildignore:  libgcc_s1
%endif
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

%package -n %{libname}%{soname}
Summary:        C library API for the MLT multimedia framework
Group:          System/Libraries

%description -n %{libname}%{soname}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the C library API for MLT.

%package devel
Summary:        Development files for MLT's C language API
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{soname} = %{version}

%description devel
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the headers to make use of the MLT C API.

%package -n %{libname_pp}%{soname_pp}
Summary:        C++ library API for the MLT multimedia framework
Group:          System/Libraries

%description -n %{libname_pp}%{soname_pp}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the C++ library API for MLT.

%package -n %{libname_pp}-devel
Summary:        Development files for MLT's C++ language API
Group:          Development/Libraries/C and C++
Requires:       %{libname_pp}%{soname_pp} = %{version}
Requires:       %{libname}-devel = %{version}

%description -n %{libname_pp}-devel
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the headers to make use of the MLT C++ API.

%package -n melt
Summary:        Multimedia framework for television broadcasting
Group:          Productivity/Multimedia/Video/Editors and Convertors
Provides:       melt%{soname} = %{version}
Obsoletes:      melt%{soname} < %{version}
Requires:       %{libname}%{soname}-data = %{version}
Requires:       %{libname}%{soname}-modules = %{version}

%description -n melt
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

The functionality of the system is provided via an assortment of
tools, XML authoring components, and an plug-in based API.

%package -n %{libname}%{soname}-modules
Summary:        Modules for the MLT multimedia framework
Group:          Productivity/Multimedia/Video/Editors and Convertors
Recommends:     frei0r-plugins
Provides:       mlt(%{soname})(avformat)

%description -n %{libname}%{soname}-modules
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

The functionality of the system is provided via an assortment of
tools, XML authoring components, and an plug-in based API.

%package -n %{libname}%{soname}-data
Summary:        Architecture-independent data files for the MLT multimedia framework
Group:          Productivity/Multimedia/Video/Editors and Convertors
BuildArch:      noarch

%description -n %{libname}%{soname}-data
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

%package -n python3-%{_name}
Summary:        Python bindings for the MLT multimedia framework
Group:          Development/Languages/Python
BuildRequires:  python3-devel
BuildRequires:  swig
Requires:       %{libname_pp}%{soname_pp} >= %{version}
Requires:       %{libname}%{soname} >= %{version}
Provides:       python3-%{_name}%{soname}

%description -n python3-%{_name}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.
This package contains python bindings.

%prep
%setup -q -n %{_name}-%{version}
%autopatch -p1

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
--swig-languages=python
make %{?_smp_mflags}

%install
%make_install
install -Dpm 0644 docs/melt.1 %{buildroot}%{_mandir}/man1/melt%{soname}.1
ln -s melt%{soname}.1 %{buildroot}%{_mandir}/man1/melt.1
install -Dpm 0644 src/swig/python/_%{_name}.so '%{buildroot}%{python3_sitearch}/_%{_name}.so'
install -Dpm 0644 src/swig/python/%{_name}.py '%{buildroot}%{python3_sitearch}/%{_name}.py'

# Get the modules that need data
for MODULE in %{buildroot}%{_libdir}/mlt-%{soname}/libmlt*.so; do
  echo $MODULE
  MODULEDIR=%{_datadir}/mlt-%{soname}/$(echo $MODULE | sed 's|%{buildroot}%{_libdir}/mlt-%{soname}/libmlt\(.*\).so|\1|')
  echo $MODULEDIR
  if [ -e %{buildroot}$MODULEDIR ]; then
    echo Done $MODULEDIR
    echo $MODULEDIR >> module_data.dirs
  fi;
done

# Pure data modules
for MODULE in feeds lumas; do
    echo %{_datadir}/mlt-%{soname}/$MODULE >> module_data.dirs
done

# Remove the unversioned symbolic links
rm -f %{buildroot}%{_libdir}/mlt
rm -f %{buildroot}%{_datadir}/mlt

# remove dupes
%fdupes -s %{buildroot}%{_datadir}/mlt-6

%post -n %{libname}%{soname} -p /sbin/ldconfig

%postun -n %{libname}%{soname} -p /sbin/ldconfig

%post -n %{libname_pp}%{soname_pp} -p /sbin/ldconfig

%postun -n %{libname_pp}%{soname_pp} -p /sbin/ldconfig

%files -n %{libname}%{soname}
%defattr(0644, root, root, 0755)
%{_libdir}/lib%{_name}.so.%{soname}
%{_libdir}/lib%{_name}.so.%{lversion}

%files devel
%defattr(0644, root, root, 0755)
%{_libdir}/lib%{_name}.so
%{_includedir}/%{_name}
%{_libdir}/pkgconfig/%{_name}-framework.pc

%files -n %{libname_pp}%{soname_pp}
%defattr(0644, root, root, 0755)
%{_libdir}/lib%{_name_pp}.so.%{soname_pp}
%{_libdir}/lib%{_name_pp}.so.%{lversion}

%files -n %{libname_pp}-devel
%defattr(0644, root, root, 0755)
%{_libdir}/lib%{_name_pp}.so
%{_includedir}/%{_name_pp}
%{_libdir}/pkgconfig/%{_name_pp}.pc

%files -n melt
%defattr(0644, root, root, 0755)
%attr(0755, root, root) %{_bindir}/melt%{soname}
%{_mandir}/man1/melt%{soname}.1%{ext_man}
%{_bindir}/melt
%{_mandir}/man1/melt.1%{ext_man}

%files -n %{libname}%{soname}-modules -f module_data.dirs
%defattr(0644, root, root, 0755)
%doc AUTHORS NEWS README
%license GPLv3 COPYING GPL
%{_libdir}/%{_name}-%{soname}/
%dir %{_datadir}/%{_name}-%{soname}/

%files -n %{libname}%{soname}-data
%defattr(0644, root, root, 0755)
%dir %{_datadir}/%{_name}-%{soname}/
%{_datadir}/%{_name}-%{soname}/metaschema.yaml
%{_datadir}/%{_name}-%{soname}/profiles/
%{_datadir}/%{_name}-%{soname}/presets/
%{_datadir}/%{_name}-%{soname}/vid.stab/

%files -n python3-%{_name}
%defattr(0644, root, root, 0755)
%{python3_sitearch}/_%{_name}.so
%{python3_sitearch}/%{_name}.py

%changelog
