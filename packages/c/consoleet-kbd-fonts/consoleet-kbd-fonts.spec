#
# spec file for package consoleet-kbd-fonts
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


Name:           consoleet-kbd-fonts
Version:        1.3
Release:        0
Summary:        Vector/OTF versions of some classic kbd fonts
License:        CC-BY-SA-4.0
Group:          System/X11/Fonts
URL:            https://inai.de/projects/consoleet/
Source:         https://inai.de/files/consoleet/consoleet-kbd-%version.tar.zst
Source2:        https://inai.de/files/consoleet/consoleet-kbd-%version.tar.asc
Source9:        %name.keyring
BuildRequires:  fontpackages-devel
BuildRequires:  zstd
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
These are OpenType remakes of (some of) the VGA bitmap fonts otherwise
found in the "kbd" package and in /usr/share/kbd/consolefonts/.

%prep
%setup -Tcq
tar --use=zstd --strip-components=1 -xf %SOURCE0

%build

%install
mkdir -pv "%buildroot/%_ttfontsdir"
cp -av *.otf "%buildroot/%_ttfontsdir/"

%reconfigure_fonts_scriptlets

%files
%_ttfontsdir/

%changelog
