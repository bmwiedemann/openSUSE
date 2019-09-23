#
# spec file for package sil-andika-fonts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           sil-andika-fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Summary:        Sans serif, Unicode-compliant Font For Literacy Use
Version:        5.000
Release:        0
URL:            http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=andika
Source0:        Andika-%{version}.zip
Source1:        AndikaNewBasic-5.500.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Andika is a sans serif, Unicode-compliant font designed
especially for literacy use, taking into account the needs of
beginning readers. The focus is on clear, easy-to-perceive
letterforms that will not be readily confused with one another.

A sans serif font is preferred by some literacy personnel for
teaching people to read. Its forms are simpler and less cluttered
than those of most serif fonts.

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
# --- Nothing to do ---


%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.odt *.pdf *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*


%changelog
