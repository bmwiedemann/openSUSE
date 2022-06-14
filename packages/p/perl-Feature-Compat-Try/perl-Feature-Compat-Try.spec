#
# spec file for package perl-Feature-Compat-Try
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


%define cpan_name Feature-Compat-Try
Name:           perl-Feature-Compat-Try
Version:        0.05
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Make try/catch syntax available
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Syntax::Keyword::Try) >= 0.27
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Syntax::Keyword::Try) >= 0.27
%{perl_requires}

%description
This module makes syntax support for 'try/catch' control flow easily
available.

Perl added such syntax at version 5.34.0, and extended it to support
optional 'finally' blocks at 5.35.9, which is enabled by

   use feature 'try';

On that version of perl or later, this module simply enables the core
feature equivalent to using it directly. On such perls, this module will
install with no non-core dependencies, and requires no C compiler.

On older versions of perl before such syntax is available, it is currently
provided instead using the Syntax::Keyword::Try module, imported with a
special set of options to configure it to recognise exactly and only the
same syntax as the core perl feature, thus ensuring that any code using it
will still continue to function on that newer perl.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
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
