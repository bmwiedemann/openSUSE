#
# spec file for package papirus-icon-theme
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


Name:           papirus-icon-theme
Version:        20230104
Release:        0
Summary:        Papirus icon theme for Linux
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
Source:         https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  xmlstarlet
Requires(post): gtk3-tools
BuildArch:      noarch

%description
Papirus is an SVG icon theme, based on Paper with a few extras like
hardcode-tray support, kde-color-scheme support, libreoffice icon theme, filezilla theme, smplayer themes ...)
and other modifications. The theme is available for GTK and KDE.

This package contains the following icon themes:

ePapirus
ePapirus-Dark
Papirus
Papirus-Dark
Papirus-Light

%prep
%autosetup

%build

%check
make %{?_smp_mflags} test-all

%install
%make_install
%fdupes %{buildroot}

#remove duplicate LICENSE files
find %{buildroot}%{_datadir}/icons -name LICENSE -delete

%files
%doc README.md
%license LICENSE
%{_datadir}/icons/ePapirus
%{_datadir}/icons/ePapirus-Dark
%{_datadir}/icons/Papirus
%{_datadir}/icons/Papirus-Light
%{_datadir}/icons/Papirus-Dark

%changelog
