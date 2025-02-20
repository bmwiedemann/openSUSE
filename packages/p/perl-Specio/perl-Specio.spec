#
# spec file for package perl-Specio
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


%define cpan_name Specio
Name:           perl-Specio
Version:        0.500.0
Release:        0
# 0.50 -> normalize -> 0.500.0
%define cpan_version 0.50
License:        Artistic-2.0
Summary:        Type constraints and coercions for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Role::Tiny) >= 1.003003
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XString)
BuildRequires:  perl(parent)
BuildRequires:  perl(version) >= 0.83
Requires:       perl(Clone)
Requires:       perl(Devel::StackTrace)
Requires:       perl(Eval::Closure)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(MRO::Compat)
Requires:       perl(Module::Runtime)
Requires:       perl(Role::Tiny) >= 1.003003
Requires:       perl(Role::Tiny::With)
Requires:       perl(Sub::Quote)
Requires:       perl(Test::Fatal)
Requires:       perl(Test::More) >= 0.96
Requires:       perl(Try::Tiny)
Requires:       perl(XString)
Requires:       perl(parent)
Requires:       perl(version) >= 0.83
Provides:       perl(Specio) = %{version}
Provides:       perl(Specio::Coercion) = %{version}
Provides:       perl(Specio::Constraint::AnyCan) = %{version}
Provides:       perl(Specio::Constraint::AnyDoes) = %{version}
Provides:       perl(Specio::Constraint::AnyIsa) = %{version}
Provides:       perl(Specio::Constraint::Enum) = %{version}
Provides:       perl(Specio::Constraint::Intersection) = %{version}
Provides:       perl(Specio::Constraint::ObjectCan) = %{version}
Provides:       perl(Specio::Constraint::ObjectDoes) = %{version}
Provides:       perl(Specio::Constraint::ObjectIsa) = %{version}
Provides:       perl(Specio::Constraint::Parameterizable) = %{version}
Provides:       perl(Specio::Constraint::Parameterized) = %{version}
Provides:       perl(Specio::Constraint::Role::CanType) = %{version}
Provides:       perl(Specio::Constraint::Role::DoesType) = %{version}
Provides:       perl(Specio::Constraint::Role::Interface) = %{version}
Provides:       perl(Specio::Constraint::Role::IsaType) = %{version}
Provides:       perl(Specio::Constraint::Simple) = %{version}
Provides:       perl(Specio::Constraint::Structurable) = %{version}
Provides:       perl(Specio::Constraint::Structured) = %{version}
Provides:       perl(Specio::Constraint::Union) = %{version}
Provides:       perl(Specio::Declare) = %{version}
Provides:       perl(Specio::DeclaredAt) = %{version}
Provides:       perl(Specio::Exception) = %{version}
Provides:       perl(Specio::Exporter) = %{version}
Provides:       perl(Specio::Helpers) = %{version}
Provides:       perl(Specio::Library::Builtins) = %{version}
Provides:       perl(Specio::Library::Numeric) = %{version}
Provides:       perl(Specio::Library::Perl) = %{version}
Provides:       perl(Specio::Library::String) = %{version}
Provides:       perl(Specio::Library::Structured) = %{version}
Provides:       perl(Specio::Library::Structured::Dict) = %{version}
Provides:       perl(Specio::Library::Structured::Map) = %{version}
Provides:       perl(Specio::Library::Structured::Tuple) = %{version}
Provides:       perl(Specio::OO) = %{version}
Provides:       perl(Specio::PartialDump) = %{version}
Provides:       perl(Specio::Registry) = %{version}
Provides:       perl(Specio::Role::Inlinable) = %{version}
Provides:       perl(Specio::Subs) = %{version}
Provides:       perl(Specio::TypeChecks) = %{version}
Provides:       perl(Test::Specio) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Ref::Util) >= 0.112
Recommends:     perl(Sub::Util) >= 1.40
%{perl_requires}

%description
The 'Specio' distribution provides classes for representing type
constraints and coercion, along with syntax sugar for declaring them.

Note that this is not a proper type system for Perl. Nothing in this
distribution will magically make the Perl interpreter start checking a
value's type on assignment to a variable. In fact, there's no built-in way
to apply a type to a variable at all.

Instead, you can explicitly check a value against a type, and optionally
coerce values to that type.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md TODO.md
%license LICENSE

%changelog
