#
# spec file for package perl-Moose
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


%define cpan_name Moose
Name:           perl-Moose
Version:        2.2206
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Postmodern object system for Perl 5
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(Class::Load) >= 0.09
BuildRequires:  perl(Class::Load::XS) >= 0.01
BuildRequires:  perl(Data::OptList) >= 0.107
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Devel::OverloadInfo) >= 0.005
BuildRequires:  perl(Devel::StackTrace) >= 2.03
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Eval::Closure) >= 0.04
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(MRO::Compat) >= 0.05
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(Module::Runtime::Conflicts) >= 0.002
BuildRequires:  perl(Package::DeprecationManager) >= 0.11
BuildRequires:  perl(Package::Stash) >= 0.32
BuildRequires:  perl(Package::Stash::XS) >= 0.24
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Scalar::Util) >= 1.19
BuildRequires:  perl(Sub::Exporter) >= 0.980
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::CleanNamespaces) >= 0.13
BuildRequires:  perl(Test::Fatal) >= 0.001
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs) >= 0.002010
BuildRequires:  perl(Try::Tiny) >= 0.17
BuildRequires:  perl(parent) >= 0.223
Requires:       perl(Carp) >= 1.22
Requires:       perl(Class::Load) >= 0.09
Requires:       perl(Class::Load::XS) >= 0.01
Requires:       perl(Data::OptList) >= 0.107
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(Devel::OverloadInfo) >= 0.005
Requires:       perl(Devel::StackTrace) >= 2.03
Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(Eval::Closure) >= 0.04
Requires:       perl(List::Util) >= 1.56
Requires:       perl(MRO::Compat) >= 0.05
Requires:       perl(Module::Runtime) >= 0.014
Requires:       perl(Module::Runtime::Conflicts) >= 0.002
Requires:       perl(Package::DeprecationManager) >= 0.11
Requires:       perl(Package::Stash) >= 0.32
Requires:       perl(Package::Stash::XS) >= 0.24
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Scalar::Util) >= 1.19
Requires:       perl(Sub::Exporter) >= 0.980
Requires:       perl(Sub::Util) >= 1.40
Requires:       perl(Try::Tiny) >= 0.17
Requires:       perl(parent) >= 0.223
Provides:       perl(Class::MOP) = 2.2206
Provides:       perl(Class::MOP::Attribute) = 2.2206
Provides:       perl(Class::MOP::Class) = 2.2206
Provides:       perl(Class::MOP::Class::Immutable::Trait) = 2.2206
Provides:       perl(Class::MOP::Deprecated) = 2.2206
Provides:       perl(Class::MOP::Instance) = 2.2206
Provides:       perl(Class::MOP::Method) = 2.2206
Provides:       perl(Class::MOP::Method::Accessor) = 2.2206
Provides:       perl(Class::MOP::Method::Constructor) = 2.2206
Provides:       perl(Class::MOP::Method::Generated) = 2.2206
Provides:       perl(Class::MOP::Method::Inlined) = 2.2206
Provides:       perl(Class::MOP::Method::Meta) = 2.2206
Provides:       perl(Class::MOP::Method::Wrapped) = 2.2206
Provides:       perl(Class::MOP::MiniTrait) = 2.2206
Provides:       perl(Class::MOP::Mixin) = 2.2206
Provides:       perl(Class::MOP::Mixin::AttributeCore) = 2.2206
Provides:       perl(Class::MOP::Mixin::HasAttributes) = 2.2206
Provides:       perl(Class::MOP::Mixin::HasMethods) = 2.2206
Provides:       perl(Class::MOP::Mixin::HasOverloads) = 2.2206
Provides:       perl(Class::MOP::Module) = 2.2206
Provides:       perl(Class::MOP::Object) = 2.2206
Provides:       perl(Class::MOP::Overload) = 2.2206
Provides:       perl(Class::MOP::Package) = 2.2206
Provides:       perl(Moose) = 2.2206
Provides:       perl(Moose::Cookbook) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::BankAccount_MethodModifiersAndSubclassing) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::BinaryTree_AttributeFeatures) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::BinaryTree_BuilderAndLazyBuild) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::Company_Subtypes) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::DateTime_ExtendingNonMooseParent) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::Document_AugmentAndInner) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::Genome_OverloadingSubtypesAndCoercion) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::HTTP_SubtypesAndCoercion) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::Immutable) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::Person_BUILDARGSAndBUILD) = 2.2206
Provides:       perl(Moose::Cookbook::Basics::Point_AttributesAndSubclassing) = 2.2206
Provides:       perl(Moose::Cookbook::Extending::Debugging_BaseClassRole) = 2.2206
Provides:       perl(Moose::Cookbook::Extending::ExtensionOverview) = 2.2206
Provides:       perl(Moose::Cookbook::Extending::Mooseish_MooseSugar) = 2.2206
Provides:       perl(Moose::Cookbook::Legacy::Debugging_BaseClassReplacement) = 2.2206
Provides:       perl(Moose::Cookbook::Legacy::Labeled_AttributeMetaclass) = 2.2206
Provides:       perl(Moose::Cookbook::Legacy::Table_ClassMetaclass) = 2.2206
Provides:       perl(Moose::Cookbook::Meta::GlobRef_InstanceMetaclass) = 2.2206
Provides:       perl(Moose::Cookbook::Meta::Labeled_AttributeTrait) = 2.2206
Provides:       perl(Moose::Cookbook::Meta::PrivateOrPublic_MethodMetaclass) = 2.2206
Provides:       perl(Moose::Cookbook::Meta::Table_MetaclassTrait) = 2.2206
Provides:       perl(Moose::Cookbook::Meta::WhyMeta) = 2.2206
Provides:       perl(Moose::Cookbook::Roles::ApplicationToInstance) = 2.2206
Provides:       perl(Moose::Cookbook::Roles::Comparable_CodeReuse) = 2.2206
Provides:       perl(Moose::Cookbook::Roles::Restartable_AdvancedComposition) = 2.2206
Provides:       perl(Moose::Cookbook::Snack::Keywords) = 2.2206
Provides:       perl(Moose::Cookbook::Snack::Types) = 2.2206
Provides:       perl(Moose::Cookbook::Style) = 2.2206
Provides:       perl(Moose::Deprecated) = 2.2206
Provides:       perl(Moose::Exception) = 2.2206
Provides:       perl(Moose::Exception::AccessorMustReadWrite) = 2.2206
Provides:       perl(Moose::Exception::AddParameterizableTypeTakesParameterizableType) = 2.2206
Provides:       perl(Moose::Exception::AddRoleTakesAMooseMetaRoleInstance) = 2.2206
Provides:       perl(Moose::Exception::AddRoleToARoleTakesAMooseMetaRole) = 2.2206
Provides:       perl(Moose::Exception::ApplyTakesABlessedInstance) = 2.2206
Provides:       perl(Moose::Exception::AttachToClassNeedsAClassMOPClassInstanceOrASubclass) = 2.2206
Provides:       perl(Moose::Exception::AttributeConflictInRoles) = 2.2206
Provides:       perl(Moose::Exception::AttributeConflictInSummation) = 2.2206
Provides:       perl(Moose::Exception::AttributeExtensionIsNotSupportedInRoles) = 2.2206
Provides:       perl(Moose::Exception::AttributeIsRequired) = 2.2206
Provides:       perl(Moose::Exception::AttributeMustBeAnClassMOPMixinAttributeCoreOrSubclass) = 2.2206
Provides:       perl(Moose::Exception::AttributeNamesDoNotMatch) = 2.2206
Provides:       perl(Moose::Exception::AttributeValueIsNotAnObject) = 2.2206
Provides:       perl(Moose::Exception::AttributeValueIsNotDefined) = 2.2206
Provides:       perl(Moose::Exception::AutoDeRefNeedsArrayRefOrHashRef) = 2.2206
Provides:       perl(Moose::Exception::BadOptionFormat) = 2.2206
Provides:       perl(Moose::Exception::BothBuilderAndDefaultAreNotAllowed) = 2.2206
Provides:       perl(Moose::Exception::BuilderDoesNotExist) = 2.2206
Provides:       perl(Moose::Exception::BuilderMethodNotSupportedForAttribute) = 2.2206
Provides:       perl(Moose::Exception::BuilderMethodNotSupportedForInlineAttribute) = 2.2206
Provides:       perl(Moose::Exception::BuilderMustBeAMethodName) = 2.2206
Provides:       perl(Moose::Exception::CallingMethodOnAnImmutableInstance) = 2.2206
Provides:       perl(Moose::Exception::CallingReadOnlyMethodOnAnImmutableInstance) = 2.2206
Provides:       perl(Moose::Exception::CanExtendOnlyClasses) = 2.2206
Provides:       perl(Moose::Exception::CanOnlyConsumeRole) = 2.2206
Provides:       perl(Moose::Exception::CanOnlyWrapBlessedCode) = 2.2206
Provides:       perl(Moose::Exception::CanReblessOnlyIntoASubclass) = 2.2206
Provides:       perl(Moose::Exception::CanReblessOnlyIntoASuperclass) = 2.2206
Provides:       perl(Moose::Exception::CannotAddAdditionalTypeCoercionsToUnion) = 2.2206
Provides:       perl(Moose::Exception::CannotAddAsAnAttributeToARole) = 2.2206
Provides:       perl(Moose::Exception::CannotApplyBaseClassRolesToRole) = 2.2206
Provides:       perl(Moose::Exception::CannotAssignValueToReadOnlyAccessor) = 2.2206
Provides:       perl(Moose::Exception::CannotAugmentIfLocalMethodPresent) = 2.2206
Provides:       perl(Moose::Exception::CannotAugmentNoSuperMethod) = 2.2206
Provides:       perl(Moose::Exception::CannotAutoDerefWithoutIsa) = 2.2206
Provides:       perl(Moose::Exception::CannotAutoDereferenceTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::CannotCalculateNativeType) = 2.2206
Provides:       perl(Moose::Exception::CannotCallAnAbstractBaseMethod) = 2.2206
Provides:       perl(Moose::Exception::CannotCallAnAbstractMethod) = 2.2206
Provides:       perl(Moose::Exception::CannotCoerceAWeakRef) = 2.2206
Provides:       perl(Moose::Exception::CannotCoerceAttributeWhichHasNoCoercion) = 2.2206
Provides:       perl(Moose::Exception::CannotCreateHigherOrderTypeWithoutATypeParameter) = 2.2206
Provides:       perl(Moose::Exception::CannotCreateMethodAliasLocalMethodIsPresent) = 2.2206
Provides:       perl(Moose::Exception::CannotCreateMethodAliasLocalMethodIsPresentInClass) = 2.2206
Provides:       perl(Moose::Exception::CannotDelegateLocalMethodIsPresent) = 2.2206
Provides:       perl(Moose::Exception::CannotDelegateWithoutIsa) = 2.2206
Provides:       perl(Moose::Exception::CannotFindDelegateMetaclass) = 2.2206
Provides:       perl(Moose::Exception::CannotFindType) = 2.2206
Provides:       perl(Moose::Exception::CannotFindTypeGivenToMatchOnType) = 2.2206
Provides:       perl(Moose::Exception::CannotFixMetaclassCompatibility) = 2.2206
Provides:       perl(Moose::Exception::CannotGenerateInlineConstraint) = 2.2206
Provides:       perl(Moose::Exception::CannotInitializeMooseMetaRoleComposite) = 2.2206
Provides:       perl(Moose::Exception::CannotInlineTypeConstraintCheck) = 2.2206
Provides:       perl(Moose::Exception::CannotLocatePackageInINC) = 2.2206
Provides:       perl(Moose::Exception::CannotMakeMetaclassCompatible) = 2.2206
Provides:       perl(Moose::Exception::CannotOverrideALocalMethod) = 2.2206
Provides:       perl(Moose::Exception::CannotOverrideBodyOfMetaMethods) = 2.2206
Provides:       perl(Moose::Exception::CannotOverrideLocalMethodIsPresent) = 2.2206
Provides:       perl(Moose::Exception::CannotOverrideNoSuperMethod) = 2.2206
Provides:       perl(Moose::Exception::CannotRegisterUnnamedTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::CannotUseLazyBuildAndDefaultSimultaneously) = 2.2206
Provides:       perl(Moose::Exception::CircularReferenceInAlso) = 2.2206
Provides:       perl(Moose::Exception::ClassDoesNotHaveInitMeta) = 2.2206
Provides:       perl(Moose::Exception::ClassDoesTheExcludedRole) = 2.2206
Provides:       perl(Moose::Exception::ClassNamesDoNotMatch) = 2.2206
Provides:       perl(Moose::Exception::CloneObjectExpectsAnInstanceOfMetaclass) = 2.2206
Provides:       perl(Moose::Exception::CodeBlockMustBeACodeRef) = 2.2206
Provides:       perl(Moose::Exception::CoercingWithoutCoercions) = 2.2206
Provides:       perl(Moose::Exception::CoercionAlreadyExists) = 2.2206
Provides:       perl(Moose::Exception::CoercionNeedsTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::ConflictDetectedInCheckRoleExclusions) = 2.2206
Provides:       perl(Moose::Exception::ConflictDetectedInCheckRoleExclusionsInToClass) = 2.2206
Provides:       perl(Moose::Exception::ConstructClassInstanceTakesPackageName) = 2.2206
Provides:       perl(Moose::Exception::CouldNotCreateMethod) = 2.2206
Provides:       perl(Moose::Exception::CouldNotCreateWriter) = 2.2206
Provides:       perl(Moose::Exception::CouldNotEvalConstructor) = 2.2206
Provides:       perl(Moose::Exception::CouldNotEvalDestructor) = 2.2206
Provides:       perl(Moose::Exception::CouldNotFindTypeConstraintToCoerceFrom) = 2.2206
Provides:       perl(Moose::Exception::CouldNotGenerateInlineAttributeMethod) = 2.2206
Provides:       perl(Moose::Exception::CouldNotLocateTypeConstraintForUnion) = 2.2206
Provides:       perl(Moose::Exception::CouldNotParseType) = 2.2206
Provides:       perl(Moose::Exception::CreateMOPClassTakesArrayRefOfAttributes) = 2.2206
Provides:       perl(Moose::Exception::CreateMOPClassTakesArrayRefOfSuperclasses) = 2.2206
Provides:       perl(Moose::Exception::CreateMOPClassTakesHashRefOfMethods) = 2.2206
Provides:       perl(Moose::Exception::CreateTakesArrayRefOfRoles) = 2.2206
Provides:       perl(Moose::Exception::CreateTakesHashRefOfAttributes) = 2.2206
Provides:       perl(Moose::Exception::CreateTakesHashRefOfMethods) = 2.2206
Provides:       perl(Moose::Exception::DefaultToMatchOnTypeMustBeCodeRef) = 2.2206
Provides:       perl(Moose::Exception::DelegationToAClassWhichIsNotLoaded) = 2.2206
Provides:       perl(Moose::Exception::DelegationToARoleWhichIsNotLoaded) = 2.2206
Provides:       perl(Moose::Exception::DelegationToATypeWhichIsNotAClass) = 2.2206
Provides:       perl(Moose::Exception::DoesRequiresRoleName) = 2.2206
Provides:       perl(Moose::Exception::EnumCalledWithAnArrayRefAndAdditionalArgs) = 2.2206
Provides:       perl(Moose::Exception::EnumValuesMustBeString) = 2.2206
Provides:       perl(Moose::Exception::ExtendsMissingArgs) = 2.2206
Provides:       perl(Moose::Exception::HandlesMustBeAHashRef) = 2.2206
Provides:       perl(Moose::Exception::IllegalInheritedOptions) = 2.2206
Provides:       perl(Moose::Exception::IllegalMethodTypeToAddMethodModifier) = 2.2206
Provides:       perl(Moose::Exception::IncompatibleMetaclassOfSuperclass) = 2.2206
Provides:       perl(Moose::Exception::InitMetaRequiresClass) = 2.2206
Provides:       perl(Moose::Exception::InitializeTakesUnBlessedPackageName) = 2.2206
Provides:       perl(Moose::Exception::InstanceBlessedIntoWrongClass) = 2.2206
Provides:       perl(Moose::Exception::InstanceMustBeABlessedReference) = 2.2206
Provides:       perl(Moose::Exception::InvalidArgPassedToMooseUtilMetaRole) = 2.2206
Provides:       perl(Moose::Exception::InvalidArgumentToMethod) = 2.2206
Provides:       perl(Moose::Exception::InvalidArgumentsToTraitAliases) = 2.2206
Provides:       perl(Moose::Exception::InvalidBaseTypeGivenToCreateParameterizedTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::InvalidHandleValue) = 2.2206
Provides:       perl(Moose::Exception::InvalidHasProvidedInARole) = 2.2206
Provides:       perl(Moose::Exception::InvalidNameForType) = 2.2206
Provides:       perl(Moose::Exception::InvalidOverloadOperator) = 2.2206
Provides:       perl(Moose::Exception::InvalidRoleApplication) = 2.2206
Provides:       perl(Moose::Exception::InvalidTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::InvalidTypeGivenToCreateParameterizedTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::InvalidValueForIs) = 2.2206
Provides:       perl(Moose::Exception::IsaDoesNotDoTheRole) = 2.2206
Provides:       perl(Moose::Exception::IsaLacksDoesMethod) = 2.2206
Provides:       perl(Moose::Exception::LazyAttributeNeedsADefault) = 2.2206
Provides:       perl(Moose::Exception::Legacy) = 2.2206
Provides:       perl(Moose::Exception::MOPAttributeNewNeedsAttributeName) = 2.2206
Provides:       perl(Moose::Exception::MatchActionMustBeACodeRef) = 2.2206
Provides:       perl(Moose::Exception::MessageParameterMustBeCodeRef) = 2.2206
Provides:       perl(Moose::Exception::MetaclassIsAClassNotASubclassOfGivenMetaclass) = 2.2206
Provides:       perl(Moose::Exception::MetaclassIsARoleNotASubclassOfGivenMetaclass) = 2.2206
Provides:       perl(Moose::Exception::MetaclassIsNotASubclassOfGivenMetaclass) = 2.2206
Provides:       perl(Moose::Exception::MetaclassMustBeASubclassOfMooseMetaClass) = 2.2206
Provides:       perl(Moose::Exception::MetaclassMustBeASubclassOfMooseMetaRole) = 2.2206
Provides:       perl(Moose::Exception::MetaclassMustBeDerivedFromClassMOPClass) = 2.2206
Provides:       perl(Moose::Exception::MetaclassNotLoaded) = 2.2206
Provides:       perl(Moose::Exception::MetaclassTypeIncompatible) = 2.2206
Provides:       perl(Moose::Exception::MethodExpectedAMetaclassObject) = 2.2206
Provides:       perl(Moose::Exception::MethodExpectsFewerArgs) = 2.2206
Provides:       perl(Moose::Exception::MethodExpectsMoreArgs) = 2.2206
Provides:       perl(Moose::Exception::MethodModifierNeedsMethodName) = 2.2206
Provides:       perl(Moose::Exception::MethodNameConflictInRoles) = 2.2206
Provides:       perl(Moose::Exception::MethodNameNotFoundInInheritanceHierarchy) = 2.2206
Provides:       perl(Moose::Exception::MethodNameNotGiven) = 2.2206
Provides:       perl(Moose::Exception::MustDefineAMethodName) = 2.2206
Provides:       perl(Moose::Exception::MustDefineAnAttributeName) = 2.2206
Provides:       perl(Moose::Exception::MustDefineAnOverloadOperator) = 2.2206
Provides:       perl(Moose::Exception::MustHaveAtLeastOneValueToEnumerate) = 2.2206
Provides:       perl(Moose::Exception::MustPassAHashOfOptions) = 2.2206
Provides:       perl(Moose::Exception::MustPassAMooseMetaRoleInstanceOrSubclass) = 2.2206
Provides:       perl(Moose::Exception::MustPassAPackageNameOrAnExistingClassMOPPackageInstance) = 2.2206
Provides:       perl(Moose::Exception::MustPassEvenNumberOfArguments) = 2.2206
Provides:       perl(Moose::Exception::MustPassEvenNumberOfAttributeOptions) = 2.2206
Provides:       perl(Moose::Exception::MustProvideANameForTheAttribute) = 2.2206
Provides:       perl(Moose::Exception::MustSpecifyAtleastOneMethod) = 2.2206
Provides:       perl(Moose::Exception::MustSpecifyAtleastOneRole) = 2.2206
Provides:       perl(Moose::Exception::MustSpecifyAtleastOneRoleToApplicant) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyAClassMOPAttributeInstance) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyADelegateToMethod) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyAMetaclass) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyAMooseMetaAttributeInstance) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyAnAccessorTypeToConstructWith) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyAnAttributeToConstructWith) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyArrayRefAsCurriedArguments) = 2.2206
Provides:       perl(Moose::Exception::MustSupplyPackageNameAndName) = 2.2206
Provides:       perl(Moose::Exception::NeedsTypeConstraintUnionForTypeCoercionUnion) = 2.2206
Provides:       perl(Moose::Exception::NeitherAttributeNorAttributeNameIsGiven) = 2.2206
Provides:       perl(Moose::Exception::NeitherClassNorClassNameIsGiven) = 2.2206
Provides:       perl(Moose::Exception::NeitherRoleNorRoleNameIsGiven) = 2.2206
Provides:       perl(Moose::Exception::NeitherTypeNorTypeNameIsGiven) = 2.2206
Provides:       perl(Moose::Exception::NoAttributeFoundInSuperClass) = 2.2206
Provides:       perl(Moose::Exception::NoBodyToInitializeInAnAbstractBaseClass) = 2.2206
Provides:       perl(Moose::Exception::NoCasesMatched) = 2.2206
Provides:       perl(Moose::Exception::NoConstraintCheckForTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::NoDestructorClassSpecified) = 2.2206
Provides:       perl(Moose::Exception::NoImmutableTraitSpecifiedForClass) = 2.2206
Provides:       perl(Moose::Exception::NoParentGivenToSubtype) = 2.2206
Provides:       perl(Moose::Exception::OnlyInstancesCanBeCloned) = 2.2206
Provides:       perl(Moose::Exception::OperatorIsRequired) = 2.2206
Provides:       perl(Moose::Exception::OverloadConflictInSummation) = 2.2206
Provides:       perl(Moose::Exception::OverloadRequiresAMetaClass) = 2.2206
Provides:       perl(Moose::Exception::OverloadRequiresAMetaMethod) = 2.2206
Provides:       perl(Moose::Exception::OverloadRequiresAMetaOverload) = 2.2206
Provides:       perl(Moose::Exception::OverloadRequiresAMethodNameOrCoderef) = 2.2206
Provides:       perl(Moose::Exception::OverloadRequiresAnOperator) = 2.2206
Provides:       perl(Moose::Exception::OverloadRequiresNamesForCoderef) = 2.2206
Provides:       perl(Moose::Exception::OverrideConflictInComposition) = 2.2206
Provides:       perl(Moose::Exception::OverrideConflictInSummation) = 2.2206
Provides:       perl(Moose::Exception::PackageDoesNotUseMooseExporter) = 2.2206
Provides:       perl(Moose::Exception::PackageNameAndNameParamsNotGivenToWrap) = 2.2206
Provides:       perl(Moose::Exception::PackagesAndModulesAreNotCachable) = 2.2206
Provides:       perl(Moose::Exception::ParameterIsNotSubtypeOfParent) = 2.2206
Provides:       perl(Moose::Exception::ReferencesAreNotAllowedAsDefault) = 2.2206
Provides:       perl(Moose::Exception::RequiredAttributeLacksInitialization) = 2.2206
Provides:       perl(Moose::Exception::RequiredAttributeNeedsADefault) = 2.2206
Provides:       perl(Moose::Exception::RequiredMethodsImportedByClass) = 2.2206
Provides:       perl(Moose::Exception::RequiredMethodsNotImplementedByClass) = 2.2206
Provides:       perl(Moose::Exception::Role::Attribute) = 2.2206
Provides:       perl(Moose::Exception::Role::AttributeName) = 2.2206
Provides:       perl(Moose::Exception::Role::Class) = 2.2206
Provides:       perl(Moose::Exception::Role::EitherAttributeOrAttributeName) = 2.2206
Provides:       perl(Moose::Exception::Role::Instance) = 2.2206
Provides:       perl(Moose::Exception::Role::InstanceClass) = 2.2206
Provides:       perl(Moose::Exception::Role::InvalidAttributeOptions) = 2.2206
Provides:       perl(Moose::Exception::Role::Method) = 2.2206
Provides:       perl(Moose::Exception::Role::ParamsHash) = 2.2206
Provides:       perl(Moose::Exception::Role::Role) = 2.2206
Provides:       perl(Moose::Exception::Role::RoleForCreate) = 2.2206
Provides:       perl(Moose::Exception::Role::RoleForCreateMOPClass) = 2.2206
Provides:       perl(Moose::Exception::Role::TypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::RoleDoesTheExcludedRole) = 2.2206
Provides:       perl(Moose::Exception::RoleExclusionConflict) = 2.2206
Provides:       perl(Moose::Exception::RoleNameRequired) = 2.2206
Provides:       perl(Moose::Exception::RoleNameRequiredForMooseMetaRole) = 2.2206
Provides:       perl(Moose::Exception::RolesDoNotSupportAugment) = 2.2206
Provides:       perl(Moose::Exception::RolesDoNotSupportExtends) = 2.2206
Provides:       perl(Moose::Exception::RolesDoNotSupportInner) = 2.2206
Provides:       perl(Moose::Exception::RolesDoNotSupportRegexReferencesForMethodModifiers) = 2.2206
Provides:       perl(Moose::Exception::RolesInCreateTakesAnArrayRef) = 2.2206
Provides:       perl(Moose::Exception::RolesListMustBeInstancesOfMooseMetaRole) = 2.2206
Provides:       perl(Moose::Exception::SingleParamsToNewMustBeHashRef) = 2.2206
Provides:       perl(Moose::Exception::TriggerMustBeACodeRef) = 2.2206
Provides:       perl(Moose::Exception::TypeConstraintCannotBeUsedForAParameterizableType) = 2.2206
Provides:       perl(Moose::Exception::TypeConstraintIsAlreadyCreated) = 2.2206
Provides:       perl(Moose::Exception::TypeParameterMustBeMooseMetaType) = 2.2206
Provides:       perl(Moose::Exception::UnableToCanonicalizeHandles) = 2.2206
Provides:       perl(Moose::Exception::UnableToCanonicalizeNonRolePackage) = 2.2206
Provides:       perl(Moose::Exception::UnableToRecognizeDelegateMetaclass) = 2.2206
Provides:       perl(Moose::Exception::UndefinedHashKeysPassedToMethod) = 2.2206
Provides:       perl(Moose::Exception::UnionCalledWithAnArrayRefAndAdditionalArgs) = 2.2206
Provides:       perl(Moose::Exception::UnionTakesAtleastTwoTypeNames) = 2.2206
Provides:       perl(Moose::Exception::ValidationFailedForInlineTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::ValidationFailedForTypeConstraint) = 2.2206
Provides:       perl(Moose::Exception::WrapTakesACodeRefToBless) = 2.2206
Provides:       perl(Moose::Exception::WrongTypeConstraintGiven) = 2.2206
Provides:       perl(Moose::Exporter) = 2.2206
Provides:       perl(Moose::Intro) = 2.2206
Provides:       perl(Moose::Manual) = 2.2206
Provides:       perl(Moose::Manual::Attributes) = 2.2206
Provides:       perl(Moose::Manual::BestPractices) = 2.2206
Provides:       perl(Moose::Manual::Classes) = 2.2206
Provides:       perl(Moose::Manual::Concepts) = 2.2206
Provides:       perl(Moose::Manual::Construction) = 2.2206
Provides:       perl(Moose::Manual::Contributing) = 2.2206
Provides:       perl(Moose::Manual::Delegation) = 2.2206
Provides:       perl(Moose::Manual::Delta) = 2.2206
Provides:       perl(Moose::Manual::Exceptions) = 2.2206
Provides:       perl(Moose::Manual::Exceptions::Manifest) = 2.2206
Provides:       perl(Moose::Manual::FAQ) = 2.2206
Provides:       perl(Moose::Manual::MOP) = 2.2206
Provides:       perl(Moose::Manual::MethodModifiers) = 2.2206
Provides:       perl(Moose::Manual::MooseX) = 2.2206
Provides:       perl(Moose::Manual::Resources) = 2.2206
Provides:       perl(Moose::Manual::Roles) = 2.2206
Provides:       perl(Moose::Manual::Support) = 2.2206
Provides:       perl(Moose::Manual::Types) = 2.2206
Provides:       perl(Moose::Manual::Unsweetened) = 2.2206
Provides:       perl(Moose::Meta::Attribute) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait::Array) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait::Bool) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait::Code) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait::Counter) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait::Hash) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait::Number) = 2.2206
Provides:       perl(Moose::Meta::Attribute::Native::Trait::String) = 2.2206
Provides:       perl(Moose::Meta::Class) = 2.2206
Provides:       perl(Moose::Meta::Class::Immutable::Trait) = 2.2206
Provides:       perl(Moose::Meta::Instance) = 2.2206
Provides:       perl(Moose::Meta::Method) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::Writer) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::accessor) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::clear) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::count) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::delete) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::elements) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::first) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::first_index) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::get) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::grep) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::insert) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::is_empty) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::join) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::map) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::natatime) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::pop) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::push) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::reduce) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::set) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::shallow_clone) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::shift) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::shuffle) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::sort) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::sort_in_place) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::splice) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::uniq) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Array::unshift) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Bool::not) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Bool::set) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Bool::toggle) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Bool::unset) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Code::execute) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Code::execute_method) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Collection) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Counter::Writer) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Counter::dec) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Counter::inc) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Counter::reset) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Counter::set) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::Writer) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::accessor) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::clear) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::count) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::defined) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::delete) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::elements) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::exists) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::get) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::is_empty) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::keys) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::kv) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::set) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::shallow_clone) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Hash::values) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Number::abs) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Number::add) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Number::div) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Number::mod) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Number::mul) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Number::set) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Number::sub) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Reader) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::append) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::chomp) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::chop) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::clear) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::inc) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::length) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::match) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::prepend) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::replace) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::String::substr) = 2.2206
Provides:       perl(Moose::Meta::Method::Accessor::Native::Writer) = 2.2206
Provides:       perl(Moose::Meta::Method::Augmented) = 2.2206
Provides:       perl(Moose::Meta::Method::Constructor) = 2.2206
Provides:       perl(Moose::Meta::Method::Delegation) = 2.2206
Provides:       perl(Moose::Meta::Method::Destructor) = 2.2206
Provides:       perl(Moose::Meta::Method::Meta) = 2.2206
Provides:       perl(Moose::Meta::Method::Overridden) = 2.2206
Provides:       perl(Moose::Meta::Mixin::AttributeCore) = 2.2206
Provides:       perl(Moose::Meta::Object::Trait) = 2.2206
Provides:       perl(Moose::Meta::Role) = 2.2206
Provides:       perl(Moose::Meta::Role::Application) = 2.2206
Provides:       perl(Moose::Meta::Role::Application::RoleSummation) = 2.2206
Provides:       perl(Moose::Meta::Role::Application::ToClass) = 2.2206
Provides:       perl(Moose::Meta::Role::Application::ToInstance) = 2.2206
Provides:       perl(Moose::Meta::Role::Application::ToRole) = 2.2206
Provides:       perl(Moose::Meta::Role::Attribute) = 2.2206
Provides:       perl(Moose::Meta::Role::Composite) = 2.2206
Provides:       perl(Moose::Meta::Role::Method) = 2.2206
Provides:       perl(Moose::Meta::Role::Method::Conflicting) = 2.2206
Provides:       perl(Moose::Meta::Role::Method::Required) = 2.2206
Provides:       perl(Moose::Meta::TypeCoercion) = 2.2206
Provides:       perl(Moose::Meta::TypeCoercion::Union) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::Class) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::DuckType) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::Enum) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::Parameterizable) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::Parameterized) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::Registry) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::Role) = 2.2206
Provides:       perl(Moose::Meta::TypeConstraint::Union) = 2.2206
Provides:       perl(Moose::Object) = 2.2206
Provides:       perl(Moose::Role) = 2.2206
Provides:       perl(Moose::Spec::Role) = 2.2206
Provides:       perl(Moose::Unsweetened) = 2.2206
Provides:       perl(Moose::Util) = 2.2206
Provides:       perl(Moose::Util::MetaRole) = 2.2206
Provides:       perl(Moose::Util::TypeConstraints) = 2.2206
Provides:       perl(Moose::Util::TypeConstraints::Builtins) = 2.2206
Provides:       perl(Test::Moose) = 2.2206
Provides:       perl(metaclass) = 2.2206
Provides:       perl(oose) = 2.2206
%define         __perllib_provides /bin/true
Recommends:     perl(Data::OptList) >= 0.110
%{perl_requires}
# MANUAL BEGIN
Provides:       perl-Class-MOP = %{version}
Obsoletes:      perl-Class-MOP < %{version}
# MANUAL END

%description
Moose is an extension of the Perl 5 object system.

The main goal of Moose is to make Perl 5 Object Oriented programming
easier, more consistent, and less tedious. With Moose you can think more
about what you want to do and less about the mechanics of OOP.

Additionally, Moose is built on top of Class::MOP, which is a metaclass
system for Perl 5. This means that Moose not only makes building normal
Perl 5 objects better, but it provides the power of metaclass programming
as well.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes Changes.Class-MOP doc README.md TODO
%license LICENSE

%changelog
