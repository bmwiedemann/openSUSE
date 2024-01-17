#
# spec file for package paglinawan-quicksand-fonts
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

%define fontname Quicksand

Name:           paglinawan-quicksand-fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Summary:        Geometric-style sans serif
Version:        1.0.20120829
Release:        1
URL:            http://www.fontsquirrel.com/fonts/Quicksand
Source0:        %{fontname}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  unzip
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq

%description
From http://andrewpaglinawan.com/category/typefaces/#quicksand:
Quicksand is a sans serif type family of three weights plus matching
obliques and a dash version for display and headings. Influenced by
the geometric-style sans serif faces that were popular during the
1920s and 30s, the fonts are based on geometric forms that have been
optically corrected for better legibility.

Designers: Andrew Paglinawan


%prep
%setup -c -n %{fontname}-%{version}
unzip -n %{S:0}
# find . -name \*.txt -print0 | xargs -0 dos2unix


%build
# --- Nothing to do ---


%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(0644,root,root,755)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*


%changelog
