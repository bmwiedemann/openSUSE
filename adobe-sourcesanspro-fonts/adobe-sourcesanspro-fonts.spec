#
# spec file for package adobe-sourcesanspro-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Dominique Leuenberger, Amsterdam, Netherlands
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


%define it_version 1.095
%define ro_version 2.045
%define _name SourceSansPro
Name:           adobe-sourcesanspro-fonts
Version:        %{ro_version}
Release:        0
Summary:        A set of OpenType fonts designed for user interfaces
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe/source-sans-pro/
Source:         https://github.com/adobe-fonts/source-sans-pro/releases/download/%{version}R-ro%2F%{it_version}R-it/source-sans-pro-%{ro_version}R-ro-%{it_version}R-it.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Source Sans is a set of OpenType fonts that have been designed to work well in user interface (UI) environments, as well as in text setting for screen and print.

%prep
%setup -q -n source-sans-pro-%{ro_version}R-ro-%{it_version}R-it
# Fix line endings
sed -i 's/\r$//g' LICENSE.txt
# fix spurious-executable-perm
chmod -x README.md

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 OTF/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license LICENSE.txt
%doc *.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
