#
# spec file for package wyrmsun
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.5.4
Release:        0
Summary:        Strategy game based on history, mythology and fiction
License:        GPL-2.0-only AND CC-BY-SA-3.0
Group:          Amusements/Games/Strategy/Real Time
URL:            https://andrettin.github.io/
Source:         https://github.com/Andrettin/Wyrmsun/archive/v%{version}/Wyrmsun-%{version}.tar.gz
Patch0:         wyrmsun-dont-search-for-a-compiler.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version} < 1330
BuildRequires:  update-desktop-files
%endif
Requires:       wyrmgus = %{version}
BuildArch:      noarch

%description
In the Wyrmsun universe a myriad of inhabited planets exist. Humans dwell on Earth,
while dwarves inhabit Nidavellir and elves nourish the world of Alfheim. These
peoples struggle to carve a place for themselves with their tools of stone, bronze
and iron. And perhaps one day they will meet one another, beyond the stars...

%prep
%setup -q -n Wyrmsun-%{version}
%patch0 -p1

%build
%cmake

%install
%cmake_install
rm -Rf %{buildroot}%{_datadir}/doc/wyrmsun/
%fdupes -s %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license license.txt
%doc readme.txt
%doc "documents/Wyrmsun - Visual Guide.pdf"
%{_bindir}/wyrmsun
%{_datadir}/wyrmsun
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
