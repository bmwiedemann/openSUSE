#
# spec file for package google-cabin-fonts
#
# Copyright (c) 2021 SUSE LLC
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


Name:           google-cabin-fonts
Version:        3.001+git1595464381.70efa8c
Release:        0
Summary:        Humanist Sans Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/impallari/Cabin
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Cabin font family is a humanist sans with 4 weights and true italics,
inspired by Edward Johnston’s and Eric Gill’s typefaces, with a touch of
modernism. Cabin incorporates modern proportions, optical adjustments, and some
elements of the geometric sans. It remains true to its roots, but has its own
personality.

The weight distribution is almost monotone, although top and bottom curves are
slightly thin. Counters of the b, g, p and q are rounded and optically
adjusted. The curved stem endings have a 10 degree angle. E and F have shorter
center arms. M is splashed.

Designer: Pablo Impallari

%prep
%autosetup
chmod 0644 {FONTLOG,OFL}.txt
dos2unix README.md

%build
# -- Nothing to do --

%install
install -dm0755 %{buildroot}%{_ttfontsdir}/
install -m0644 fonts/OTF/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%doc {README,TRADEMARKS}.md {FONTLOG,AUTHORS,CONTRIBUTORS}.txt
%license OFL.txt

%changelog
