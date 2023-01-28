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


# According to upstream, kicad 6.x.y can be used with the footprint and
# symbol libraries from version 6.0.0
%define compatversion 6.0.0
Name:           kicad
Version:        6.0.11
%define file_version 6.0.11
Release:        0
Summary:        EDA software suite for the creation of schematics and PCB
License:        AGPL-3.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://www.kicad.org
Source:         https://gitlab.com/kicad/code/kicad/-/archive/%{file_version}/kicad-%{file_version}.tar.bz2
Patch0:         0001-Use-library-target-install-for-python-module-to-fix-.patch

BuildRequires:  cmake >= 3.14
BuildRequires:  fdupes
BuildRequires:  gcc-c++
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

%build
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

# Delete packaging/maintenance scripts
rm "%{buildroot}%{_docdir}/kicad/scripts/"{test_kicad_plugin.py,test_plugin.py}

# Move remaining standalone scripts to kicad directory
mv %{buildroot}%{_docdir}/kicad/scripts %{buildroot}%{_datadir}/kicad/
sed -i '1s@^#!.*python.*@#!/usr/bin/python3@' %{buildroot}%{_datadir}/kicad/scripts/*.py
chmod +x %{buildroot}%{_datadir}/kicad/scripts/*.py

# Fix executable bits for scripts executed directly from kicad, remove she-bangs
chmod -x %{buildroot}%{_datadir}/kicad/scripting/*/*.py
sed -i '1s@^#!.*@@' %{buildroot}%{_datadir}/kicad/scripting/*/*.py

%fdupes %{buildroot}%{_datadir}/kicad
%fdupes %{buildroot}%{_datadir}/icons/hicolor
# the pcbnew kiface and the python module are actually the same file
cmp %{buildroot}%{_bindir}/_pcbnew.kiface %{buildroot}%{python3_sitearch}/_pcbnew.so && \
  ln -sf  %{_bindir}/_pcbnew.kiface %{buildroot}%{python3_sitearch}/_pcbnew.so

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
%doc README.md Documentation/changelogs
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
