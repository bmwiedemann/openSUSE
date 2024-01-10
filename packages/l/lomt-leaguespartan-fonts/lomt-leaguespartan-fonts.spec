#
# spec file for package lomt-leaguespartan-fonts
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

%global desc League Spartan is The League Of Moveable Type's interpretation of Matt Bailey's Spartan, a typeface based on early 20th century American geometric sans serifs.
Name:           lomt-leaguespartan-fonts
Version:        2.220
Release:        0
Summary:        A contemporary serif typeface family for long-form reading
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/theleagueof/league-spartan
Source0:        %{url}/releases/download/%{version}/LeagueSpartan-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
%{desc}

%package -n lomt-leaguespartan-variable-fonts
Summary:        A contemporary serif typeface family for long-form reading (variable version)
%reconfigure_fonts_prereq

%description -n lomt-leaguespartan-variable-fonts
%{desc} This package contains the variable version of fonts.

%prep
%autosetup -n LeagueSpartan-%{version}

%build

%install
install -dm0755 %{buildroot}%{_ttfontsdir}
install -m0644 {static,variable}/TTF/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license OFL.md
%doc README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf
%exclude %{_ttfontsdir}/LeagueSpartan-VF.ttf

%files -n lomt-leaguespartan-variable-fonts
%license OFL.md
%doc README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/LeagueSpartan-VF.ttf

%changelog
