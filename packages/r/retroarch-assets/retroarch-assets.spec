#
# spec file for package retroarch-assets
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


Name:           retroarch-assets
Version:        0~git20210903
Release:        0
Summary:        RetroArch Assets
License:        CC-BY-4.0
Group:          System/Emulators/Other
URL:            https://github.com/libretro/retroarch-assets

Source:         %{name}-%{version}.tar.xz

BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  google-droid-fonts
BuildRequires:  make
BuildArch:      noarch

Requires:       dejavu-fonts
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

rm %{buildroot}%{_datadir}/libretro/assets/pkg/fallback-font.ttf
rm %{buildroot}%{_datadir}/libretro/assets/pkg/chinese-fallback-font.ttf
ln -s %{_datadir}/fonts/truetype/DroidSansFallbackFull.ttf %{buildroot}%{_datadir}/libretro/assets/pkg/chinese-fallback-font.ttf
ln -s %{_datadir}/fonts/truetype/DejaVuSans.ttf %{buildroot}%{_datadir}/libretro/assets/pkg/fallback-font.ttf

%files
%license COPYING
%dir %{_datadir}/libretro
%{_datadir}/libretro/assets

%changelog
