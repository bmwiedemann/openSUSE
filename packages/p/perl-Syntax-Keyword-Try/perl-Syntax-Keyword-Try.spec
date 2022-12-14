#
# spec file for package perl-Syntax-Keyword-Try
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Syntax-Keyword-Try
Name:           perl-Syntax-Keyword-Try
Version:        0.28
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Try/catch/finally syntax for perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XS::Parse::Keyword) >= 0.06
BuildRequires:  perl(XS::Parse::Keyword::Builder) >= 0.06
Requires:       perl(XS::Parse::Keyword) >= 0.06
%{perl_requires}

%description
This module provides a syntax plugin that implements exception-handling
semantics in a form familiar to users of other languages, being built on a
block labeled with the 'try' keyword, followed by at least one of a 'catch'
or 'finally' block.

As well as providing a handy syntax for this useful behaviour, this module
also serves to contain a number of code examples for how to implement
parser plugins and manipulate optrees to provide new syntax and behaviours
for perl code.

Syntax similar to this module has now been added to core perl, starting at
version 5.34.0. If you are writing new code, it is suggested that you
instead use the Feature::Compat::Try module instead, as that will enable
the core feature on those supported perl versions, falling back to
'Syntax::Keyword::Try' on older perls.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
