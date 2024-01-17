#
# spec file for package perl-Pod-Elemental
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Pod-Elemental
Name:           perl-Pod-Elemental
Version:        0.103006
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Work with nestable Pod elements
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Mixin::Linewise::Readers)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role) >= 0.90
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Pod::Eventual::Simple) >= 0.004
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(String::Truncate)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::ForMethods)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Class::Load)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Mixin::Linewise::Readers)
Requires:       perl(Moose)
Requires:       perl(Moose::Role) >= 0.90
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(Pod::Eventual::Simple) >= 0.004
Requires:       perl(String::RewritePrefix)
Requires:       perl(String::Truncate)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::ForMethods)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
Pod::Elemental is a system for treating a Pod (plain old
documentation|perlpod) documents as trees of elements. This model may be
familiar from many other document systems, especially the HTML DOM.
Pod::Elemental's document object model is much less sophisticated than the
HTML DOM, but still makes a lot of document transformations easy.

In general, you'll want to read in a Pod document and then perform a number
of prepackaged transformations on it. The most common of these will be the
Pod5 transformation|Pod::Elemental::Transformer::Pod5, which assumes that
the basic meaning of Pod commands described in the Perl 5 documentation
hold: '=begin', '=end', and '=for' commands mark regions of the document,
leading whitespace marks a verbatim paragraph, and so on. The Pod5
transformer also eliminates the need to track elements representing
vertical whitespace.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
