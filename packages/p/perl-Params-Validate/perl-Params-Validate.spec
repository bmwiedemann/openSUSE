#
# spec file for package perl-Params-Validate
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Params-Validate
Version:        1.30
Release:        0
%define cpan_name Params-Validate
Summary:        Validate method/function parameters
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.422700
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
Requires:       perl(Module::Implementation)
%{perl_requires}

%description
*I would recommend you consider using Params::ValidationCompiler instead.
That module, despite being pure Perl, is _significantly_ faster than this
one, at the cost of having to adopt a type system such as Specio,
Type::Tiny, or the one shipped with Moose*.

This module allows you to validate method or function call parameters to an
arbitrary level of specificity. At the simplest level, it is capable of
validating the required parameters were given and that no unspecified
additional parameters were passed in.

It is also capable of determining that a parameter is of a specific type,
that it is an object of a certain class hierarchy, that it possesses
certain methods, or applying validation callbacks to arguments.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md TODO
%license LICENSE

%changelog
