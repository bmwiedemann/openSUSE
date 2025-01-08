#
# spec file for package perl-Perl-Critic
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Perl-Critic
Name:           perl-Perl-Critic
Version:        1.156.0
Release:        0
# 1.156 -> normalize -> 1.156.0
%define cpan_version 1.156
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Critique Perl source code for best-practices
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Keywords) >= 1.23
BuildRequires:  perl(Config::Tiny) >= 2
BuildRequires:  perl(Exception::Class) >= 1.23
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(File::Which)
BuildRequires:  perl(List::SomeUtils) >= 0.55
BuildRequires:  perl(Module::Build) >= 0.4204
BuildRequires:  perl(Module::Pluggable) >= 3.1
BuildRequires:  perl(PPI) >= 1.277
BuildRequires:  perl(PPI::Document) >= 1.277
BuildRequires:  perl(PPI::Document::File) >= 1.277
BuildRequires:  perl(PPI::Node) >= 1.277
BuildRequires:  perl(PPI::Token::Quote::Single) >= 1.277
BuildRequires:  perl(PPI::Token::Whitespace) >= 1.277
BuildRequires:  perl(PPIx::QuoteLike)
BuildRequires:  perl(PPIx::Regexp) >= 0.027
BuildRequires:  perl(PPIx::Regexp::Util) >= 0.068
BuildRequires:  perl(PPIx::Utils::Traversal) >= 0.003
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(Pod::Spell) >= 1
BuildRequires:  perl(Readonly) >= 2
BuildRequires:  perl(String::Format) >= 1.18
BuildRequires:  perl(Term::ANSIColor) >= 2.02
BuildRequires:  perl(Test::Builder) >= 0.92
BuildRequires:  perl(parent)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(B::Keywords) >= 1.23
Requires:       perl(Config::Tiny) >= 2
Requires:       perl(Exception::Class) >= 1.23
Requires:       perl(Exporter) >= 5.63
Requires:       perl(File::Which)
Requires:       perl(List::SomeUtils) >= 0.55
Requires:       perl(Module::Pluggable) >= 3.1
Requires:       perl(PPI) >= 1.277
Requires:       perl(PPI::Document) >= 1.277
Requires:       perl(PPI::Document::File) >= 1.277
Requires:       perl(PPI::Node) >= 1.277
Requires:       perl(PPI::Token::Quote::Single) >= 1.277
Requires:       perl(PPI::Token::Whitespace) >= 1.277
Requires:       perl(PPIx::QuoteLike)
Requires:       perl(PPIx::Regexp) >= 0.027
Requires:       perl(PPIx::Regexp::Util) >= 0.068
Requires:       perl(PPIx::Utils::Traversal) >= 0.003
Requires:       perl(Perl::Tidy)
Requires:       perl(Pod::PlainText)
Requires:       perl(Pod::Select)
Requires:       perl(Pod::Spell) >= 1
Requires:       perl(Readonly) >= 2
Requires:       perl(String::Format) >= 1.18
Requires:       perl(Term::ANSIColor) >= 2.02
Requires:       perl(Test::Builder) >= 0.92
Requires:       perl(parent)
Requires:       perl(version) >= 0.77
Provides:       perl(Perl::Critic) = %{version}
Provides:       perl(Perl::Critic::Annotation) = %{version}
Provides:       perl(Perl::Critic::Command) = %{version}
Provides:       perl(Perl::Critic::Config) = %{version}
Provides:       perl(Perl::Critic::Document) = %{version}
Provides:       perl(Perl::Critic::Exception) = %{version}
Provides:       perl(Perl::Critic::Exception::AggregateConfiguration) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Generic) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::NonExistentPolicy) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Option) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Global) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Global::ExtraParameter) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Global::ParameterValue) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Policy) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Policy::ExtraParameter) = %{version}
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Policy::ParameterValue) = %{version}
Provides:       perl(Perl::Critic::Exception::Fatal) = %{version}
Provides:       perl(Perl::Critic::Exception::Fatal::Generic) = %{version}
Provides:       perl(Perl::Critic::Exception::Fatal::Internal) = %{version}
Provides:       perl(Perl::Critic::Exception::Fatal::PolicyDefinition) = %{version}
Provides:       perl(Perl::Critic::Exception::IO) = %{version}
Provides:       perl(Perl::Critic::Exception::Parse) = %{version}
Provides:       perl(Perl::Critic::OptionsProcessor) = %{version}
Provides:       perl(Perl::Critic::Policy) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitBooleanGrep) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitComplexMappings) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitLvalueSubstr) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitReverseSortBlock) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitShiftRef) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitSleepViaSelect) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitStringyEval) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitStringySplit) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitUniversalCan) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitUniversalIsa) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitUselessTopic) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitVoidGrep) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitVoidMap) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireBlockGrep) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireBlockMap) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireGlobFunction) = %{version}
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireSimpleSortBlock) = %{version}
Provides:       perl(Perl::Critic::Policy::ClassHierarchies::ProhibitAutoloading) = %{version}
Provides:       perl(Perl::Critic::Policy::ClassHierarchies::ProhibitExplicitISA) = %{version}
Provides:       perl(Perl::Critic::Policy::ClassHierarchies::ProhibitOneArgBless) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitHardTabs) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitParensWithBuiltins) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitQuotedWordLists) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitTrailingWhitespace) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireConsistentNewlines) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireTidyCode) = %{version}
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireTrailingCommas) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitCStyleForLoops) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitCascadingIfElse) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitDeepNests) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitLabelsWithSpecialBlockNames) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitMutatingListFunctions) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitNegativeExpressionsInUnlessAndUntilConditions) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitPostfixControls) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitUnlessBlocks) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitUnreachableCode) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitUntilBlocks) = %{version}
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitYadaOperator) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::PodSpelling) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::RequirePackageMatchesPodName) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::RequirePodAtEnd) = %{version}
Provides:       perl(Perl::Critic::Policy::Documentation::RequirePodSections) = %{version}
Provides:       perl(Perl::Critic::Policy::ErrorHandling::RequireCarping) = %{version}
Provides:       perl(Perl::Critic::Policy::ErrorHandling::RequireCheckingReturnValueOfEval) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitBacktickOperators) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitBarewordDirHandles) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitBarewordFileHandles) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitExplicitStdin) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitInteractiveTest) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitJoinedReadline) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitOneArgSelect) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitReadlineInForLoop) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitTwoArgOpen) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireBracedFileHandleWithPrint) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireBriefOpen) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireCheckedClose) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireCheckedOpen) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireCheckedSyscalls) = %{version}
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireEncodingWithUTF8Layer) = %{version}
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitFormats) = %{version}
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitTies) = %{version}
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitUnrestrictedNoCritic) = %{version}
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitUselessNoCritic) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitAutomaticExportation) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitConditionalUseStatements) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitEvilModules) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitExcessMainComplexity) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitMultiplePackages) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::RequireBarewordIncludes) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::RequireEndWithOne) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::RequireExplicitPackage) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::RequireFilenameMatchesPackage) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::RequireNoMatchVarsWithUseEnglish) = %{version}
Provides:       perl(Perl::Critic::Policy::Modules::RequireVersionVar) = %{version}
Provides:       perl(Perl::Critic::Policy::NamingConventions::Capitalization) = %{version}
Provides:       perl(Perl::Critic::Policy::NamingConventions::ProhibitAmbiguousNames) = %{version}
Provides:       perl(Perl::Critic::Policy::Objects::ProhibitIndirectSyntax) = %{version}
Provides:       perl(Perl::Critic::Policy::References::ProhibitDoubleSigils) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitCaptureWithoutTest) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitComplexRegexes) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitEnumeratedClasses) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitEscapedMetacharacters) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitFixedStringMatches) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitSingleCharAlternation) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitUnusedCapture) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitUnusualDelimiters) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitUselessTopic) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireBracesForMultiline) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireDotMatchAnything) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireExtendedFormatting) = %{version}
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireLineBoundaryMatching) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitAmpersandSigils) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitBuiltinHomonyms) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitExcessComplexity) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitExplicitReturnUndef) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitManyArgs) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitNestedSubs) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitReturnSort) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitSubroutinePrototypes) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitUnusedPrivateSubroutines) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::ProtectPrivateSubs) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::RequireArgUnpacking) = %{version}
Provides:       perl(Perl::Critic::Policy::Subroutines::RequireFinalReturn) = %{version}
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::ProhibitNoStrict) = %{version}
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::ProhibitNoWarnings) = %{version}
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::ProhibitProlongedStrictureOverride) = %{version}
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::RequireTestLabels) = %{version}
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::RequireUseStrict) = %{version}
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::RequireUseWarnings) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitCommaSeparatedStatements) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitComplexVersion) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitConstantPragma) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitEmptyQuotes) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitEscapedCharacters) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitImplicitNewlines) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitInterpolationOfLiterals) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitLeadingZeros) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitLongChainsOfMethodCalls) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMagicNumbers) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMismatchedOperators) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMixedBooleanOperators) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitNoisyQuotes) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitQuotesAsQuotelikeOperatorDelimiters) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitSpecialLiteralHeredocTerminator) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitVersionStrings) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireConstantVersion) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireInterpolationOfMetachars) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireNumberSeparators) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireQuotedHeredocTerminator) = %{version}
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireUpperCaseHeredocTerminator) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitAugmentedAssignmentInDeclaration) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitConditionalDeclarations) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitEvilVariables) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitLocalVars) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitMatchVars) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitPackageVars) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitPerl4PackageNames) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitPunctuationVars) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitReusedNames) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitUnusedVariables) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::ProtectPrivateVars) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::RequireInitializationForLocalVars) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::RequireLexicalLoopIterators) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::RequireLocalizedPunctuationVars) = %{version}
Provides:       perl(Perl::Critic::Policy::Variables::RequireNegativeIndices) = %{version}
Provides:       perl(Perl::Critic::PolicyConfig) = %{version}
Provides:       perl(Perl::Critic::PolicyFactory) = %{version}
Provides:       perl(Perl::Critic::PolicyListing) = %{version}
Provides:       perl(Perl::Critic::PolicyParameter) = %{version}
Provides:       perl(Perl::Critic::PolicyParameter::Behavior) = %{version}
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::Boolean) = %{version}
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::Enumeration) = %{version}
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::Integer) = %{version}
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::String) = %{version}
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::StringList) = %{version}
Provides:       perl(Perl::Critic::ProfilePrototype) = %{version}
Provides:       perl(Perl::Critic::Statistics) = %{version}
Provides:       perl(Perl::Critic::TestUtils) = %{version}
Provides:       perl(Perl::Critic::Theme) = %{version}
Provides:       perl(Perl::Critic::ThemeListing) = %{version}
Provides:       perl(Perl::Critic::UserProfile) = %{version}
Provides:       perl(Perl::Critic::Utils) = %{version}
Provides:       perl(Perl::Critic::Utils::Constants) = %{version}
Provides:       perl(Perl::Critic::Utils::McCabe) = %{version}
Provides:       perl(Perl::Critic::Utils::POD) = %{version}
Provides:       perl(Perl::Critic::Utils::PPI) = %{version}
Provides:       perl(Perl::Critic::Utils::Perl) = %{version}
Provides:       perl(Perl::Critic::Violation) = %{version}
Provides:       perl(Test::Perl::Critic::Policy) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Perl::Critic is an extensible framework for creating and applying coding
standards to Perl source code. Essentially, it is a static source code
analysis engine. Perl::Critic is distributed with a number of
Perl::Critic::Policy modules that attempt to enforce various coding
guidelines. Most Policy modules are based on Damian Conway's book *Perl
Best Practices*. However, Perl::Critic is *not* limited to PBP and will
even support Policies that contradict Conway. You can enable, disable, and
customize those Polices through the Perl::Critic interface. You can also
create new Policy modules that suit your own tastes.

For a command-line interface to Perl::Critic, see the documentation for
perlcritic. If you want to integrate Perl::Critic with your build process,
Test::Perl::Critic provides an interface that is suitable for test
programs. Also, Test::Perl::Critic::Progressive is useful for gradually
applying coding standards to legacy code. For the ultimate convenience (at
the expense of some flexibility) see the criticism pragma.

If you'd like to try Perl::Critic without installing anything, there is a
web-service available at http://perlcritic.com. The web-service does not
yet support all the configuration features that are available in the native
Perl::Critic API, but it should give you a good idea of what it does.

Also, ActivePerl includes a very slick graphical interface to Perl-Critic
called 'perlcritic-gui'. You can get a free community edition of ActivePerl
from http://www.activestate.com.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md examples README README.md
%license LICENSE

%changelog
