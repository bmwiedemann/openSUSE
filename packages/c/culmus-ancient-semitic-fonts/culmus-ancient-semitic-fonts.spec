#
# spec file for package culmus-ancient-semitic-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define src_name  AncientSemiticFonts
%define src_ver   0.06
%define src_rel   1

Name:           culmus-ancient-semitic-fonts
Version:        %{src_ver}.%{src_rel}
Release:        0
Summary:        Ancient Semitic Fonts
License:        GPL-2.0
Group:          System/X11/Fonts
Url:            http://culmus.sourceforge.net/ancient/index.html
Source0:        http://sourceforge.net/projects/culmus/files/ancient_fonts/AncientSemiticFonts-%{src_ver}-%{src_rel}/AncientSemiticFonts-0.06-1.tgz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Collection of fonts related to the history of the Hebrew writing.

%prep
%setup -q -n %{src_name}-%{src_ver}-%{src_rel}

%build
# Keter YG already part of culmus-fonts
rm src/KeterYG*.ttf

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 src/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc CHANGES GNU-GPL LICENSE README
%{_ttfontsdir}

%changelog
