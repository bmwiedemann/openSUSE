#
# spec file for package perl-TryCatch
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-TryCatch
Version:        1.003002
Release:        0
%define cpan_name TryCatch
Summary:        first class try catch semantics for Perl, without source filters.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/TryCatch/
Source:         http://www.cpan.org/authors/id/A/AS/ASH/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.18
BuildRequires:  perl(B::Hooks::OP::PPAddr) >= 0.03
BuildRequires:  perl(Devel::Declare) >= 0.005007
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(Parse::Method::Signatures) >= 1.003012
BuildRequires:  perl(Scope::Upper) >= 0.06
BuildRequires:  perl(Sub::Exporter) >= 0.979
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Variable::Magic) >= 0.28
BuildRequires:  perl(namespace::clean) >= 0.20
#BuildRequires: perl(Class::Throwable)
#BuildRequires: perl(CPANPLUS::Backend)
#BuildRequires: perl(Devel::Declare::Context::Simple)
#BuildRequires: perl(Devel::PartialDump)
#BuildRequires: perl(Exception::Class)
#BuildRequires: perl(File::Copy::Recursive)
#BuildRequires: perl(inc::Module::Install) >= 0.79
#BuildRequires: perl(JSON)
#BuildRequires: perl(LWP::Simple)
#BuildRequires: perl(Module::AutoInstall)
#BuildRequires: perl(Module::Build)
#BuildRequires: perl(Module::Install::Base)
#BuildRequires: perl(Moose::Util::TypeConstraints)
#BuildRequires: perl(MooseX::Types::Structured)
#BuildRequires: perl(NoType)
#BuildRequires: perl(NoVarName)
#BuildRequires: perl(Parse::CPAN::Meta)
#BuildRequires: perl(Path::Class)
#BuildRequires: perl(TryCatch)
#BuildRequires: perl(TryCatchTest)
#BuildRequires: perl(XML::SAX::Base)
#BuildRequires: perl(XML::SAX::Expat)
#BuildRequires: perl(YAML::Tiny)
Requires:       perl(B::Hooks::EndOfScope) >= 0.12
Requires:       perl(B::Hooks::OP::Check) >= 0.18
Requires:       perl(B::Hooks::OP::PPAddr) >= 0.03
Requires:       perl(Devel::Declare) >= 0.005007
Requires:       perl(Moose)
Requires:       perl(MooseX::Types)
Requires:       perl(Parse::Method::Signatures) >= 1.003012
Requires:       perl(Scope::Upper) >= 0.06
Requires:       perl(Sub::Exporter) >= 0.979
Requires:       perl(Variable::Magic) >= 0.28
Requires:       perl(namespace::clean) >= 0.20
%{perl_requires}

%description
This module aims to provide a nicer syntax and method to catch errors in
Perl, similar to what is found in other languages (such as Java, Python or
C++). The standard method of using 'eval {}; if ($@) {}' is often prone to
subtle bugs, primarily that its far too easy to stomp on the error in error
handlers. And also eval/if isn't the nicest idiom.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
PERL5LIB=. %{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes MYMETA.json MYMETA.yml README

%changelog
