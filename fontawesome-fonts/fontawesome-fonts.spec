#
# spec file for package fontawesome-fonts
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fontawesome-fonts
Version:        4.7.0
Release:        0
Summary:        Iconic font set
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://fontawesome.io/
Source0:        http://fontawesome.io/assets/font-awesome-%{version}.zip
Source1:        README-Trademarks.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n font-awesome-%{version}
cp -p %{SOURCE1} .

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -p -m 0644 fonts/*.ttf fonts/*.otf fonts/*.woff %{buildroot}%{_ttfontsdir}

install -m 0755 -d %{buildroot}%{_datadir}/font-awesome-web
install -p -m 0644 fonts/*.svg %{buildroot}%{_datadir}/font-awesome-web
cp -r css less scss %{buildroot}%{_datadir}/font-awesome-web/

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc README-Trademarks.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%files web
%defattr(-, root,root)
%{_datadir}/font-awesome-web/

%changelog
