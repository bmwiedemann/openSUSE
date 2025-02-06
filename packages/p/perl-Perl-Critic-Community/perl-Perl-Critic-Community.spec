#
# spec file for package perl-Perl-Critic-Community
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Perl-Critic-Community
Name:           perl-Perl-Critic-Community
Version:        1.0.4
Release:        0
# v1.0.4 -> normalize -> 1.0.4
%define cpan_version v1.0.4
License:        Artistic-2.0
Summary:        Community-inspired Perl::Critic policies
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(PPI) >= 1.254
BuildRequires:  perl(Path::Tiny) >= 0.101
BuildRequires:  perl(Perl::Critic) >= 1.126
BuildRequires:  perl(Perl::Critic::Policy::Objects::ProhibitIndirectSyntax) >= 1.126
BuildRequires:  perl(Perl::Critic::Policy::Plicease::ProhibitArrayAssignAref) >= 100.0.0
BuildRequires:  perl(Perl::Critic::Policy::Subroutines::ProhibitAmpersandSigils) >= 1.126
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
Requires:       perl(Perl::Critic::Policy::Plicease::ProhibitArrayAssignAref) >= 100.0.0
Requires:       perl(Perl::Critic::Policy::Subroutines::ProhibitAmpersandSigils) >= 1.126
Requires:       perl(Perl::Critic::Policy::Variables::ProhibitConditionalDeclarations) >= 1.126
Requires:       perl(Perl::Critic::Policy::Variables::ProhibitLoopOnHash) >= 0.005
Requires:       perl(Perl::Critic::Policy::Variables::RequireLexicalLoopIterators) >= 1.126
Requires:       perl(parent)
Requires:       perl(version)
%{perl_requires}
# MANUAL BEGIN
Obsoletes:      perl-Perl-Critic-Freenode
# MANUAL END

%description
A set of Perl::Critic policies to enforce the practices generally
recommended by subsets of the Perl community, particularly on IRC. Formerly
known as Perl::Critic::Freenode. Because this policy "theme" is designed to
be used with zero configuration on the command line, some duplication will
occur if it is used in combination with core Perl::Critic policies.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
