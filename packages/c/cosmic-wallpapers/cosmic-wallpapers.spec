#
# spec file for package cosmic-wallpapers
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


Name:           cosmic-wallpapers
Version:        1.0.0~alph4+0
Release:        0
Summary:        Wallpapers for the COSMIC Desktop Environment
License:        CC-BY-4.0 OR  CC0-1.0
URL:            https://github.com/pop-os/cosmic-wallpapers
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  make
BuildRequires:  zstd

%description
%{summary}.

%prep
%autosetup

%build

%install
%make_install prefix=%{_prefix}

# wallpapers we can't ship
rm -f %{buildroot}%{_datadir}/backgrounds/cosmic/{otherworldly_earth_nasa_ISS064-E-29444.jpg,round_moons_nasa.jpg,phytoplankton_bloom_nasa_oli2_20240121.jpg}

%files
%doc README.md
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/cosmic

%changelog
