#
# spec file for package hartke-aurulentsans-fonts
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

Name:           hartke-aurulentsans-fonts
Version:        20070504
Release:        0
Summary:        A Sans-Serif Font for Use as Primary Interface Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://delubrum.org/
Source0:        AurulentSans-%{version}.tgz
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Aurulent Sans is a humanist sans serif intended to be used as an
interface font. The width and style is reminiscent of Luxi Sans,
Lucida Sans, Tahoma, and Andale Sans UI. Aurulent currently ha
s four styles: regular, italic, bold, and bold italic.

Designer: Stephen G. Hartke


%prep
%setup -T -c %{name} -n %{name}
tar xzvf %{SOURCE0}


%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc README
%{_ttfontsdir}

%changelog
