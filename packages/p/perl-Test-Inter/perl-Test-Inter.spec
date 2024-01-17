#
# spec file for package perl-Test-Inter
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


%define cpan_name Test-Inter
Name:           perl-Test-Inter
Version:        1.10
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Framework for more readable interactive test scripts
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This is another framework for writing test scripts. Much of the syntax is
loosely inspired by Test::More, and Test::Inter has most of it's
functionality, but it is not a drop-in replacement.

Test::More (and other existing test frameworks) suffer from two weaknesses,
both of which have prevented me from ever using them:

   None offer the ability to access specific tests in
   a reasonably interactive fashion, primarily for
   debugging purposes

   None offer the ability to write the tests in
   whatever format would make the tests the most
   readable

The way I write and use test scripts, existing Test::* modules are not
nearly as useful as they could be.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README
%license LICENSE

%changelog
