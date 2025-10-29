#
# spec file for package cantarell-fonts
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


Name:           cantarell-fonts
Version:        0.303.1
Release:        0
Summary:        Contemporary Humanist Sans Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://wiki.gnome.org/Projects/CantarellFonts
Source0:        https://download.gnome.org/sources/cantarell-fonts/0.303/%{name}-%{version}.tar.xz

# needed for directory ownership
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(appstream)
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Cantarell font family is a contemporary Humanist sans serif designed
for on-screen reading.

%prep
%autosetup

%build
%meson \
	-Dfontsdir=%{_ttfontsdir} \
	-Duseprebuilt=true \
	%{nil}
%meson_build

%install
%meson_install

%reconfigure_fonts_scriptlets

%files
%license COPYING
%doc NEWS README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/Cantarell-VF.otf
%{_datadir}/metainfo/org.gnome.cantarell.metainfo.xml

%changelog
