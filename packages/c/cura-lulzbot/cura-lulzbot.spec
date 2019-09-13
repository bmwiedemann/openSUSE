#
# spec file for package cura-lulzbot
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           cura-lulzbot
Version:        3.6.18
Release:        0
Summary:        3D printer control software
License:        AGPL-3.0-only
Group:          Hardware/Printing
Url:            https://code.alephobjects.com/source/cura-lulzbot.git
Source0:        %name-%{version}.tar.xz
# PATCH-FIX-OPENSUSE fix-build.patch -- adapt SUSE python install path
Patch1:         fix-build.patch
# PATCH-FIX-OPENSUSE CuraEngine-lulzbot.patch -- use lulzbot variant of CuraEngine by default
Patch2:         CuraEngine-lulzbot.patch
BuildArch:      noarch
Provides:       cura2-lulzbot
Obsoletes:      cura2-lulzbot < 3
Conflicts:      cura
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  icoutils
BuildRequires:  gettext-tools
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  uranium-lulzbot
Requires:       cura-engine-lulzbot = %version
Requires:       uranium-lulzbot = %version
# dependency scripts do not find qtquickcontrols automatically
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Requires:       python3-numpy
Requires:       python3-opengl
Requires:       python3-power
Requires:       python3-pyserial
Requires:       python3-qt5
Requires:       python3-scipy
Requires:       python3-sip
Requires:       python3-zeroconf
# No 32bit support anymore
ExcludeArch:    %ix86 %arm s390

# There is a hardcoded version to the firmware in the code :/ 
Requires:       uranium-firmware-lulzbot = %( tar xf %{S:0} --wildcards \*/USBPrinterOutputDeviceManager.py --to-command='sed -n -e "s,.*Marlin_Mini_SingleExtruder_\([^_]*_[^_]*\).hex.*,\1,p"' )

%description
Cura is a software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura helps in setting up an Ultimaker, shows 3D models, allows for scaling /
positioning, can slice the model to G-Code, has editable configuration
settings, and send this G-Code to the 3D printer for printing.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
sed -i -e 's,@CURA_VERSION@,%version,' cura/CuraVersion.py.in
sed -i -e 's,@CURA_BUILDTYPE@,release,' cura/CuraVersion.py.in
sed -i -e 's,CuraDebugMode = .*,CuraDebugMode = False,' cura/CuraVersion.py.in
%cmake -DURANIUM_DIR=/usr/lib/uranium -DURANIUM_SCRIPTS_DIR=/usr/share/uranium/resources/scripts -DCURA_DEBUGMODE=OFF
make %{?_smp_mflags}

%install
cd build
%make_install
install -m 0644 ../version.json %buildroot/usr/share/cura/
%suse_update_desktop_file cura-lulzbot Graphics 3DGraphics
sed -i -e 's,^Exec=.*,Exec=cura-lulzbot %F,' \
       -e 's,^#!/usr/bin/env.*,#!/usr/bin/python3,' \
    %{buildroot}%{_datadir}/applications/cura-lulzbot.desktop
%fdupes %buildroot

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/cura
%{_datadir}/cura
%{_datadir}/applications/cura-lulzbot.desktop
%{_datadir}/mime/packages/cura.xml
%{_datadir}/appdata/cura.appdata.xml
%{_bindir}/cura-lulzbot
/usr/lib/cura

%changelog
