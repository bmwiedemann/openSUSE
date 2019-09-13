#
# spec file for package perl-SVG
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


Name:           perl-SVG
Version:        2.84
Release:        0
%define cpan_name SVG
Summary:        Perl extension for generating Scalable Vector Graphics (SVG) documents
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/SVG/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
SVG is a 100% Perl module which generates a nested data structure
containing the DOM representation of an SVG (Scalable Vector Graphics)
image. Using SVG, you can generate SVG objects, embed other SVG instances
into it, access the DOM object, create and access javascript, and generate
SMIL animation content.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes examples README
%license LICENSE

%changelog
