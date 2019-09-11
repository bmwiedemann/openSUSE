#
# spec file for package google-nobile-fonts
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


%define fontname nobile

Name:           google-nobile-fonts
Version:        1.0.38
Release:        0
Summary:        Sans Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://code.google.com/webfonts/family?family=Nobile
Source0:        %{fontname}-%{version}.tar.bz2
Source1:        OFL.txt
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
"Nobile" is designed to work with the technologies of digital
screens and handheld devices without losing the distinctive look
more usually found in fonts designed for printing. Going back to
William Morris's baseline "Have nothing in your house that you do
not know to be useful, or believe to be beautiful", the aim was to
design a font that could function well, have good legibility on
screen yet also be good loooking, not only at larger display sizes
but also right down to small text sizes.

Designer: Vernon Adams

%prep
%setup -n %{fontname}-%{version}

%build
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*
%doc OFL.txt

%changelog
