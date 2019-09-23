#
# spec file for package gdouros-maya-fonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gdouros-maya-fonts
Version:        4.17
Release:        0
Summary:        Font with Basic Maya Glyphs
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://greekfonts.teilar.gr
# Download source:
# http://users.teilar.gr/~g1951d/Maya.zip
Source0:        Maya-%{version}.zip
Source1:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      maya-fonts < 4.14
Provides:       maya-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Maya covers the glyphs in J. Eric S. Thompson’s “A Catalog of Maya
Hieroglyphs”, as well as some extra glyphs for days, months and numbers.
This is a work-font that may be of some scholarly use; it is not a proposal
of any kind. There are no plans to improve or expand it.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
install -m 0644 %{SOURCE1} .

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE Maya.pdf
%{_ttfontsdir}

%changelog
