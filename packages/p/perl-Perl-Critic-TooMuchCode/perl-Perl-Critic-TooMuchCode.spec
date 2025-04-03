#
# spec file for package perl-Perl-Critic-TooMuchCode
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


%define cpan_name Perl-Critic-TooMuchCode
Name:           perl-Perl-Critic-TooMuchCode
Version:        0.190.0
Release:        0
# 0.19 -> normalize -> 0.190.0
%define cpan_version 0.19
License:        MIT
Summary:        Perlcritic add-ons that generally check for dead code
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.50
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.39.0
BuildRequires:  perl(PPIx::QuoteLike)
BuildRequires:  perl(PPIx::Utils) >= 0.2.0
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Scalar::Util) >= 1.50
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(List::Util) >= 1.50
Requires:       perl(PPIx::QuoteLike)
Requires:       perl(PPIx::Utils) >= 0.2.0
Requires:       perl(Perl::Critic)
Requires:       perl(Scalar::Util) >= 1.50
Requires:       perl(version) >= 0.77
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitDuplicateLiteral)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitDuplicateSub)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitExcessiveColons) = 0.10.0
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitExtraStricture)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitLargeBlock)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitLargeTryBlock)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitUnnecessaryScalarKeyword)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitUnnecessaryUTF8Pragma)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitUnusedConstant)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitUnusedImport)
Provides:       perl(Perl::Critic::Policy::TooMuchCode::ProhibitUnusedInclude)
Provides:       perl(Perl::Critic::TooMuchCode) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This add-on for Perl::Critic is aiming for identifying trivial dead code.
Either the ones that has no use, or the one that produce no effect. Having
dead code floating around causes maintenance burden. Some might prefer not
to generate them in the first place.

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
