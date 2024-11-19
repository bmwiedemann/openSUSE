#
# spec file for package pantheon-wallpapers
#
# Copyright (c) 2024 SUSE LLC
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


%define         appid io.elementary.wallpapers
Name:           pantheon-wallpapers
Version:        8.0.0
Release:        0
Summary:        The desktop backgrounds for the Pantheon DE
License:        CC-BY-NC-SA-4.0 AND CC0-1.0
URL:            https://github.com/elementary/wallpapers
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildArch:      noarch
Provides:       elementary-wallpapers = %{version}
Obsoletes:      elementary-wallpapers < %{version}

%description
This package contains quality desktop backgrounds

%prep
%autosetup -n wallpapers-%{version}

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}

# remove wallpapers, which we can't ship
rm -f %{buildroot}%{_datadir}/backgrounds/{elementaryos-default,Martin\ Adams.jpg,Morskie\ Oko.jpg,Nattu\ Adnan.jpg,Tj\ Holowaychuk.jpg,Viktor\ Forgacs.jpg,A\ Large\ Body\ of\ Water\ Surrounded\ By\ Mountains.jpg,A\ Trail\ of\ Footprints\ In\ The\ Sand.jpg,Photo\ of\ Valley.jpg,Snow-Capped\ Mountain.jpg}

%files
%doc README.md
%{_datadir}/backgrounds
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
