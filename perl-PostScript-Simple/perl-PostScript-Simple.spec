#
# spec file for package perl-PostScript-Simple
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-PostScript-Simple
Version:        0.09
Release:        0
#Upstream: CHECK(GPL-1.0+ or Artistic-1.0)
%define cpan_name PostScript-Simple
Summary:        Produce PostScript files from Perl
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/PostScript-Simple/
Source0:        http://www.cpan.org/authors/id/M/MC/MCNEWTON/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
PostScript::Simple allows you to have a simple method of writing PostScript
files from Perl. It has graphics primitives that allow lines, curves,
circles, polygons and boxes to be drawn. Text can be added to the page
using standard PostScript fonts.

The images can be single page EPS files, or multipage PostScript files. The
image size can be set by using a recognised paper size ("'A4'", for
example) or by giving dimensions. The units used can be specified ("'mm'"
or "'in'", etc) and are the same as those used in TeX. The default unit is
a bp, or a PostScript point, unlike TeX.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README TODO

%changelog
