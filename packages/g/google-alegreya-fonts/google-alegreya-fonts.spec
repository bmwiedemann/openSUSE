#
# spec file for package google-alegreya-fonts
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


%define fontname alegreya

Name:           google-alegreya-fonts
Version:        1.003
Release:        0
Summary:        Serif Font for Literature
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://code.google.com/webfonts/family?family=Alegreya
Source0:        %{fontname}.tar.bz2
Source1:        %{fontname}sc.tar.bz2
BuildRequires:  bzip2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Alegreya was chosen as one of 53 "Fonts of the Decade" at
the ATypI Letter2 competition in September 2011, and one
of the top 14 text type systems. It was also selected in
the 2nd Bienal Iberoamericana de Diseño, competition
held in Madrid in 2010.

Alegreya is a typeface originally intended for literature.
Among its crowning characteristics, it conveys a dynamic
and varied rhythm which facilitates the reading of long
texts. Also, it provides freshness to the page while
referring to the calligraphic letter, not as a literal
interpretation, but rather in a contemporary typographic language.

Designed by Juan Pablo del Peral for Huerta Tipográfica.

%prep
%setup -c %{name} -n %{name}
tar xjvf %{SOURCE1}

%build
chmod 644 alegreyasc/OFL.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 %{fontname}/*.ttf %{fontname}sc/*.ttf \
  %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%doc %{fontname}sc/OFL.txt

%changelog
