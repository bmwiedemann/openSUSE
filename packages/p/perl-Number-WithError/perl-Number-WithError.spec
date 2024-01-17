#
# spec file for package perl-Number-WithError
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Number-WithError
Version:        1.01
Release:        0
%define cpan_name Number-WithError
Summary:        Numbers with error propagation and scientific rounding
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Number-WithError/
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Number-WithError-1.01-no-dot-inc.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Params::Util) >= 0.10
BuildRequires:  perl(Test::LectroTest)
BuildRequires:  perl(prefork) >= 1.00
Requires:       perl(Params::Util) >= 0.10
Requires:       perl(prefork) >= 1.00
%{perl_requires}

%description
This class is a container class for numbers with a number of associated
symmetric and asymmetric errors. It overloads practically all common
arithmetic operations and trigonometric functions to propagate the errors.
It can do proper scientific rounding (as explained in more detail below in
the documentation of the 'significant_digit()' method).

You can use Math::BigFloat objects as the internal representation of
numbers in order to support arbitrary precision calculations.

Errors are propagated using Gaussian error propagation.

With a notable exception, the test suite covers way over ninety percent of
the code. The remaining holes are mostly difficult-to-test corner cases and
sanity tests. The comparison routines are the exception for which there
will be more extensive tests in a future release.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p1

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
%doc Changes README

%changelog
