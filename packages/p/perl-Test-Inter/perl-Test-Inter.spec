#
# spec file for package perl-Test-Inter
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Inter
Version:        1.09
Release:        0
%define cpan_name Test-Inter
Summary:        Framework for more readable interactive test scripts
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README
%license LICENSE

%changelog
