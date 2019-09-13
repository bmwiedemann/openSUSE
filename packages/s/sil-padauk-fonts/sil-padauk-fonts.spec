#
# spec file for package sil-padauk-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sil-padauk-fonts
Version:        2.2
Release:        0
Summary:        Smart Unicode Font for the Myanmar Script
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=Padauk
Source0:        padauk_2_2.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       locale(my)
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      sil-padauk <= %{version}
Provides:       sil-padauk = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
As part of the Unicode development effort, the encoding for the Myanmar
script is being extended. These changes are being voted on as part of a
PDAM and as such fonts that support these encoding extensions are not
officially Unicode compliant with any current version of Unicode.
Padauk conforms to the proposed extensions in anticipation of their
being accepted into the Unicode standard.

Users wishing to find a font capable of supporting Unicode data today
should look elsewhere. They should also be made aware that assuming the
extensions are accepted into Unicode, then they will need to transcode
their data to continue to be conforming.

Padauk supports the Myanmar script extensions including changes to how
Burmese is encoded, Sgaw Karen and Mon. Padauk continues to be
developed so should you find problems with the font, please send
feedback to SIL_fonts@sil.org.	Requirements

Padauk includes the necessary Graphite smarts to render Myanmar script
correctly. Thus if you want to use this font you will need the Graphite
libraries and Graphite capable applications or graphics extensions.

%prep
%setup -n ttf-sil-padauk-%{version}
dos2unix OFL*

%build
chmod 644 font-source/myanmar5.gdl

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%clean

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc FONTLOG OFL OFL-FAQ font-source
%{_ttfontsdir}

%changelog
