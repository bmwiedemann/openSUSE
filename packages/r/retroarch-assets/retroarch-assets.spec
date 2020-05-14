#
# spec file for package retroarch-assets
#
# Copyright (c) 2020 SUSE LLC
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


Name:           retroarch-assets
Version:        0~git20200505
Release:        0
Summary:        RetroArch Assets
License:        CC-BY-4.0
Group:          System/Emulators/Other
URL:            https://github.com/libretro/retroarch-assets

Source:         %{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  google-droid-fonts
BuildRequires:  make
BuildArch:      noarch

Requires:       google-droid-fonts
Requires:       retroarch

%description
Assets needed for RetroArch - e.g. menu drivers, etc. Also contains the official branding.

%prep
%setup -q

%build

%install
%make_install
%fdupes -s %{buildroot}

# Use Droid Sans Fallback because the RetroArch font doesn't support Chinese and Korean
rm %{buildroot}%{_datadir}/libretro/assets/xmb/monochrome/font.ttf
ln -s %{_datadir}/fonts/truetype/DroidSansFallbackFull.ttf %{buildroot}%{_datadir}/libretro/assets/xmb/monochrome/font.ttf

%files
%license COPYING
%dir %{_datadir}/libretro
%{_datadir}/libretro/assets

%changelog
