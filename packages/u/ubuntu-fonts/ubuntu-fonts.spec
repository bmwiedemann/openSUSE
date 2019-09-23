#
# spec file for package ubuntu-fonts
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define fontname ubuntu-font-family
Name:           ubuntu-fonts
Version:        0.83
Release:        0
Summary:        A unique, custom designed font that has a very distinctive look and feel
License:        SUSE-Ubuntu-Font-License-1.0
Group:          System/X11/Fonts
Url:            http://font.ubuntu.com
Source:         %{fontname}-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{reconfigure_fonts_prereq}

%description
The Ubuntu Font Family are a set of matching new libre/open fonts.
The development is being funded by Canonical on behalf the wider
Free Software community and the Ubuntu project. The technical font
design work and implementation is being undertaken by Dalton Maag.

Both the final font Truetype/OpenType files and the design files
used to produce the font family are distributed under an open
licence and you are expressly encouraged to experiment, modify,
share and improve. The typeface is sans-serif, uses OpenType
features and is manually hinted for clarity on desktop and
mobile computing screens.

The scope of the Ubuntu Font Family includes all the languages
used by the various Ubuntu users around the world in tune with
Ubuntu's philosophy which states that every user should be able
to use their software in the language of their choice. So the
Ubuntu Font Family project will be extended to cover many more
written languages.

%prep
%setup -q -n %{fontname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc CONTRIBUTING.txt FONTLOG.txt LICENCE-FAQ.txt LICENCE.txt copyright.txt README.txt TRADEMARKS.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
