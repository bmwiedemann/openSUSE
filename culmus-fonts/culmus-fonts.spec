#
# spec file for package culmus-fonts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define type1dir %{_fontsdir}/Type1
%define upstream_name  culmus

Name:           culmus-fonts
Version:        0.132
Release:        0
Summary:        A set of Hebrew fonts
License:        GPL-2.0-or-later
Group:          System/X11/Fonts
Url:            http://culmus.sourceforge.net/
Source0:        %{upstream_name}-%{version}.tar.gz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       locale(he)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A set of 15 Hebrew font families. Those families provide a basic set
of a serif (Frank Ruehl), sans serif (Nachlieli), and monospaced
(Miriam Mono) fonts. ASCII glyphs are partially borrowed from the URW
and Bitstream fonts. Also included Miriam, Drugulin, Aharoni, David,
Yehuda, and Ellinia.

%prep
%setup -q -n %{upstream_name}-%{version}

%build

%install
mkdir -p %{buildroot}%_ttfontsdir
install -m 0644 *.ttf *.otf \
        %{buildroot}%_ttfontsdir
mkdir -p %{buildroot}%type1dir
install -c -m 644 *.afm *.pf? %{buildroot}%type1dir
install -c -m 644 fonts.scale-type1 \
        %{buildroot}%type1dir/fonts.scale.culmus

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc CHANGES fonts.scale-ttf culmus.conf GNU-GPL LICENSE LICENSE-BITSTREAM
%type1dir
%_ttfontsdir

%changelog
