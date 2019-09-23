#
# spec file for package icc-profiles-basiccolor-printing2009
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Kai-Uwe Behrmann <ku.b@gmx.de>
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


Version:        1.2.0
Release:        0
Source:         icc-profiles-basiccolor-printing2009-1.2.0.tar.bz2
%define syscolordir     /usr/share/color
%define iccdirname      icc
%define cmmsubpath      colour/modules
%define settingsdirname settings
%define targetdirname   target
%define pixmapdir       /usr/share/pixmaps
%define icondir         /usr/share/icons
%define desktopdir      /usr/share/applications
Summary:        Colour Management Data from basICColor 

Name:           icc-profiles-basiccolor-printing2009
License:        Zlib
Group:          Productivity/Graphics/Other
Url:            http://www.colormanagement.org
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         %{_prefix}

BuildRequires:  color-filesystem

%description
Printing profiles according to ISO 12647-2. These are CMYK
ICC profiles for ISO Printing conditions.


%package      coat2
Summary:        Single Cmyk Profile from basICColor
Group:          Productivity/Graphics/Other
Requires:       color-filesystem

%description  coat2
Printing profile according to ISO 12647-2. This is one CMYK
ICC profile for a ISO Printing condition.

%package      extra
Summary:        Collection of Cmyk Profiles from basICColor
Group:          Productivity/Graphics/Other
Requires:       icc-profiles-basiccolor-printing2009-coat2

%description  extra
More printing profiles according to ISO 12647-2. This are all remaining
CMYK ICC profiles for ISO Printing conditions from the 2009 set.
The ISOcoated_v2_bas.ICC profile is packaged separately.

%package      doc
Summary:        Printing Profiles Documentation from basICColor
Group:          Productivity/Graphics/Other

%description  doc
Printing profiles according to ISO 12647-2. These are CMYK
ICC profiles documentation files for ISO Printing conditions.



%prep
%setup

%build
%configure --quick

%install
%make_install

%files	coat2
%defattr(-, root, root)
%dir %{syscolordir}/icc/basICColor
%{syscolordir}/icc/basICColor/ISOcoated_v2_bas.ICC

%files	extra
%defattr(-, root, root)
%{syscolordir}/icc/basICColor/ISOcoated_v2_300_bas.ICC
%{syscolordir}/icc/basICColor/ISOcoated_v2_grey1c_bas.ICC
%{syscolordir}/icc/basICColor/ISOnewspaper_v4_26_bas.ICC
%{syscolordir}/icc/basICColor/ISOuncoatedyellowish_bas.ICC
%{syscolordir}/icc/basICColor/PSO_Coated_300_NPscreen_ISO12647_bas.ICC
%{syscolordir}/icc/basICColor/PSO_Coated_NPscreen_ISO12647_bas.ICC
%{syscolordir}/icc/basICColor/PSO_LWC_Improved_bas.ICC
%{syscolordir}/icc/basICColor/PSO_LWC_Standard_bas.ICC
%{syscolordir}/icc/basICColor/PSO_MFC_Paper_bas.ICC
%{syscolordir}/icc/basICColor/PSO_SNP_Paper_bas.ICC
%{syscolordir}/icc/basICColor/PSO_Uncoated_ISO12647_bas.ICC
%{syscolordir}/icc/basICColor/PSO_Uncoated_NPscreen_ISO12647_bas.ICC
%{syscolordir}/icc/basICColor/SC_paper_bas.ICC

%files	doc
%defattr(-, root, root)
# This should go in the package docs, not with the profiles.
%doc default_profiles/printing/LICENSE-ZLIB-bICC default_profiles/printing/*.pdf

%changelog
