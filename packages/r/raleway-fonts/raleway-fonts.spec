#
# spec file for package raleway-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           raleway-fonts
Version:        3.0
Release:        0
Summary:        Elegant sans-serif Typeface Family
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.impallari.com/projects/overview/matt-mcinerneys-raleway-family
Source0:        update-100-source.zip
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  unzip
# The LOMT collection only has the original single thickness and can thus be
# considered a subset that can be replaced without worry.
Obsoletes:      lomt-raleway-fonts
Provides:       lomt-raleway-fonts

%description
Raleway is an elegant sans-serif typeface, designed by Matt McInerney, 
initially in a single Thin weight. It is a display face that features 
both old style and lining numerals, standard and discretionary ligatures, 
a pretty complete set of diacritics, as well as stylistic alternates 
inspired by more geometric sans-serif typefaces than it's neo-grotesque 
inspired default character set.

The Impallari–Fuenzalida derivative extends the Raleway font family
into a full set of 9 weights with true italics and expanded character
set support for all 104 Latin languages.

%prep
%setup -q -n raleway-family-v%{version}

%build
chmod 644 FONTLOG.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc OFL.txt FONTLOG.txt
%{_ttfontsdir}

%changelog
