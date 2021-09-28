#
# spec file for package consoleet-oldschoolpc-fonts
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


Name:           consoleet-oldschoolpc-fonts
Version:        2.2
Release:        0
Summary:        Smooth-edge versions of int10h's IBM/PC fonts
License:        CC-BY-SA-4.0
Group:          System/X11/Fonts
URL:            https://inai.de/projects/consoleet/
Source:         https://inai.de/files/consoleet/consoleet-oldschoolpc-%version.tar.zst
Source2:        https://inai.de/files/consoleet/consoleet-oldschoolpc-%version.tar.zst.asc
BuildRequires:  fontpackages-devel
BuildRequires:  zstd
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A modification of the int10h oldschoolpc font pack with some fonts
redone with smooth edges.

%prep
%setup -Tcq
tar --use=zstd --strip-components=1 -xf %SOURCE0

%build

%install
mkdir -p "%buildroot/%_ttfontsdir"
cp -av *.otf "%buildroot/%_ttfontsdir/"

%reconfigure_fonts_scriptlets

%files
%license license.txt
%_ttfontsdir/

%changelog
