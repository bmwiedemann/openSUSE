#
# spec file for package perl-Perl-Critic-Pulp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Perl-Critic-Pulp
Name:           perl-Perl-Critic-Pulp
Version:        100.0.0
Release:        0
# 100 -> normalize -> 100.0.0
%define cpan_version 100
#Upstream: GPL-1.0-or-later
License:        GPL-3.0-or-later
Summary:        Some add-on policies for Perl::Critic
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
Patch0:         avoid-wrong-provides.diff
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::String) >= 1.20
BuildRequires:  perl(List::MoreUtils) >= 0.240
BuildRequires:  perl(PPI) >= 1.220
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Perl::Critic) >= 1.84
BuildRequires:  perl(Perl::Critic::Policy) >= 1.84
BuildRequires:  perl(Perl::Critic::Utils) >= 1.100
BuildRequires:  perl(Perl::Critic::Utils::PPI)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::MinimumVersion) >= 50
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(version)
Requires:       perl(IO::String) >= 1.20
Requires:       perl(List::MoreUtils) >= 0.240
Requires:       perl(PPI) >= 1.220
Requires:       perl(PPI::Document)
Requires:       perl(PPI::Dumper)
Requires:       perl(Perl::Critic) >= 1.84
Requires:       perl(Perl::Critic::Policy) >= 1.84
Requires:       perl(Perl::Critic::Utils) >= 1.100
Requires:       perl(Perl::Critic::Utils::PPI)
Requires:       perl(Perl::Critic::Violation)
Requires:       perl(Pod::Escapes)
Requires:       perl(Pod::MinimumVersion) >= 50
Requires:       perl(Pod::Parser)
Requires:       perl(version)
Provides:       perl(Perl::Critic::PodParser::ProhibitVerbatimMarkup)
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitFatCommaNewline) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitIfIfSameLine) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireFinalSemicolon) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireTrailingCommaAtNewline) = %{version}
Provides:       perl(Perl::Critic::Policy::Compatibility::ConstantLeadingUnderscore) = %{version}
Provides:       perl(Perl::Critic::Policy::Compatibility::ConstantPragmaHash) = %{version}
Provides:       perl(Perl::Critic::Policy::Compatibility::Gtk2Constants) = %{version}
Provides:       perl(Perl::Critic::Policy::Compatibility::PerlMinimumVersionAndWhy) = %{version}
Provides:       perl(Perl::Critic::Policy::Compatibility::PodMinimumVersion) = %{version}
Provides:       perl(Perl::Critic::Policy::Compatibility::ProhibitUnixDevNull) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitAdjacentLinks) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitAdjacentLinks::Parser)
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitBadAproposMarkup) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitDuplicateHeadings) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitDuplicateSeeAlso) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitLinkToSelf) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitParagraphEndComma) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitParagraphTwoDots) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitUnbalancedParens) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::ProhibitVerbatimMarkup) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::RequireEndBeforeLastPod) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::RequireFilenameMarkup) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::RequireFinalCut) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::RequireLinkedURLs) = %{version}
Provides:       perl(Perl::Critic::Policy::Miscellanea::TextDomainPlaceholders) = %{version}
Provides:       perl(Perl::Critic::Policy::Miscellanea::TextDomainUnused) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitModuleShebang) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitPOSIXimport) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitUseQuotedVersion) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ConstantBeforeLt) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::NotWithCompare) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitArrayAssignAref) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitBarewordDoubleColon) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitDuplicateHashKeys) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitEmptyCommas) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitFiletest_f) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitNullStatements) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitUnknownBackslash) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireNumericVersion) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::UnexpandedSpecialLiteral) = %{version}
Provides:       perl(Perl::Critic::Pulp) = %{version}
Provides:       perl(Perl::Critic::Pulp::PodMinimumVersionViolation)
Provides:       perl(Perl::Critic::Pulp::PodParser) = %{version}
Provides:       perl(Perl::Critic::Pulp::PodParser::ProhibitBadAproposMarkup)
Provides:       perl(Perl::Critic::Pulp::PodParser::ProhibitDuplicateHeadings)
Provides:       perl(Perl::Critic::Pulp::PodParser::ProhibitDuplicateSeeAlso)
Provides:       perl(Perl::Critic::Pulp::PodParser::ProhibitLinkToSelf)
Provides:       perl(Perl::Critic::Pulp::PodParser::ProhibitParagraphEndComma)
Provides:       perl(Perl::Critic::Pulp::PodParser::ProhibitParagraphTwoDots)
Provides:       perl(Perl::Critic::Pulp::PodParser::ProhibitUnbalancedParens)
Provides:       perl(Perl::Critic::Pulp::PodParser::RequireFilenameMarkup)
Provides:       perl(Perl::Critic::Pulp::PodParser::RequireFinalCut)
Provides:       perl(Perl::Critic::Pulp::PodParser::RequireLinkedURLs)
Provides:       perl(Perl::Critic::Pulp::ProhibitDuplicateHashKeys::Qword)
Provides:       perl(Perl::Critic::Pulp::Utils) = %{version}
Provides:       perl(Perl::MinimumVersion)
%undefine       __perllib_provides
%{perl_requires}

%description
This is a collection of add-on policies for 'Perl::Critic'. They're under a
"pulp" theme plus other themes according to their purpose (see
Perl::Critic/POLICY THEMES).

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license COPYING

%changelog
