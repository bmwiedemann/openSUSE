#
# spec file for package perl-UNIVERSAL-require
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name UNIVERSAL-require
Name:           perl-UNIVERSAL-require
Version:        0.19
Release:        0
Summary:        Require() modules from a variable [deprecated]
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Before using this module, you should look at the alternatives, some of
which are listed in SEE ALSO below.

This module provides a safe mechanism for loading a module at runtime, when
you have the name of the module in a variable.

If you've ever had to do this...

    eval "require $module";

to get around the bareword caveats on require(), this module is for you. It
creates a universal require() class method that will work with every Perl
module and its secure. So instead of doing some arcane eval() work, you can
do this:

    $module->require;

It doesn't save you much typing, but it'll make a lot more sense to someone
who's not a ninth level Perl acolyte.

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

%changelog
