#
# spec file for package fira-code-fonts
#
# Copyright (c) 2021 SUSE LLC
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


Name:           fira-code-fonts
Version:        6.2
Release:        0
Summary:        Free monospaced font with programming ligatures
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/tonsky/FiraCode
Source0:        https://github.com/tonsky/FiraCode/releases/download/%{version}/Fira_Code_v%{version}.zip
Source100:      https://raw.githubusercontent.com/tonsky/FiraCode/%{version}/LICENSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%reconfigure_fonts_prereq

%description
Fira Code is a free monospaced font containing ligatures for common programming multi-character combinations. This is just a font rendering feature: underlying code remains ASCII-compatible. This helps to read and understand code faster.

%prep
unzip -qq %{_sourcedir}/Fira_Code_v%{version}.zip '*.ttf' '*.txt'
cp %{SOURCE100} .

%build

%install
mkdir -p %{buildroot}/%{_ttfontsdir}
install -c -m 644 ttf/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -c

%files
%license LICENSE
%doc README.txt
%{_ttfontsdir}

%changelog
