#
# spec file for package google-worksans-fonts
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


%define fontname Work-Sans

Name:           google-worksans-fonts
Version:        1.6+git145.18037a0
Release:        0
Summary:        A Grotesque Sans Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/weiweihuanghuang/Work-Sans
Source:         %fontname-%version.tar.xz
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Work Sans is a typeface family with 9 weights, and based loosely on
early Grotesques — for example, Stephenson Blake, Miller & Richard
and Bauerschen Giesserei.

Work Sans had been updated between 2018–2020 with accompanying italics, variable
font files and the character set had been expanded to the Google Latin Expert
glyph set, which supports Vietnamese.

%prep
%setup -q -n %{fontname}-%{version}
chmod -x *.md *.txt

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -p -m 0644 fonts/static/TTF/*.ttf %{buildroot}/%{_ttfontsdir}/

# call fonts-config after installation or deinstallation of this package
%reconfigure_fonts_scriptlets

%files
%doc README.md
%license OFL.txt
%{_ttfontsdir}

%changelog
