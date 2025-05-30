#
# spec file for package perl-Test-Perl-Critic
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


%define cpan_name Test-Perl-Critic
Name:           perl-Test-Perl-Critic
Version:        1.40.0
Release:        0
# 1.04 -> normalize -> 1.40.0
%define cpan_version 1.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Use Perl::Critic in test programs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MCE) >= 1.827
BuildRequires:  perl(Module::Build) >= 0.4
BuildRequires:  perl(Perl::Critic) >= 1.105
BuildRequires:  perl(Perl::Critic::Utils) >= 1.105
BuildRequires:  perl(Perl::Critic::Violation) >= 1.105
BuildRequires:  perl(Test::Builder) >= 0.88
Requires:       perl(MCE) >= 1.827
Requires:       perl(Perl::Critic) >= 1.105
Requires:       perl(Perl::Critic::Utils) >= 1.105
Requires:       perl(Perl::Critic::Violation) >= 1.105
Requires:       perl(Test::Builder) >= 0.88
Provides:       perl(Test::Perl::Critic) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Test::Perl::Critic wraps the Perl::Critic engine in a convenient subroutine
suitable for test programs written using the Test::More framework. This
makes it easy to integrate coding-standards enforcement into the build
process. For ultimate convenience (at the expense of some flexibility), see
the criticism pragma.

If you have an large existing code base, you might prefer to use
Test::Perl::Critic::Progressive, which allows you to clean your code
incrementally instead of all at once..

If you'd like to try Perl::Critic without installing anything, there is a
web-service available at http://perlcritic.com. The web-service does not
support all the configuration features that are available in the native
Perl::Critic API, but it should give you a good idea of what Perl::Critic
can do.

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
%doc Changes README
%license LICENSE

%changelog
