#
# spec file for package wyrmsun
#
# Copyright (c) 2022 SUSE LLC
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


Name:           wyrmsun
Version:        5.3.6
Release:        0
Summary:        Strategy game based on history, mythology and fiction
License:        CC-BY-SA-3.0 AND GPL-2.0-only
Group:          Amusements/Games/Strategy/Real Time
URL:            https://andrettin.github.io/
Source:         https://github.com/Andrettin/Wyrmsun/archive/v%{version}/Wyrmsun-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       wyrmgus = %{version}
BuildArch:      noarch

%description
In the Wyrmsun universe a myriad of inhabited planets exist. Humans dwell on Earth,
while dwarves inhabit Nidavellir and elves nourish the world of Alfheim. These
peoples struggle to carve a place for themselves with their tools of stone, bronze
and iron. And perhaps one day they will meet one another, beyond the stars...

%prep
%setup -q -n Wyrmsun-%{version}

%build
%cmake -DBIN_DIR=bin

%install
%cmake_install
rm -R %{buildroot}%{_datadir}/doc/wyrmsun/
%fdupes -s %{buildroot}%{_datadir}

%files
%license license.txt
%doc readme.txt
%doc "documents/Wyrmsun - Visual Guide.pdf"
%{_bindir}/wyrmsun
%{_datadir}/wyrmsun
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
