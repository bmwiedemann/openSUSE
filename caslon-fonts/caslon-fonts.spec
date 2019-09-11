#
# spec file for package caslon-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define fontname ttf-caslon

Name:           caslon-fonts
Version:        20031202
Release:        0
Summary:        Caslon TrueType Fonts
License:        BSD-3-Clause
Group:          System/X11/Fonts
Url:            http://bibliofile.mc.duke.edu/gww/fonts/Unicode.html
# downloaded from
# http://bibliofile.mc.duke.edu/gww/fonts/Caslon/CasUni.zip
# and converted to tar.bz2 to save a bit of space
Source0:        %{fontname}-%{version}.tar.bz2
Source1:        license.html
Source2:        Unicode.html
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-bg
Provides:       scalable-font-el
Provides:       scalable-font-he
Provides:       scalable-font-ru
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Caslon TrueType font is a partial implementation of Unicode. I does
not contain

* CJK characters (ideographs)

* Asian & Indian alphabets and sylabaries

* Arabic

but it contains enough for most European languages including the
euro-sign.

%prep
%setup -n ttf-caslon
cp %{SOURCE1} %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.html
%{_ttfontsdir}

%changelog
