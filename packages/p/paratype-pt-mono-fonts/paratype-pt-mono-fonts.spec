#
# spec file for package paratype-pt-mono-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           paratype-pt-mono-fonts
Version:        1.003OFL
Release:        0
Summary:        Monospaced Fonts for Minority Languages of Russia
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTMonoOFL.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Provides:       locale(be;ru;uk)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
PT Mono was developed for the special needs — for use in forms, tables,
work sheets etc. Equal widths of characters are very helpful in setting
complex documents, with such font you may easily calculate size of entry
fields, column widths in tables and so on. One of the most important
area of use is Web sites of “electronic governments“ where visitors have
to fill different request forms. Currently PT Mono consists of Regular
and Bold styles.

The fonts beside standard Western, Central European and Cyrillic code
pages contain characters of all title languages of Russian Federation
that make them unique and very important tool of the modern digital
communications.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' PTSSM_OFL.txt

%build

%install
install -dm 0755 %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc PTSSM_OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
