#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%define lversion 7.12.0
%define sover 7
%define lib_pkgname %{libname}-%{sover}-%{sover}
%define _name_pp %{_name}++
%define libname_pp lib%{_name_pp}
%define sover_pp 7
%define lversion_pp 7.12.0
%define libpp_pkgname %{libname_pp}-%{sover_pp}-%{sover_pp}
# Qt 6 is not available in Leap 15.3
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%bcond_without Qt6
%endif
Name:           %{libname}
Version:        7.12.0
Release:        0
Summary:        Multimedia framework for television broadcasting
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.mltframework.org
Source0:        https://github.com/mltframework/mlt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if %{with Qt6} && 0%{?sle_version}
# Qt 6 requires a compiler that fully supports c++-17
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  cmake(Qt5Core) >= 5.10
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
%if %{with Qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Xml)
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(frei0r)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavdevice) >= 58
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil) >= 56
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libswscale) >= 5
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(movit)
%if 0%{?suse_version} > 1501
BuildRequires:  pkgconfig(opencv4)
%endif
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sox)
BuildRequires:  pkgconfig(vidstab)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)

%description
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers. The functionality of the system is
provided via an assortment of tools, XML authoring components, and an
plug-in based API.

%package -n %{lib_pkgname}
Summary:        C library API for the MLT multimedia framework
Group:          System/Libraries

%description -n %{lib_pkgname}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the C library API for MLT.

%package -n %{libpp_pkgname}
Summary:        C++ library API for the MLT multimedia framework
Group:          System/Libraries

%description -n %{libpp_pkgname}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the C++ library API for MLT.

%package devel
Summary:        Development files for MLT's C and C++ language API
Group:          Development/Libraries/C and C++
Provides:       libmlt++-devel = %{version}
Requires:       %{lib_pkgname} = %{version}
Requires:       %{libpp_pkgname} = %{version}

%description devel
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

This subpackage contains the headers to make use of the MLT C and
C++ API.

%package -n melt
Summary:        Multimedia framework for television broadcasting
Group:          Productivity/Multimedia/Video/Editors and Convertors
Provides:       melt%{sover} = %{version}
Requires:       %{libname}%{sover}-data = %{version}
Requires:       %{libname}%{sover}-modules = %{version}

%description -n melt
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

%if %{with Qt6}
# Creating a distinct Qt 6 module avoids pulling Qt 6 when installing the
# libmlt modules package
%package -n %{libname}%{sover}-module-qt6
Summary:        Qt 6 module for the MLT multimedia framework
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       %{libname}%{sover}-modules

%description -n %{libname}%{sover}-module-qt6
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

The functionality of the system is provided via an assortment of
tools, XML authoring components, and an plug-in based API.

This package provides a Qt 6 module for MLT.
%endif

%package -n %{libname}%{sover}-data
Summary:        Architecture-independent data files for the MLT multimedia framework
Group:          Productivity/Multimedia/Video/Editors and Convertors
BuildArch:      noarch

%description -n %{libname}%{sover}-data
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.

%package -n python3-%{_name}
Summary:        Python bindings for the MLT multimedia framework
Group:          Development/Languages/Python
BuildRequires:  swig
BuildRequires:  pkgconfig(python3)
Provides:       python3-%{_name} = %{version}
Conflicts:      python3-%{_name} < %{version}

%description -n python3-%{_name}
MLT is a multimedia framework for television broadcasting. It
provides a toolkit for broadcasters, video editors, media players,
transcoders and web streamers.
This package contains python bindings.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%if %{with Qt6} && 0%{?sle_version}
export CC=gcc-10 CXX=g++-10
%endif

# WARNING: building opencv module causes multicore issues - boo#1068792
%cmake \
%if 0%{?suse_version} > 1501
   -DMOD_OPENCV=ON \
%else
   -DMOD_OPENCV=OFF \
%endif
   -DGPL=ON \
   -DGPL3=ON \
   -DSWIG_PYTHON=ON \
   -DCMAKE_SKIP_RPATH=1 \
%if %{with Qt6}
   -DMOD_QT6=ON
%endif

%cmake_build

%install
%cmake_install

# Get the modules that need data
for MODULE in %{buildroot}%{_libdir}/mlt-%{sover}/libmlt*.so; do
  echo $MODULE
  MODULEDIR=%{_datadir}/mlt-%{sover}/$(echo $MODULE | sed 's|%{buildroot}%{_libdir}/mlt-%{sover}/libmlt\(.*\).so|\1|')
  if [[ "$MODULEDIR" =~ "qt6" ]]; then
    echo "Ignoring $MODULEDIR"
    continue
  fi
  echo $MODULEDIR
  if [ -e %{buildroot}$MODULEDIR ]; then
    echo Done $MODULEDIR
    echo $MODULEDIR >> module_data.dirs
  fi
done

#Link man melt to man melt-7
pushd  %{buildroot}%{_mandir}/man1/
ln -s  melt-%{sover}.1 melt.1
popd

# remove dupes
%fdupes %{buildroot}%{_datadir}/mlt-%{sover}

%post -n %{lib_pkgname} -p /sbin/ldconfig
%postun -n %{lib_pkgname} -p /sbin/ldconfig
%post -n %{libpp_pkgname} -p /sbin/ldconfig
%postun -n %{libpp_pkgname} -p /sbin/ldconfig

%files -n %{lib_pkgname}
%{_libdir}/lib%{_name}-%{sover}.so.%{sover}
%{_libdir}/lib%{_name}-%{sover}.so.%{lversion}

%files devel
%{_includedir}/%{_name}-%{sover}
%{_libdir}/cmake/Mlt%{sover}
%{_libdir}/lib%{_name}-%{sover}.so
%{_libdir}/lib%{_name_pp}-%{sover_pp}.so
%{_libdir}/pkgconfig/%{_name}-framework-%{sover}.pc
%{_libdir}/pkgconfig/%{_name_pp}-%{sover_pp}.pc

%files -n %{libpp_pkgname}
%{_libdir}/lib%{_name_pp}-%{sover_pp}.so.%{sover_pp}
%{_libdir}/lib%{_name_pp}-%{sover_pp}.so.%{lversion_pp}

%files -n melt
%{_bindir}/melt
%{_bindir}/melt-%{sover}
%{_mandir}/man1/melt.1%{?ext_man}
%{_mandir}/man1/melt-%{sover}.1%{?ext_man}

%files -n %{libname}%{sover}-modules -f module_data.dirs
%doc AUTHORS NEWS README.md
%license GPLv3 COPYING GPL
%{_libdir}/%{_name}-%{sover}
%dir %{_datadir}/%{_name}-%{sover}/
%exclude %{_libdir}/%{_name}-%{sover}/libmltqt6.so

%if %{with Qt6}
%files -n %{libname}%{sover}-module-qt6
%dir %{_libdir}/%{_name}-%{sover}
%{_libdir}/%{_name}-%{sover}/libmltqt6.so
%dir %{_datadir}/%{_name}-%{sover}/
%{_datadir}/%{_name}-%{sover}/qt6/
%endif

%files -n %{libname}%{sover}-data
%dir %{_datadir}/%{_name}-%{sover}/
%{_datadir}/%{_name}-%{sover}/metaschema.yaml
%{_datadir}/%{_name}-%{sover}/profiles/
%{_datadir}/%{_name}-%{sover}/presets/
%{_datadir}/%{_name}-%{sover}/vid.stab/

%files -n python3-%{_name}
%{python3_sitearch}/_%{_name}%{sover}.so
%{python3_sitearch}/%{_name}%{sover}.py

%changelog
