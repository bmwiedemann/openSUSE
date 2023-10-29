#
# spec file for package perl-Perl-Critic
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.152.0
Release:        0
%define cpan_version 1.152
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
BuildRequires:  perl(PPI) >= 1.277.0
BuildRequires:  perl(PPI::Document) >= 1.277.0
BuildRequires:  perl(PPI::Document::File) >= 1.277.0
BuildRequires:  perl(PPI::Node) >= 1.277.0
BuildRequires:  perl(PPI::Token::Quote::Single) >= 1.277.0
BuildRequires:  perl(PPI::Token::Whitespace) >= 1.277.0
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
Requires:       perl(PPI) >= 1.277.0
Requires:       perl(PPI::Document) >= 1.277.0
Requires:       perl(PPI::Document::File) >= 1.277.0
Requires:       perl(PPI::Node) >= 1.277.0
Requires:       perl(PPI::Token::Quote::Single) >= 1.277.0
Requires:       perl(PPI::Token::Whitespace) >= 1.277.0
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
Provides:       perl(Perl::Critic) = 1.152.0
Provides:       perl(Perl::Critic::Annotation) = 1.152.0
Provides:       perl(Perl::Critic::Command) = 1.152.0
Provides:       perl(Perl::Critic::Config) = 1.152.0
Provides:       perl(Perl::Critic::Document) = 1.152.0
Provides:       perl(Perl::Critic::Exception) = 1.152.0
Provides:       perl(Perl::Critic::Exception::AggregateConfiguration) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Generic) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::NonExistentPolicy) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Option) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Global) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Global::ExtraParameter) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Global::ParameterValue) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Policy) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Policy::ExtraParameter) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Configuration::Option::Policy::ParameterValue) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Fatal) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Fatal::Generic) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Fatal::Internal) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Fatal::PolicyDefinition) = 1.152.0
Provides:       perl(Perl::Critic::Exception::IO) = 1.152.0
Provides:       perl(Perl::Critic::Exception::Parse) = 1.152.0
Provides:       perl(Perl::Critic::OptionsProcessor) = 1.152.0
Provides:       perl(Perl::Critic::Policy) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitBooleanGrep) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitComplexMappings) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitLvalueSubstr) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitReverseSortBlock) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitShiftRef) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitSleepViaSelect) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitStringyEval) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitStringySplit) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitUniversalCan) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitUniversalIsa) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitUselessTopic) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitVoidGrep) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::ProhibitVoidMap) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireBlockGrep) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireBlockMap) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireGlobFunction) = 1.152.0
Provides:       perl(Perl::Critic::Policy::BuiltinFunctions::RequireSimpleSortBlock) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ClassHierarchies::ProhibitAutoloading) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ClassHierarchies::ProhibitExplicitISA) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ClassHierarchies::ProhibitOneArgBless) = 1.152.0
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitHardTabs) = 1.152.0
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitParensWithBuiltins) = 1.152.0
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitQuotedWordLists) = 1.152.0
Provides:       perl(Perl::Critic::Policy::CodeLayout::ProhibitTrailingWhitespace) = 1.152.0
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireConsistentNewlines) = 1.152.0
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireTidyCode) = 1.152.0
Provides:       perl(Perl::Critic::Policy::CodeLayout::RequireTrailingCommas) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitCStyleForLoops) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitCascadingIfElse) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitDeepNests) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitLabelsWithSpecialBlockNames) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitMutatingListFunctions) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitNegativeExpressionsInUnlessAndUntilConditions) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitPostfixControls) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitUnlessBlocks) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitUnreachableCode) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitUntilBlocks) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ControlStructures::ProhibitYadaOperator) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Documentation::PodSpelling) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Documentation::RequirePackageMatchesPodName) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Documentation::RequirePodAtEnd) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Documentation::RequirePodSections) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ErrorHandling::RequireCarping) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ErrorHandling::RequireCheckingReturnValueOfEval) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitBacktickOperators) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitBarewordDirHandles) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitBarewordFileHandles) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitExplicitStdin) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitInteractiveTest) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitJoinedReadline) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitOneArgSelect) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitReadlineInForLoop) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::ProhibitTwoArgOpen) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireBracedFileHandleWithPrint) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireBriefOpen) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireCheckedClose) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireCheckedOpen) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireCheckedSyscalls) = 1.152.0
Provides:       perl(Perl::Critic::Policy::InputOutput::RequireEncodingWithUTF8Layer) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitFormats) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitTies) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitUnrestrictedNoCritic) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Miscellanea::ProhibitUselessNoCritic) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitAutomaticExportation) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitConditionalUseStatements) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitEvilModules) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitExcessMainComplexity) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitMultiplePackages) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::RequireBarewordIncludes) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::RequireEndWithOne) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::RequireExplicitPackage) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::RequireFilenameMatchesPackage) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::RequireNoMatchVarsWithUseEnglish) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Modules::RequireVersionVar) = 1.152.0
Provides:       perl(Perl::Critic::Policy::NamingConventions::Capitalization) = 1.152.0
Provides:       perl(Perl::Critic::Policy::NamingConventions::ProhibitAmbiguousNames) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Objects::ProhibitIndirectSyntax) = 1.152.0
Provides:       perl(Perl::Critic::Policy::References::ProhibitDoubleSigils) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitCaptureWithoutTest) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitComplexRegexes) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitEnumeratedClasses) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitEscapedMetacharacters) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitFixedStringMatches) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitSingleCharAlternation) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitUnusedCapture) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitUnusualDelimiters) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::ProhibitUselessTopic) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireBracesForMultiline) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireDotMatchAnything) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireExtendedFormatting) = 1.152.0
Provides:       perl(Perl::Critic::Policy::RegularExpressions::RequireLineBoundaryMatching) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitAmpersandSigils) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitBuiltinHomonyms) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitExcessComplexity) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitExplicitReturnUndef) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitManyArgs) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitNestedSubs) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitReturnSort) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitSubroutinePrototypes) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProhibitUnusedPrivateSubroutines) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::ProtectPrivateSubs) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::RequireArgUnpacking) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Subroutines::RequireFinalReturn) = 1.152.0
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::ProhibitNoStrict) = 1.152.0
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::ProhibitNoWarnings) = 1.152.0
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::ProhibitProlongedStrictureOverride) = 1.152.0
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::RequireTestLabels) = 1.152.0
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::RequireUseStrict) = 1.152.0
Provides:       perl(Perl::Critic::Policy::TestingAndDebugging::RequireUseWarnings) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitCommaSeparatedStatements) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitComplexVersion) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitConstantPragma) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitEmptyQuotes) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitEscapedCharacters) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitImplicitNewlines) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitInterpolationOfLiterals) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitLeadingZeros) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitLongChainsOfMethodCalls) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMagicNumbers) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMismatchedOperators) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMixedBooleanOperators) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitNoisyQuotes) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitQuotesAsQuotelikeOperatorDelimiters) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitSpecialLiteralHeredocTerminator) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitVersionStrings) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireConstantVersion) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireInterpolationOfMetachars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireNumberSeparators) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireQuotedHeredocTerminator) = 1.152.0
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::RequireUpperCaseHeredocTerminator) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitAugmentedAssignmentInDeclaration) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitConditionalDeclarations) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitEvilVariables) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitLocalVars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitMatchVars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitPackageVars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitPerl4PackageNames) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitPunctuationVars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitReusedNames) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitUnusedVariables) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::ProtectPrivateVars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::RequireInitializationForLocalVars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::RequireLexicalLoopIterators) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::RequireLocalizedPunctuationVars) = 1.152.0
Provides:       perl(Perl::Critic::Policy::Variables::RequireNegativeIndices) = 1.152.0
Provides:       perl(Perl::Critic::PolicyConfig) = 1.152.0
Provides:       perl(Perl::Critic::PolicyFactory) = 1.152.0
Provides:       perl(Perl::Critic::PolicyListing) = 1.152.0
Provides:       perl(Perl::Critic::PolicyParameter) = 1.152.0
Provides:       perl(Perl::Critic::PolicyParameter::Behavior) = 1.152.0
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::Boolean) = 1.152.0
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::Enumeration) = 1.152.0
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::Integer) = 1.152.0
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::String) = 1.152.0
Provides:       perl(Perl::Critic::PolicyParameter::Behavior::StringList) = 1.152.0
Provides:       perl(Perl::Critic::ProfilePrototype) = 1.152.0
Provides:       perl(Perl::Critic::Statistics) = 1.152.0
Provides:       perl(Perl::Critic::TestUtils) = 1.152.0
Provides:       perl(Perl::Critic::Theme) = 1.152.0
Provides:       perl(Perl::Critic::ThemeListing) = 1.152.0
Provides:       perl(Perl::Critic::UserProfile) = 1.152.0
Provides:       perl(Perl::Critic::Utils) = 1.152.0
Provides:       perl(Perl::Critic::Utils::Constants) = 1.152.0
Provides:       perl(Perl::Critic::Utils::McCabe) = 1.152.0
Provides:       perl(Perl::Critic::Utils::POD) = 1.152.0
Provides:       perl(Perl::Critic::Utils::PPI) = 1.152.0
Provides:       perl(Perl::Critic::Utils::Perl) = 1.152.0
Provides:       perl(Perl::Critic::Violation) = 1.152.0
Provides:       perl(Test::Perl::Critic::Policy) = 1.152.0
%define         __perllib_provides /bin/true
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
