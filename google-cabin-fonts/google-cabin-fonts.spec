#
# spec file for package google-cabin-fonts
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


%define fontname cabin

Name:           google-cabin-fonts
Version:        1.005
Release:        0
Summary:        Humanist Sans Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.impallari.com
Source0:        %{fontname}.tar.bz2
Source1:        %{fontname}condensed.tar.bz2
BuildRequires:  bzip2
BuildRequires:  dos2unix
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Cabin font family is a humanist sans with 4 weights and true
italics, inspired by Edward Johnston’s and Eric Gill’s typefaces,
with a touch of modernism.

Cabin incorporates modern proportions, optical adjustments, and some
elements of the geometric sans.

It remains true to its roots, but has its own personality.

The weight distribution is almost monotone, although top and bottom
curves are slightly thin.

Counters of the b, g, p and q are rounded and optically adjusted. The
curved stem endings have a 10 degree angle. E and F have shorter
center arms. M is splashed.

Designer: Pablo Impallari

%prep
%setup -c %{fontname} -n %{fontname}
tar xjvf %{SOURCE1}

%build
# -- Nothing to do --

%install
mkdir -p  %{buildroot}%{_ttfontsdir}/
install -m 644 %{fontname}/*.ttf %{fontname}condensed/*.ttf \
  %{buildroot}%{_ttfontsdir}
dos2unix cabin/OFL.txt
chmod 644 cabin/OFL.txt

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%doc cabin/OFL.txt

%changelog
