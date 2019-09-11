#
# spec file for package perl-Perl-Critic-Freenode
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


Name:           perl-Perl-Critic-Freenode
Version:        0.029
Release:        0
%define cpan_name Perl-Critic-Freenode
Summary:        Perl::Critic policies inspired by #perl on
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(PPI) >= 1.254
BuildRequires:  perl(Path::Tiny) >= 0.101
BuildRequires:  perl(Perl::Critic) >= 1.126
BuildRequires:  perl(Perl::Critic::Policy::Objects::ProhibitIndirectSyntax) >= 1.126
BuildRequires:  perl(Perl::Critic::Policy::Subroutines::ProhibitAmpersandSigils) >= 1.126
BuildRequires:  perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitArrayAssignAref) >= 90
BuildRequires:  perl(Perl::Critic::Policy::Variables::ProhibitConditionalDeclarations) >= 1.126
BuildRequires:  perl(Perl::Critic::Policy::Variables::ProhibitLoopOnHash) >= 0.005
BuildRequires:  perl(Perl::Critic::Policy::Variables::RequireLexicalLoopIterators) >= 1.126
BuildRequires:  perl(parent)
BuildRequires:  perl(version)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(PPI) >= 1.254
Requires:       perl(Path::Tiny) >= 0.101
Requires:       perl(Perl::Critic) >= 1.126
Requires:       perl(Perl::Critic::Policy::Objects::ProhibitIndirectSyntax) >= 1.126
Requires:       perl(Perl::Critic::Policy::Subroutines::ProhibitAmpersandSigils) >= 1.126
Requires:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitArrayAssignAref) >= 90
Requires:       perl(Perl::Critic::Policy::Variables::ProhibitConditionalDeclarations) >= 1.126
Requires:       perl(Perl::Critic::Policy::Variables::ProhibitLoopOnHash) >= 0.005
Requires:       perl(Perl::Critic::Policy::Variables::RequireLexicalLoopIterators) >= 1.126
Requires:       perl(parent)
Requires:       perl(version)
%{perl_requires}

%description
A set of Perl::Critic policies to enforce the practices generally
recommended by the denizens of #perl on at https://freenode.net/. Because
this policy "theme" is designed to be used with zero configuration on the
command line, some duplication will occur if it is used in combination with
core Perl::Critic policies.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
