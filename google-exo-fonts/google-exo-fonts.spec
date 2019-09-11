#
# spec file for package google-exo-fonts
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


%define  fontname   exo

Name:           google-exo-fonts
Version:        0.9pre
Release:        0
Summary:        Contemporary Geometric Sans Serif Typeface
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://code.google.com/webfonts/family?family=Exo
Source0:        %{fontname}.tar.bz2
Source1:        OFL.txt
BuildRequires:  bzip2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Exo is a contemporary geometric sans serif typeface that
tries to convey a technological/futuristic feeling while
keeping an elegant design. Exo was meant to be a very
versatile font, so it has 9 weights (the maximum on the web)
each with a true italic version. It works great as a display
face but it also works good for small to intermediate size texts.

Designer: Natanael Gama

%prep
%setup -q -n %{fontname} -c %{fontname}

%build
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 exo/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%doc OFL.txt

%changelog
