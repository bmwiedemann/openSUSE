#
# spec file for package perl-Test-Modern
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Modern
Version:        0.013
Release:        0
%define cpan_name Test-Modern
Summary:        precision testing for modern perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Modern/
Source:         http://www.cpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Tiny) >= 0.030
BuildRequires:  perl(Import::Into) >= 1.002000
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Test::API) >= 0.004
BuildRequires:  perl(Test::Deep) >= 0.111
BuildRequires:  perl(Test::Fatal) >= 0.007
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(Try::Tiny) >= 0.15
#BuildRequires: perl(CPAN::Meta::Requirements)
#BuildRequires: perl(LWP::UserAgent)
#BuildRequires: perl(Moose)
#BuildRequires: perl(namespace::clean)
#BuildRequires: perl(Role::Tiny)
#BuildRequires: perl(Test::Modern)
Requires:       perl(Exporter::Tiny) >= 0.030
Requires:       perl(Import::Into) >= 1.002000
Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(Test::API) >= 0.004
Requires:       perl(Test::Deep) >= 0.111
Requires:       perl(Test::Fatal) >= 0.007
Requires:       perl(Test::More) >= 0.96
Requires:       perl(Test::Warnings) >= 0.009
Requires:       perl(Try::Tiny) >= 0.15
Recommends:     perl(Test::LongString) >= 0.15

Provides:       perl(Test::Modern)

%{perl_requires}

%description
Test::Modern provides the best features of the Test::More manpage, the
Test::Fatal manpage, the Test::Warnings manpage, the Test::API manpage, the
Test::LongString manpage, and the Test::Deep manpage, as well as ideas from
the Test::Requires manpage, the Test::DescribeMe manpage, the Test::Moose
manpage, and the Test::CleanNamespaces manpage.

Test::Modern also automatically imposes the strict manpage and the warnings
manpage on your script, and loads the IO::File manpage. (Much of the same
stuff the Modern::Perl manpage does.)

Although Test::Modern is a modern testing framework, it should run fine on
pre-modern versions of Perl. It should be easy to install on Perl 5.8.9 and
above; and if you can persuade its dependencies to install (not necessarily
easy!), should be OK on anything back to Perl 5.6.1.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS doap.ttl LICENSE README

%changelog
