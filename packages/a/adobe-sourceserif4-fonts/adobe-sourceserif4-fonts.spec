#
# spec file for package adobe-sourceserif4-fonts
#
# Copyright (c) 2023 SUSE LLC
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


Name:           adobe-sourceserif4-fonts
Version:        4.005
Release:        0
Summary:        A set of OpenType fonts designed for user interfaces
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe-fonts/source-serif/
Source0:        https://github.com/adobe-fonts/source-serif/archive/refs/tags/%{version}R.zip#/source-serif-%{version}R.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A set of serif OpenType fonts designed to complement Source Sans

%prep
%setup -q -n source-serif-%{version}R
# Fix line endings
sed -i 's/\r$//g' LICENSE.md

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 OTF/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license LICENSE.md
%doc README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
