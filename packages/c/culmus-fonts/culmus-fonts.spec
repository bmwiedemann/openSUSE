#
# spec file for package culmus-fonts
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define upstream_name  culmus

Name:           culmus-fonts
Version:        0.140
Release:        0
Summary:        A set of Hebrew fonts
License:        GPL-2.0-or-later
Group:          System/X11/Fonts
URL:            https://culmus.sourceforge.io/
Source0:        https://sourceforge.net/projects/culmus/files/culmus/%{version}/culmus-%{version}.tar.gz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
A set of 15 Hebrew font families. Those families provide a basic set
of a serif (Frank Ruehl), sans serif (Nachlieli), and monospaced
(Miriam Mono) fonts. ASCII glyphs are partially borrowed from the URW
and Bitstream fonts. Also included Miriam, Drugulin, Aharoni, David,
Yehuda, and Ellinia.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build

%install
mkdir -p %{buildroot}%_ttfontsdir
install -m 0644 *.ttf *.otf \
        %{buildroot}%_ttfontsdir

%reconfigure_fonts_scriptlets

%files
%doc CHANGES fonts.scale-ttf culmus.conf
%license GNU-GPL LICENSE LICENSE-BITSTREAM
%_ttfontsdir

%changelog
