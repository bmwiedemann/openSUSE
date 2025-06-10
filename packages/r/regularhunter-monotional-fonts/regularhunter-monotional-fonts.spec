#
# spec file for package regularhunter-monotional-fonts
#
# Copyright (c) 2025 SUSE LLC
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


Name:           regularhunter-monotional-fonts
Version:        1.9
Release:        0
Summary:        A humanist, monospace font based on DejaVu
License:        Apache-2.0
Group:          System/X11/Fonts
URL:            https://github.com/regularhunter/monotional-font
Source0:        Monotional_v%{version}.zip
Source1:        README.md
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Recommends:     monotional-fonts
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A humanist, monospace font based on DejaVu Sans Mono and inspired by 
André Berg's Meslo.

%prep
%autosetup -n "Monotional_v%{version}" -p1
cp %{SOURCE1} .

%build

%install
mkdir -p "%{buildroot}/%{_ttfontsdir}"
install -Dpm 644 *.ttf "%{buildroot}/%{_ttfontsdir}/"

%reconfigure_fonts_scriptlets

%files
%doc LICENSE COPYRIGHT README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
