#
# spec file for package kicad
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


%if %{suse_version} >= 1550
%bcond_without python3
%else
%bcond_with python3
%endif

# According to upstream, kicad 5.x.y can be used with the footprint and
# symbol libraries from version 5.0.0
%define compatversion 5.0.0
Name:           kicad
Version:        5.1.7
Release:        0
Summary:        EDA software suite for the creation of schematics and PCB
License:        GPL-3.0-or-later AND AGPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://kicad-pcb.org
Source:         https://gitlab.com/kicad/code/kicad/-/archive/%{version}/kicad-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE davejplater@gmail.com -kicad-suse-help-path.patch - kicad looks in /usr/share/doc/kicad for help files and doesn't find them.
# this patch adds packges/ befor kicad and enables help to function.
Patch3:         kicad-suse-help-path.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libngspice-devel
BuildRequires:  occt-devel
BuildRequires:  pkg-config
BuildRequires:  swig >= 3
BuildRequires:  update-desktop-files

%if %{with python3}
BuildRequires:  wxGTK3-devel >= 3
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-wxPython
Recommends:     python3-wxPython
%else
# Use direct version to avoid problems with wx 3.2
BuildRequires:  python-wxWidgets-3_0-devel >= 3
BuildRequires:  wxWidgets-3_0-devel >= 3
BuildRequires:  pkgconfig(python)
Requires:       python-wxWidgets-3_0 >= 3
%endif

BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# Fix directory owner
BuildRequires:  hicolor-icon-theme
# Dlopen'ed simulator library
Requires:       libngspice0
# The help function gives an error without the doc package
Requires:       %{name}-doc = %{version}
# You cannot build a schematic without symbols
Requires:       %{name}-symbols = %{compatversion}
# You cannot create a pcb layout without footprints
Requires:       %{name}-footprints = %{compatversion}
# KiCad functions without these packages
Recommends:     %{name}-packages3D = %{compatversion}
Recommends:     %{name}-templates = %{compatversion}
Obsoletes:      kicad = 20140120
Provides:       kicad = %{compatversion}

%description
KiCad is an open source (GPL) software for the creation of electronic schematic
diagrams and printed circuit with up to 32 copper layers and additional techinical layers.

KiCad includes a project manager and four main independent software tools:
- Eeschema: schematic editor.
- Pcbnew: printed circuit board editor.
- Gerbview: GERBER file viewer (photoplotter documents).
- Cvpcb: footprint selector for components association.

%prep
%setup -q -n kicad-%{version}
%patch3

%build
#    -DKICAD_PLUGINS:PATH=%%{_libdir}/kicad/plugins \
# The above path is for .py scripts and other text files install places these files correctly.
# The KICAD_USER_PLUGIN is for binary plugins.
%cmake \
    -DKICAD_VERSION_EXTRA=%{version} \
    -DKICAD_LIB:PATH=%{_libdir} \
    -DKICAD_USER_PLUGIN:PATH=%{_libdir}/kicad/plugins \
    -DKICAD_DOCS:PATH=%{_docdir}/kicad \
    -DKICAD_DATA:PATH=%{_datadir}/kicad \
    -DBUILD_GITHUB_PLUGIN=ON \
    -DKICAD_SCRIPTING=ON \
    -DKICAD_SCRIPTING_MODULES=ON \
    -DKICAD_SCRIPTING_WXPYTHON=ON \
%if %{with python3}
    -DKICAD_SCRIPTING_PYTHON3=ON \
    -DKICAD_SCRIPTING_WXPYTHON_PHOENIX=ON \
%endif
    -DKICAD_USE_OCC:BOOL=ON \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -pie" \
    -DPYTHON_SITE_PACKAGE_PATH=%{python_sitearch} \
    -DKICAD_SPICE=ON

make %{?_smp_mflags}

%install
%cmake_install

%suse_update_desktop_file -r bitmap2component "Education;Engineering"
%suse_update_desktop_file -r eeschema "Education;Engineering"
%suse_update_desktop_file -r gerbview "Education;Engineering"
%suse_update_desktop_file -r kicad "Education;Engineering"
%suse_update_desktop_file -r pcbcalculator "Education;Engineering"
%suse_update_desktop_file -r pcbnew "Education;Engineering"

# Link to library libkicad_3dsg.so.2.0.0 has no use
rm -rf %{buildroot}%{_libdir}/libkicad_3dsg.so

# Delete packaging/maintenance scripts
for f in test_kicad_plugin.py test_plugin.py ; do
    rm "%{buildroot}%{_docdir}/kicad/scripts/$f"
done
# Move remaining standalone scripts to kicad directory
mv %{buildroot}%{_docdir}/kicad/scripts %{buildroot}%{_datadir}/kicad/
%if %{with python3}
sed -i '1s@^#!.*python.*@#!/usr/bin/python3@' %{buildroot}%{_datadir}/kicad/scripts/*.py
%else
sed -i '1s@^#!.*python.*@#!/usr/bin/python2@' %{buildroot}%{_datadir}/kicad/scripts/*.py
%endif
chmod +x %{buildroot}%{_datadir}/kicad/scripts/*.py

# Fix executable bits for scripts executed directly from kicad, remove she-bangs
chmod -x %{buildroot}%{_datadir}/kicad/scripting/*/*.py
sed -i '1s@^#!.*@@' %{buildroot}%{_datadir}/kicad/scripting/*/*.py

%fdupes -s %{buildroot}%{_datadir}/kicad
%fdupes -s %{buildroot}%{_datadir}/icons/hicolor
# the pcbnew kiface and the python module are actually the same file
cmp --quiet %{buildroot}%{_bindir}/_pcbnew.kiface %{buildroot}%{python_sitearch}/_pcbnew.so && \
  ln -sf  %{_bindir}/_pcbnew.kiface %{buildroot}%{python_sitearch}/_pcbnew.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.txt Documentation/changelogs
%license LICENSE.GPLv3 LICENSE.AGPLv3 LICENSE.README
%{_bindir}/*
%exclude %{_bindir}/kicad-library-install.sh
%{_libdir}/kicad/
%{_datadir}/kicad/
%{python_sitearch}/*
%{_datadir}/appdata/kicad.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/%{name}-*.xml
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_libdir}/libkicad_3dsg.so.2.0.0

%changelog
