#
# spec file for package csound
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define py3version %(pkg-config python3 --modversion)
%define support_fltk 1
%if 0%{?suse_version} > 1500
%bcond_with java
%else
%bcond_with java
%endif
%define maj 6
%define min 0
%global luaver %(lua -v | sed -r 's/Lua ([[:digit:]]+\\.[[:digit:]]+).*/\\1/')
%bcond_with python
Name:           csound
Version:        6.18.1
Release:        0
Summary:        Computer Sound Synthesis and Composition Program
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://www.csounds.com
Source0:        https://github.com/csound/csound/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        README.SUSE
Source2:        COPYING_gpl2+.txt
# Default to using pulseaudio instead of portaudio
Patch2:         csound-6.08-default-pulse.patch
# Use xdg-open to open a browser to view the manual
Patch4:         csound-6.08-xdg-open.patch
Patch5:         csound-rename-sndinfo.patch
Patch6:         csound-rename-extract.patch
Patch7:         csound-gcc14.patch
BuildRequires:  alsa-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  liblo-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lua-devel
BuildRequires:  portaudio-devel
BuildRequires:  swig
Recommends:     %{name}-lang
%if %{with java}
BuildRequires:  java-devel-openjdk
%endif
%if %{with python}
BuildRequires:  python3-devel
%endif
%if %{support_fltk}
BuildRequires:  fltk-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
%endif

%description
Csound is a software synthesis program. It is modular and
supports an unlimited amount of oscillators and filters.

%package -n libcsnd6-%{maj}_%{min}
Summary:        Computer sound synthesis and composition library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libcsnd6-%{maj}_%{min}
Library for csound use.
Csound is a software synthesis program supporting oscillators and
filters.

%package -n libcsound64-%{maj}_%{min}
Summary:        Computer sound synthesis and composition library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libcsound64-%{maj}_%{min}
Library for csound use
Csound is a software synthesis program supporting oscillators and
filters.

%package java-bindings
Summary:        Java bindings for the Csound sound synthesis and composition library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description java-bindings
Java bindings for csound use.
Csound is a software synthesis program supporting oscillators and
filters.

%package plugins
Summary:        Plugins for csound
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other

%description plugins
Plugins for csound

%package -n python3-csound
Summary:        Csound opcodes for python
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other

%description -n python3-csound
Csound opcodes for python

%package samples
Summary:        Data files for csound
License:        MIT
Group:          Productivity/Multimedia/Other
BuildArch:      noarch

%description samples
HRTF datafiles and Soundfont for csound

%package devel
Summary:        Development files for Csound
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libcsnd6-%{maj}_%{min} = %{version}
Requires:       libcsound64-%{maj}_%{min} = %{version}
%if %{with java}
Requires:       %{name}-java-bindings = %{version}
%endif

%description devel
Development files for Csound, a sound synthesis program.

%lang_package

%prep
%autosetup -p1
# remove __DATE__ from source files, causes unnecessary rebuilds
#sed -i 's:__DATE__:"":' Engine/musmon.c include/version.h Top/main.c
# copy readme
cp %{SOURCE1} %{SOURCE2} .
#These source files are undistributable
#rm -f Opcodes/scansyn*
head -n 28 util/SDIF/sdif.c > COPYING.PostgreSQL

%build
# Needed to link libbuchla.so
export CFLAGS="%{optflags} -lm"
export CXXFLAGS="%{optflags} -std=c++11"

%cmake \
       -DBUILD_SCANSYN_OPCODES=OFF \
%if %{with python}
       -DPYTHON_LIBRARY="%{_libdir}/libpython$(pkg-config python3 --modversion)$(python3-config --abiflags).so" \
       -DPYTHON_INCLUDE_DIR="%{_includedir}/python$(pkg-config python3 --modversion)$(python3-config --abiflags)" \
%endif
       -DNEED_PORTTIME:BOOL=OFF \
       -DRPM_LUAVER:STRING=%{luaver} \
%if "%{_lib}" == "lib64"
       -DUSE_LIB64:BOOL=ON
%else
       -DUSE_LIB64:BOOL=OFF
%endif

%make_build

%install
%cmake_install
#python bindings are wip
rm -rf %{buildroot}root
cp -v OOps/README.md README.OOps

%fdupes -s %{buildroot}
%find_lang %{name}%{maj}

%ldconfig_scriptlets -n libcsnd6-%{maj}_%{min}
%ldconfig_scriptlets -n libcsound64-%{maj}_%{min}
%ldconfig_scriptlets java-bindings

%files
%doc AUTHORS README.md README.SUSE Release_Notes README.OOps
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%{_bindir}/*
%{_bindir}/csound-extract

%files -n libcsnd6-%{maj}_%{min}
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%{_libdir}/libcsnd6.so.%{maj}.%{min}

%files -n libcsound64-%{maj}_%{min}
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%{_libdir}/libcsound64.so.%{maj}.%{min}

%if %{with java}
%files java-bindings
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%{_libdir}/lib_jcsound6.so
%{_libdir}/csnd6.jar
%endif

%files plugins
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%{_libdir}/csound/

%files samples
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%{_datadir}/samples/

%files -n python3-csound
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%if 0%{?suse_version} > 1500
%{python_sitearch}/ctcsound.py
%else
%{_libdir}/python3.6/site-packages/ctcsound.py
%endif

%files devel
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL
%{_includedir}/csound/
%{_libdir}/libcs*.so
%{_datadir}/cmake/Csound/

%files lang -f %{name}%{maj}.lang
%license COPYING COPYING_gpl2+.txt COPYING.PostgreSQL

%changelog
