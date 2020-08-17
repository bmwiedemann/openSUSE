#
# spec file for package fontawesome-fonts
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           fontawesome-fonts
Version:        5.14.0
Release:        0
Summary:        Iconic font set
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://fontawesome.io/
Source0:        https://github.com/FortAwesome/Font-Awesome/releases/download/%{version}/fontawesome-free-%{version}-desktop.zip
Source1:        https://github.com/FortAwesome/Font-Awesome/releases/download/%{version}/fontawesome-free-%{version}-web.zip
Source2:        LICENSE.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Scalable vector icons that can be customized — size, color, drop shadow,
and anything that can be done with the power of CSS.

(Note that the font does not contain regular letters, and that icons
are in the range U+F000..U+F23A.)

%package web
Summary:        Web files for font-awesome
License:        MIT
Group:          System/X11/Fonts

%description web
Web files (css, less, scss, etc) for font-awesome.

%prep
%setup -q -c
%setup -q -T -D -a 1
cp -p %{SOURCE2} .

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -p -m 0644 */otfs/*.otf %{buildroot}%{_ttfontsdir}

install -m 0755 -d %{buildroot}%{_datadir}/fontawesome-web/webfonts
install -p -m 0644 */webfonts/*.{ttf,woff,woff2,svg,eot} %{buildroot}%{_datadir}/fontawesome-web/webfonts
cp -r */css */less */scss %{buildroot}%{_datadir}/fontawesome-web/

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%license LICENSE.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%files web
%defattr(-, root,root)
%{_datadir}/fontawesome-web/

%changelog
