#
# spec file for package consoleet-fixedsys-fonts
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           consoleet-fixedsys-fonts
Version:        3.09.10
Release:        0
Summary:        Smooth-edge version of Fixedsys Excelsior
License:        SUSE-Public-Domain
Group:          System/X11/Fonts
URL:            https://inai.de/projects/consoleet/
Source:         https://inai.de/files/consoleet/consoleet-fixedsys-%version.zip
Source2:        https://inai.de/files/consoleet/consoleet-fixedsys-%version.zip.asc
Source3:        %name.keyring
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Smooth-edge versions of the Fixedsys Excelsior font.

%prep
%autosetup -n consoleet-fixedsys-%version

%build

%install
mkdir -pv "%buildroot/%_ttfontsdir"
cp -av *.otf "%buildroot/%_ttfontsdir/"

%reconfigure_fonts_scriptlets

%files
%license *README*
%_ttfontsdir/

%changelog
