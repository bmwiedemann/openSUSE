#
# spec file for package sil-abyssinica-fonts
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


Name:           sil-abyssinica-fonts
Version:        1.0
Release:        0
Summary:        Smart Unicode Font for the Ethiopic Script (Amharic)
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=AbyssinicaSIL
Source0:        AbyssinicaSIL1.0.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Provides:       locale(so)
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      sil-abyssinica <= %{version}
Provides:       sil-abyssinica = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Ethiopic script is used for writing many of the languages of
Ethiopia and Eritrea.  Ethiopic (U+1200..U+137F) was added to Unicode
3.0.  Ethiopic Supplement (U+1380..U+139F) and Ethiopic Extended
(U+2D80..U+2DDF) were added to Unicode 4.1. Abyssinica SIL supports all
Ethiopic characters which are in Unicode including the Unicode 4.1
extensions. Some languages of Ethiopia are not yet able to be fully
represented in Unicode and, where necessary, we have included
non-Unicode characters in the Private Use Area (see Private-use (PUA)
characters supported by Abyssinica SIL).

Abyssinica SIL is based on Ethiopic calligraphic traditions. This
release is a regular typeface, with no bold or italic version available
or planned.

%prep
%setup -T -c sil-abyssinica -n sil-abyssinica
unzip -j $RPM_SOURCE_DIR/AbyssinicaSIL1.0.zip
chmod 644 *
dos2unix *.txt

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.txt *.pdf
%{_ttfontsdir}

%changelog
