#
# spec file for package perl-Font-FreeType
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Font-FreeType
Version:        0.12
Release:        0
%define cpan_name Font-FreeType
Summary:        Read Font Files and Render Glyphs From Perl Using Freetype2
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Font-FreeType/
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMOL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Test::Warnings)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  freetype2-devel
# MANUAL END

%description
This module allows Perl programs to conveniently read information from font
files. All the font access is done through the FreeType2 library, which
supports many formats. It can render images of characters with high-quality
hinting and antialiasing, extract metrics information, and extract the
outlines of characters in scalable formats like TrueType.

Warning: this module is currently in 'beta' stage. It'll be another release
or two before it stabilizes. The API may change in ways that break programs
based on it, but I don't think it will change much. Some of the values
returned may be wrong, or not scaled correctly. See the _TODO_ file to get
a handle on how far along this work is. Contributions welcome, particularly
if you know more than I do (which isn't much) about fonts and the FreeType2
library.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples TODO

%changelog
