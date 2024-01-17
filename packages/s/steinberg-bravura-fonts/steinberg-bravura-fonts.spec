#
# spec file for package steinberg-bravura-fonts
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


Name:           steinberg-bravura-fonts
Version:        1.392
Release:        0
Summary:        A complete, SMuFL compliant music font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://www.smufl.org/fonts/
Source:         bravura-%{version}.tar.xz
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Bravura is the reference music font for the Standard Music Font Layout
(SMuFL) specification, fully compliant with SMuFL 1.2.

%prep
%setup -q -n bravura-%{version}

%build
# Nothing to do

%install
# The actual SMuFL music font files
install -Dpm 644 otf/*.otf -t %{buildroot}%{_ttfontsdir}/

# call fonts-config after installation or deinstallation of this package
%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%doc bravura-text.md FONTLOG.txt
%{_ttfontsdir}

%changelog
