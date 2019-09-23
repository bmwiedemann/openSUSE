#
# spec file for package google-allerta-fonts
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


%define fontname allerta

Name:           google-allerta-fonts
Version:        1.0
Release:        0
Summary:        Easily Readable Sans Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://pixelspread.com/allerta/
Source0:        %{fontname}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Allerta is an open source typeface designed for use in
signage. Allerta was designed to be easily and quickly
read from a distance. Each letter exploits the most
unique aspects of that individual letter so that each
character can be easily distinguished from any other.

Allerta has been released as an open source project so
that those countries, communities, and/or organizations
without a proper signage system may have a way of quickly
designing and implementing one. While Allerta is complete
with a large character set, because it is open source,
modification and expansion is encouraged.

For the more urgent of circumstances, Allerta Stencil
and an accompanying kit have been designed so that signage
can be created with nothing more than the kit of letters, a
can of spray paint, and the nearest available substrate.
Although the stencil kit may allude the finer points of
typographic spacing, it is intended to serve the most basic
purpose of signage: guiding people towards their destination
or towards assistance.

The name Allerta is derived from the origins of the word
alert (adj. swift, v. to advise or warn). The Italian origin
all'erta literally means on the lookout.

Designer: Matt McInerney


%prep
%setup -T -c %{name} -n %{name}
unzip -j $RPM_SOURCE_DIR/allerta.zip
chmod 644 *.otf *.ttf
mv allerta_pdf.pdf allerta.pdf
find . -type f -name \*.txt -print0 | xargs -0 dos2unix

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 644 *.otf *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.pdf
%doc Open*.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%changelog
