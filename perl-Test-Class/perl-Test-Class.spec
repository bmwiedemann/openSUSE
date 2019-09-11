#
# spec file for package perl-Test-Class
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


Name:           perl-Test-Class
Version:        0.50
Release:        0
%define cpan_name Test-Class
Summary:        Easily create test classes in an xUnit/JUnit style
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Class/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MRO::Compat) >= 0.11
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::Builder) >= 0.78
BuildRequires:  perl(Test::Exception) >= 0.250000
BuildRequires:  perl(Test::More) >= 0.78
BuildRequires:  perl(Test::Simple) >= 0.78
BuildRequires:  perl(Try::Tiny)
Requires:       perl(MRO::Compat) >= 0.11
Requires:       perl(Module::Runtime)
Requires:       perl(Test::Builder) >= 0.78
Requires:       perl(Test::Simple) >= 0.78
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
Test::Class provides a simple way of creating classes and objects to test
your code in an xUnit style.

Built using the Test::Builder manpage, it was designed to work with other
Test::Builder based modules (the Test::More manpage, the Test::Differences
manpage, the Test::Exception manpage, etc.).

_Note:_ This module will make more sense, if you are already familiar with
the "standard" mechanisms for testing perl code. Those unfamiliar with the
Test::Harness manpage, the Test::Simple manpage, the Test::More manpage and
friends should go take a look at them now. the Test::Tutorial manpage is a
good starting point.

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
%doc Changes README

%changelog
