#
# spec file for package perl-Test-Assert
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-Test-Assert
Version:        0.0504
Release:        0
%define cpan_name Test-Assert
Summary:        Assertion methods for those who like JUnit.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Assert/
Source:         http://www.cpan.org/authors/id/D/DE/DEXTER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Exception::Base) >= 0.21
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Symbol::Util) >= 0.0202
BuildRequires:  perl(Test::Unit::Lite) >= 0.11
BuildRequires:  perl(constant::boolean) >= 0.02
BuildRequires:  perl(parent)
#BuildRequires: perl(Exception::Assertion)
#BuildRequires: perl(File::Slurp)
#BuildRequires: perl(Readonly)
#BuildRequires: perl(Test::Assert)
#BuildRequires: perl(Test::CheckChanges)
#BuildRequires: perl(Test::Differences)
#BuildRequires: perl(Test::Distribution)
#BuildRequires: perl(Test::Kwalitee)
#BuildRequires: perl(Test::Perl::Critic)
#BuildRequires: perl(Test::Signature)
#BuildRequires: perl(Test::Spelling)
#BuildRequires: perl(Test::Unit::TestCase)
Requires:       perl(constant::boolean) >= 0.02
Requires:       perl(Exception::Base) >= 0.21
Requires:       perl(Symbol::Util) >= 0.0202
%{perl_requires}

%description
This class provides a set of assertion methods useful for writing tests.
The API is based on JUnit4 and the Test::Unit::Lite manpage and the methods
die on failure.

These assertion methods might be not useful for common the Test::Builder
manpage-based (the Test::Simple manpage, the Test::More manpage, etc.) test
units.

The assertion methods can be used in class which is derived from
'Test::Assert' or used as standard Perl functions after importing them into
user's namespace.

'Test::Assert' can also wrap standard the Test::Simple manpage, the
Test::More manpage or other the Test::Builder manpage-based tests.

The assertions can be also used for run-time checking.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes eg LICENSE README xt

%changelog
