#
# spec file for package cura
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


# 'qmlimport(Cura.1)' - Internal QML import
# 'qmlimport(DigitalFactory.1) - Internal, registered from plugins/DigitalLibrary/src/DigitalFactoryController.py
%global __requires_exclude qmlimport\\((Cura|DigitalFactory)\\..*

Name:           cura
%define sversion        4.13.1
Version:        4.13.1
Release:        0
Summary:        3D printer control software
License:        LGPL-3.0-only
Group:          Hardware/Printing
URL:            https://github.com/Ultimaker/Cura
Source:         https://github.com/Ultimaker/Cura/archive/%{sversion}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE disable-code-style-check.patch code style is no distro business
Patch1:         disable-code-style-check.patch
# PATCH-FIX-UPSTREAM - remove unused import of sentry_sdk
Patch2:         https://github.com/Ultimaker/Cura/commit/aad41807c365ccef001b787407d7dc756e11de02.patch#/remove_unused_sentry_sdk.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python3-Arcus >= %{version}
BuildRequires:  python3-Savitar >= %{version}
BuildRequires:  python3-keyring >= 21
BuildRequires:  python3-numpy
BuildRequires:  python3-pynest2d
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
Requires:       python3-Arcus >= %{version}
Requires:       python3-Savitar >= %{version}
Requires:       python3-keyring >= 21
Requires:       python3-numpy
Requires:       python3-pynest2d
Requires:       python3-pyserial
Requires:       python3-qt5 >= 5.10
Requires:       python3-requests
Requires:       python3-scipy
Requires:       python3-sentry-sdk
Requires:       python3-shapely
Requires:       python3-typing
Requires:       uranium >= %{version}
Recommends:     cura-fdm-materials >= %{version}
Recommends:     python3-trimesh
Recommends:     python3-zeroconf
BuildArch:      noarch
# The CuraEngine is not supported on 32bit Linux anymore
ExcludeArch:    %ix86 %arm s390 ppc

%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura helps setting up an Ultimaker, shows the 3D model, allows for scaling /
positioning, can slice the model to G-Code with editable configuration
settings, and send this G-Code to the 3D printer for printing.

%prep
%autosetup -n Cura-%sversion -p1
sed -i -e '1 s/env python3/python3/' cura_app.py

%build
export CFLAGS="%{optflags}"
# Hack, remove LIB_SUFFIX for 64bit, which is correct as cura is pure python (i.e. noarch)
%cmake -DLIB_SUFFIX="" \
       -DCURA_BUILDTYPE=RPM \
       -DCURA_CLOUD_API_ROOT:STRING=https://api.ultimaker.com \
       -DCURA_CLOUD_API_VERSION:STRING=1 \
       -DCURA_CLOUD_ACCOUNT_API_ROOT:STRING=https://account.ultimaker.com \
       -DCURA_VERSION=%version \
       -DCURA_DEBUGMODE=OFF \
       %{nil}
%cmake_build

%install
%cmake_install

for x in 128 64 48 32; do
    install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/
    install -m 644 icons/cura-${x}.png %{buildroot}%{_datadir}/icons/hicolor/${x}x${x}/apps/cura-icon.png
done

# i18n sources (po/pot) are installed in cura/resources, .mo in uranium/resources
rm -Rf %{buildroot}%{_datadir}/%{name}/resources/i18n
# uranium uses i18n instead of locale for the path to translation files,
# thus we cannot use %%find_lang
echo '%defattr(644,root,root,755)' > %{name}.lang
find %{buildroot}%{_datadir}/cura -name *.mo | sed '
  s:'%{buildroot}'::; s:\(.*/i18n/\)\([^/]\+\)\(.*mo\):%lang(\2) \1\2\3:' \
  >> %{name}.lang

%fdupes -s %{buildroot}%{_datadir}/%{name}
%suse_update_desktop_file com.ultimaker.cura Graphics 3DGraphics

%check
cd build
make CTEST_OUTPUT_ON_FAILURE=TRUE test

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{python3_sitelib}/cura
%{_datadir}/%{name}
%{_datadir}/applications/com.ultimaker.cura.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/com.ultimaker.cura.appdata.xml
%{_datadir}/mime/packages/cura.xml
%{_datadir}/icons/hicolor
%{_bindir}/cura
%{_prefix}/lib/cura

%changelog
