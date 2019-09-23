#
# spec file for package sil-gentium-fonts
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sil-gentium-fonts
Version:        5.000
Release:        0
Summary:        A International Typeface for Languages Using the Latin Script
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=Gentium
Source0:        GentiumPlus-%{version}.zip
Source1:        GentiumBasic_110.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Provides:       GentiumBasic
Provides:       GentiumPlus
Provides:       locale(vi)
# FIXME: This causes a rpmlint warning; change <= to < once there's a new upstream version
Obsoletes:      gentium <= 1.508
Provides:       gentium = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Gentium is a typeface family designed to enable the diverse ethnic
groups around the world who use the Latin script to produce readable,
high-quality publications. It supports a wide range of Latin-based
alphabets and includes glyphs that correspond to all the Latin ranges
of Unicode.

%prep
%setup -T -c %{name} -n %{name}
unzip -j %{SOURCE0}
unzip -j -n %{SOURCE1}
chmod 644 *.txt *.ttf
# Remove DOS line endings:
for i in *.txt; do
 sed -i 's/.$//' $i
done

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.txt
%{_ttfontsdir}

%changelog
