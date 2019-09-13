#
# spec file for package vollkorn-fonts
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


%define fontname vollkorn

Name:           vollkorn-fonts
Version:        4.105
Release:        0
Summary:        A serif font for everyday use
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://vollkorn-typeface.com/
Source0:        http://vollkorn-typeface.com/download/%{fontname}-4-105.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Vollkorn is a text face with dark and meaty serifs and a bouncing look.
It might be used as body type as well as for headlines or titles.

("Vollkorn" is German for »wholemeal« which refers to the old term
"Brotschrift".)

%prep
%setup -T -c %{name} -n %{name}
unzip %{SOURCE0}
chmod 644 *.txt TTF/*.ttf
# Remove DOS line endings:
for i in *.txt; do
 sed -i 's/.$//' $i
done
rm -Rf __MACOSX/ EOT/ PS-OTF/ WOFF/ WOFF2/

%build
# -- nop --

%install
mkdir -p  %{buildroot}%{_ttfontsdir}/
install -c -m 644 TTF/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.txt
%{_ttfontsdir}

%changelog
