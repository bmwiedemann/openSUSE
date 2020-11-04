#
# spec file for package cura
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


Name:           cura
Version:        4.7.1
Release:        0
Summary:        3D printer control software
License:        LGPL-3.0-only
Group:          Hardware/Printing
URL:            https://github.com/Ultimaker/Cura
Source0:        Cura-%{version}.tar.xz
# PATCH-FIX-OPENSUSE disable-code-style-check.patch code style is no distro business
Patch1:         disable-code-style-check.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libArcus3 >= %{version}
BuildRequires:  python3-Savitar >= 4.6.0
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-qt5
BuildRequires:  python3-requests
BuildRequires:  python3-scipy
BuildRequires:  python3-shapely
BuildRequires:  python3-zeroconf
BuildRequires:  update-desktop-files
BuildRequires:  uranium >= %{version}
# It builds with older Qt, but crashes due to missing qml features
BuildRequires:  pkgconfig(Qt5Core) >= 5.10
Requires:       cura-engine >= %{version}
Requires:       python3-numpy
# Build and test suite works with older Qt, but no UI shows up due to usage
# of newer QML elements
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Requires:       python3-Savitar
Requires:       python3-pyserial
Requires:       python3-qt5 >= 5.10
Requires:       python3-requests
Requires:       python3-scipy
Requires:       python3-shapely
Requires:       python3-typing
Requires:       uranium >= %{version}
Recommends:     cura-fdm-materials >= %{version}
Recommends:     python3-trimesh
Recommends:     python3-zeroconf
BuildArch:      noarch
# The CuraEngine is not supported on 32bit Linux anymore
ExcludeArch:    %ix86 %arm s390

%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura helps setting up an Ultimaker, shows the 3D model, allows for scaling /
positioning, can slice the model to G-Code with editable configuration
settings, and send this G-Code to the 3D printer for printing.

%prep
%setup -q -n Cura-%version
%patch1 -p1
sed -i -e '1 s/env python3/python3/' cura_app.py

%build
export CFLAGS="%{optflags}"
sed -i 's/PythonInterp 3.5.0/PythonInterp 3.4.0/' CMakeLists.txt cmake/CuraTests.cmake
# Hack, remove LIB_SUFFIX for 64bit, which is correct as cura is pure python (i.e. noarch)
%cmake -DLIB_SUFFIX="" \
       -DCMAKE_BUILD_TYPE=Release \
       -DCURA_BUILDTYPE=RPM \
       -DCURA_CLOUD_API_ROOT:STRING=https://api.ultimaker.com \
       -DCURA_CLOUD_API_VERSION:STRING=1 \
       -DCURA_CLOUD_ACCOUNT_API_ROOT:STRING=https://account.ultimaker.com \
       -DCURA_VERSION=%version \
       -DCURA_DEBUGMODE=OFF \
       -DCURA_SDK_VERSION="6.0.0"
#       -DURANIUM_SCRIPTS_DIR=
make %{?_smp_mflags}

%install
pushd build
%make_install
popd

for x in 128 64 48 32; do
    install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}
    install -m 644 icons/cura-${x}.png %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/cura-icon.png
done

# i18n sources (po/pot) are installed in cura/resources, .mo in uranium/resources
rm -Rf %{buildroot}%{_datadir}/%{name}/resources/i18n
# uranium uses i18n instead of locale for the path to translation files,
# thus we cannot use %%find_lang
echo '%defattr(644,root,root,755)' > %{name}.lang
find %{buildroot}%{_datadir}/uranium -name *.mo | sed '
  s:'%{buildroot}'::; s:\(.*/i18n/\)\([^/]\+\)\(.*mo\):%lang(\2) \1\2\3:' \
  >> %{name}.lang

%fdupes -s %{buildroot}%{_datadir}/%{name}
%suse_update_desktop_file cura Graphics 3DGraphics

%check
cd build
make CTEST_OUTPUT_ON_FAILURE=TRUE test

%files -f %{name}.lang
%defattr (-,root,root,-)
%license LICENSE
%doc README.md
%{python3_sitelib}/cura
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/mime/packages/cura.xml
%{_datadir}/icons/hicolor
%{_bindir}/cura
%{_prefix}/lib/cura

%changelog
