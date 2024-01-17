#
# spec file for package google-lekton-fonts
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


# Definitions
%define fontname lekton

Name:           google-lekton-fonts
Version:        22
Release:        0
Summary:        Monospaced Typewriter Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.lekton.info/
Source0:        %{fontname}-%{version}.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Lekton has been designed at ISIA Urbino, Italy, and is inspired by some of the typefaces used on the Olivetti typewriters.

It was designed by: Paolo Mazzetti, Luciano Perondi, Raffaele Flaùto, Elena Papassissa, Emilio Macchia, Michela Povoleri, Tobias Seemiller, Riccardo Lorusso, Sabrina Campagna, Elisa Ansuini, Mariangela Di Pinto, Antonio Cavedoni, Marco Comastri, Luna Castroni, Stefano Faoro, Daniele Capo, and Jan Henrik Arnold.

%prep
%setup -n %{fontname}-%{version}
# Fixed line endings
find . -name \*.txt -print0 | xargs -0 dos2unix

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_ttfontsdir}
cp *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root, root)
%doc METADATA FONTLOG.txt OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
