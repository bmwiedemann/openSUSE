#
# spec file for package cyreal-lobster-cyrillic-fonts
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


Name:           cyreal-lobster-cyrillic-fonts
Version:        1.4
Release:        0
License:        OFL-1.1
Summary:        Lobster Cyrillic Font
Url:            http://cyreal.org/archives/373
Group:          System/X11/Fonts
#Source0:       wget http://www.google.com/webfonts/download?kit=V9dGwk5Wx0cNwNcoYGYKAqCWcynf_cDxXwCLxiixG1c -O cyreal-lobster-cyrillic-fonts.zip
Source0:        cyreal-lobster-cyrillic-fonts.zip
BuildRequires:	fontpackages-devel
BuildRequires:  unzip
Provides:       locale(ru;uk)
Provides:       lobster-cyrillic-fonts = %{version}
# FIXME: This causes a rpmlint warning; change "<=" to "<" once there's
# a new upstream version.
Obsoletes:      lobster-cyrillic-fonts <= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A lovely Bold Condensed Script fully loaded with hundreds of ligatures
and alternates.

Lobster Cyrillic includes:
- 99 Cyrillic ligatures.
- 25 ending glyphs.
- 100 ending ligatures.
- 2 initial ligatures.
- Ukrainian Hryvnia and Russian Ruble currency symbols.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' OFL.txt

%build

%install
install -Dm 644 Lobster.ttf %{buildroot}%{_ttfontsdir}/Lobster.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/Lobster.ttf

%changelog
