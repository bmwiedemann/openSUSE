#
# spec file for package icc-profiles-openicc
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011-2012 Kai-Uwe Behrmann <ku.b@gmx.de>
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


Version:        1.3.1
Release:        0
Source:         icc-profiles-openicc-1.3.1.tar.bz2
%define syscolordir     /usr/share/color
%define usercolordir    ~/.color
%define iccdirname      icc
%define cmmsubpath      colour/modules
%define settingsdirname settings
%define targetdirname   target
%define pixmapdir       /usr/share/pixmaps
%define icondir         /usr/share/icons
%define desktopdir      /usr/share/applications
Summary:        Color Management Data

Name:           icc-profiles-openicc
License:        Zlib
Group:          Productivity/Graphics/Other
Url:            http://www.freedesktop.org/wiki/OpenIcc
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  color-filesystem icc-profiles-basiccolor-printing2009-coat2

%description
The color data is provided to be used by color managed applications and
systems.



%prep
%setup -n  %{name}-%{version}

%build
%configure --quick

%install
%make_install
rm -fr %{buildroot}/%{_datadir}/color/icc/Cine*

%package    -n icc-mime-types
Summary:        ICC + CGATS icon
Group:          Productivity/Graphics/Other
Version:        1.2


%description  -n icc-mime-types
The ICC profile and CGATS mime types and a icon for these file types.

%package    -n icc-profiles-openicc-rgb
Summary:        Default sRGB ICC profile +
Group:          Productivity/Graphics/Other
Version:        1.3


Requires:       color-filesystem

%description  -n icc-profiles-openicc-rgb
The "WWW standard" sRGB colorimetry in a ICC profile and others.

%package    -n icc-profiles-oyranos-extra
Summary:        Gray and ITUlab profiles
Group:          Productivity/Graphics/Other
Url:            http://www.oyranos.org
Version:        1.2


Requires:       color-filesystem

%description  -n icc-profiles-oyranos-extra
A gray and ITUlab fax ICC profile.

%package      -n icc-profiles-lcms-lab
Summary:        Default PCS profiles
Group:          Productivity/Graphics/Other
Url:            http://www.littlecms.com
Version:        1.2


Requires:       color-filesystem

%description  -n icc-profiles-lcms-lab
Special LCMS profiles for PCS color spaces.

%package      -n icc-profiles-basiccolor-lstarrgb
Summary:        Default Editing RGB profile
Group:          Productivity/Graphics/Other
Url:            http://www.colormanagement.org
Version:        1.2


Requires:       color-filesystem

%description  -n icc-profiles-basiccolor-lstarrgb
The RGB profile maintaining perceptual equal lightness.
The LStar-RGB.icc profile is colorimetric identical to the eciRGB_v2 profile.


%package      -n icc-targets-fogra
Summary:        FOGRA Printing Characterisation Data
Group:          Productivity/Graphics/Other
Url:            http://www.fogra.org
Version:        1.0


Requires:       color-filesystem

%description  -n icc-targets-fogra
Printing characterisation data according to ISO 12647-2.
These are CMYK characterisation data for coated,
webcoated, uncoated, uncoatedyellowish and SC paper.

%package      -n icc-targets-npes
Summary:        NPES Printing Characterisation Data
Group:          Productivity/Graphics/Other
Url:            http://www.npes.org
Version:        1.0


Requires:       color-filesystem

%description  -n icc-targets-npes
Printing characterisation data. These are CMYK
characterisation data for GRACoL, SWOP and SNAP.

%package      -n icc-profiles-mini
Summary:        OpenICC Data with minimal ICC profiles
Group:          Productivity/Graphics/Other
Version:        1.2


Requires:       icc-profiles-openicc-rgb
Requires:       icc-profiles-basiccolor-lstarrgb
Requires:       icc-profiles-lcms-lab

%description  -n icc-profiles-mini
The meta package installs a minimal set of ICC profiles from the OpenICC 
Data collection. No Cmyk and Gray profiles are contained.

%package     -n icc-profiles
Summary:        OpenICC Data with complete ICC profiles
Group:          Productivity/Graphics/Other
Version:        1.2


Requires:       icc-profiles-mini
Requires:       icc-profiles-basiccolor-printing2009-coat2
Provides:       openicc-data = %{version}-%{release}
Obsoletes:      openicc-data < %{version}-%{release}

%description  -n icc-profiles
The meta package installs a complete set of ICC profiles from the OpenICC 
Data collection. One Cmyk profile is contained.

%package      -n icc-profiles-all
Summary:        OpenICC Data with all ICC profiles and targets
Group:          Productivity/Graphics/Other
Version:        1.2


Requires:       icc-profiles
Requires:       icc-profiles-oyranos-extra
Requires:       icc-profiles-basiccolor-printing2009-extra

%description  -n icc-profiles-all
The meta package installs all ICC profiles from the OpenICC Data collection.


%files -n icc-mime-types
%defattr(-, root, root)
%{_datadir}/mime/packages/*
%{pixmapdir}/*
%{icondir}/*

%files -n icc-profiles-lcms-lab
%defattr(-, root, root)
%dir %{syscolordir}/icc/lcms
%{syscolordir}/icc/lcms/LCMS*.ICM
%{syscolordir}/icc/lcms/Lab.icc
%{syscolordir}/icc/lcms/XYZ.icc

%files -n icc-profiles-oyranos-extra
%defattr(-, root, root)
%dir %{syscolordir}/icc/Oyranos
%{syscolordir}/icc/Oyranos/ITULab.icc
%{syscolordir}/icc/Oyranos/Gray_linear.icc
%{syscolordir}/icc/Oyranos/Gray-CIE_L.icc

%files -n icc-profiles-basiccolor-lstarrgb
%defattr(-, root, root)
%{syscolordir}/icc/basICColor/LStar-RGB.icc
# This should go in the package docs, not with the profiles.
%doc default_profiles/base/LICENSE-ZLIB-LSTAR

%files -n icc-profiles-openicc-rgb
%defattr(-, root, root)
%dir %{syscolordir}/icc/OpenICC
%{syscolordir}/icc/OpenICC/sRGB.icc
%{syscolordir}/icc/OpenICC/ProPhoto-RGB.icc
%{syscolordir}/icc/OpenICC/compatibleWithAdobeRGB1998.icc

%files -n icc-targets-fogra
%defattr(-, root, root)
%dir %{syscolordir}/target/fogra
%{syscolordir}/target/fogra/FOGRA28L.ti3
%{syscolordir}/target/fogra/FOGRA29L.ti3
%{syscolordir}/target/fogra/FOGRA30L.ti3
%{syscolordir}/target/fogra/FOGRA39L.ti3
%{syscolordir}/target/fogra/FOGRA40L.ti3

%files -n icc-targets-npes
%defattr(-, root, root)
%dir %{syscolordir}/target/NPES
%{syscolordir}/target/NPES/TR002.ti3
%{syscolordir}/target/NPES/TR003.ti3
%{syscolordir}/target/NPES/TR005.ti3
%{syscolordir}/target/NPES/TR006.ti3

%files -n icc-profiles-all
%defattr(-, root, root)
%doc default_profiles/base/LICENSE-ZLIB

%files -n icc-profiles-mini
%defattr(-, root, root)
%doc default_profiles/base/LICENSE-ZLIB

%files -n icc-profiles
%defattr(-, root, root)
%doc default_profiles/base/LICENSE-ZLIB

%changelog
