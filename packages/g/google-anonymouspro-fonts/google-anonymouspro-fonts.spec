#
# spec file for package google-anonymouspro-fonts
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


%define fontname  anonymouspro

Name:           google-anonymouspro-fonts
Version:        1.002
Release:        0
Summary:        A Free Monospace Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.ms-studio.com/FontSales/anonymouspro.html
Source0:        %{fontname}.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Anonymous Pro is a family of four fixed-width fonts designed especially
with coding in mind. Characters that could be mistaken for one another
(O, 0, I, l, 1, etc.) have distinct shapes to make them easier to tell
apart in the context of source code.

Anonymous Pro also features an international, Unicode-based character set,
with support for most Western and European Latin-based languages, Greek,
and Cyrillic. It also includes special "box drawing" characters for those
who need them.

Designer: Mark Simonson

%prep
%setup -n %{fontname}
chmod 644 *.ttf

%build
# -- Nothing to do ---

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}
dos2unix OFL.txt

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc README.txt FONTLOG.txt OFL.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%changelog
