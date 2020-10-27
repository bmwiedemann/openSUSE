#
# spec file for package openmoji-fonts
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


%define ttf_fontdir %{_datadir}/fonts/truetype
%define fontname     openmoji
Name:           openmoji-fonts
Version:        12.4.0+git.1595925010.16e293b40
Release:        0
Summary:        OpenMoji fonts
License:        CC-BY-SA-4.0
Group:          System/X11/Fonts
URL:            https://openmoji.org/
Source:         %{fontname}-%{version}.tar.xz
%reconfigure_fonts_prereq
BuildRequires:  %suseconfig_fonts_prereq
BuildRequires:  fontpackages-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
OpenMoji was developed with visual guidelines that are not linked to a
specific branding. In addition, the goal was to design emojis that
integrate well in combination with text.

%package -n OpenMoji-Black
Summary:        Black only color emoji
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n OpenMoji-Black
Black color only variation of Openmoji glyphs.

%package -n OpenMoji-Color
Summary:        Colorful emoji
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n OpenMoji-Color
Colorful variation of Openmoji glyphs.

%prep
%setup -n %{fontname}-%{version} 

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 font/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n OpenMoji-Black
%reconfigure_fonts_scriptlets -n OpenMoji-Color

%files -n OpenMoji-Black
%dir %{_ttfontsdir}/
%{_ttfontsdir}/OpenMoji-Black.*

%files -n OpenMoji-Color
%dir %{_ttfontsdir}/
%{_ttfontsdir}/OpenMoji-Color.*

%doc changelog.txt CONTRIBUTING.md README.md 
%license FAQ.md

%changelog
