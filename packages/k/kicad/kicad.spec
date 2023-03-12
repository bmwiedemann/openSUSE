#
# spec file for package kicad
#
# Copyright (c) 2023 SUSE LLC
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


# According to upstream, kicad 7.x.y can be used with the footprint and
# symbol libraries from version 7.0.0
%define compatversion 7.0.0
Name:           kicad
Version:        7.0.1
%define file_version 7.0.1
Release:        0
Summary:        EDA software suite for the creation of schematics and PCB
License:        AGPL-3.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://www.kicad.org
Source:         https://gitlab.com/kicad/code/kicad/-/archive/%{file_version}/kicad-%{file_version}.tar.bz2

BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
# Requires charconv from C++17
%if 0%{?suse_version} >= 1550
BuildRequires:  gcc-c++ >= 8
%else
BuildRequires:  gcc11-PIE
BuildRequires:  gcc11-c++ >= 8
%endif
BuildRequires:  gettext
BuildRequires:  glm-devel >= 0.9.8
BuildRequires:  libboost_filesystem-devel-impl
BuildRequires:  libboost_system-devel-impl >= 1.71
BuildRequires:  libboost_test-devel-impl
BuildRequires:  libngspice-devel
BuildRequires:  occt-devel
BuildRequires:  pkg-config
BuildRequires:  python3-pybind11-devel
BuildRequires:  python3-wxPython
BuildRequires:  swig >= 3
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel >= 3
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3) >= 3.6
BuildRequires:  pkgconfig(zlib)
# Fix directory owner
BuildRequires:  hicolor-icon-theme
# Dlopen'ed simulator library
Requires:       libngspice0
# The help function gives an error without the doc package
Recommends:     kicad-doc = %{version}
# You cannot build a schematic without symbols
Requires:       kicad-symbols = %{compatversion}
# You cannot create a pcb layout without footprints
Requires:       kicad-footprints = %{compatversion}
# KiCad functions without these packages
Recommends:     kicad-packages3D = %{compatversion}
Recommends:     kicad-templates = %{compatversion}
Recommends:     python3-wxPython
Obsoletes:      kicad = 20140120
Provides:       kicad = %{compatversion}
# Test suite fails, 32 bit archs no longer supported
ExcludeArch:    %{arm}

%description
KiCad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit with up to 32 copper layers and
additional technical layers.

KiCad includes a project manager and four main independent software tools:
- Eeschema: schematic editor.
- Pcbnew: printed circuit board editor.
- Gerbview: GERBER file viewer (photoplotter documents).
- Cvpcb: footprint selector for components association.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch
# Per lang split packages from old kicad-i18n
Conflicts:      kicad-lang-bg < 6.0.0
Conflicts:      kicad-lang-ca < 6.0.0
Conflicts:      kicad-lang-cs < 6.0.0
Conflicts:      kicad-lang-de < 6.0.0
Conflicts:      kicad-lang-el < 6.0.0
Conflicts:      kicad-lang-en < 6.0.0
Conflicts:      kicad-lang-es < 6.0.0
Conflicts:      kicad-lang-fi < 6.0.0
Conflicts:      kicad-lang-fr < 6.0.0
Conflicts:      kicad-lang-hu < 6.0.0
Conflicts:      kicad-lang-it < 6.0.0
Conflicts:      kicad-lang-ja < 6.0.0
Conflicts:      kicad-lang-ko < 6.0.0
Conflicts:      kicad-lang-lt < 6.0.0
Conflicts:      kicad-lang-nl < 6.0.0
Conflicts:      kicad-lang-pl < 6.0.0
Conflicts:      kicad-lang-pt < 6.0.0
Conflicts:      kicad-lang-ru < 6.0.0
Conflicts:      kicad-lang-sk < 6.0.0
Conflicts:      kicad-lang-sl < 6.0.0
Conflicts:      kicad-lang-sv < 6.0.0
Conflicts:      kicad-lang-zh_CN < 6.0.0
Conflicts:      kicad-lang-zh_TW < 6.0.0

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup -p1 -n kicad-%{file_version}
%if 0%{?suse_version} < 1550
sed -i -e '/cmake_minimum_required/ s/3.21/3.16/' CMakeLists.txt
sed -i -e '/SWIG/ s/4.0/3.0/' CMakeLists.txt
sed -i -e '/SWIG_OPTS/ { s/ -O/ -py3/ ; s/ -fastdispatch//}' pcbnew/CMakeLists.txt
%endif

%build
%if 0%{?suse_version} < 1550
export CXX=g++-11 CC=gcc-11
%endif
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -pie" \
    -DKICAD_DOCS:PATH=%{_docdir}/kicad \
    -DPYTHON_SITE_PACKAGE_PATH=%{python3_sitearch} \
    -DKICAD_BUILD_I18N=ON \
    -DKICAD_I18N_UNIX_STRICT_PATH:BOOL=ON \
    -DKICAD_SCRIPTING_WXPYTHON=ON \
    -DKICAD_USE_OCC:BOOL=ON \
    -DKICAD_PCM=ON \
    -DKICAD_SPICE=ON

%cmake_build

%install
%cmake_install

%if 0%{?suse_version} < 1550
%suse_update_desktop_file -r org.kicad.bitmap2component "Education;Engineering"
%suse_update_desktop_file -r org.kicad.eeschema "Education;Engineering"
%suse_update_desktop_file -r org.kicad.gerbview "Education;Engineering"
%suse_update_desktop_file -r org.kicad.kicad "Education;Engineering"
%suse_update_desktop_file -r org.kicad.pcbcalculator "Education;Engineering"
%suse_update_desktop_file -r org.kicad.pcbnew "Education;Engineering"
%endif

# Link to library libkicad_3dsg.so.2.0.0 has no use
rm -rf %{buildroot}%{_libdir}/libkicad_3dsg.so

# https://gitlab.com/kicad/code/kicad/-/issues/9944
rm -rf %{buildroot}%{_libdir}/libkicad*.a

# Fix executable bits for scripts executed directly from kicad
chmod -x %{buildroot}%{_datadir}/kicad/scripting/*/*.py

%fdupes %{buildroot}%{_datadir}/kicad
%fdupes %{buildroot}%{_datadir}/icons/hicolor

%find_lang %{name}

%check
%ifarch %{ix86}
# https://gitlab.com/kicad/code/kicad/-/issues/10149
%ctest --exclude-regex qa_eeschema
%else
%ctest
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE.*
%{_bindir}/*
%{_libdir}/kicad/
%{_datadir}/kicad/
%{python3_sitearch}/*
%{_datadir}/metainfo/org.kicad.kicad.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/kicad-*.xml
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_libdir}/libkicad_3dsg.so.2.0.0

%files lang -f %{name}.lang

%changelog
