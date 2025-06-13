#
# spec file for package perl-MooX-Types-MooseLike
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


%define cpan_name MooX-Types-MooseLike
Name:           perl-MooX-Types-MooseLike
Version:        0.290.0
Release:        0
# 0.29 -> normalize -> 0.290.0
%define cpan_version 0.29
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Some Moosish types and a type builder
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATEU/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Runtime) >= 0.14
BuildRequires:  perl(Moo) >= 1.004002
BuildRequires:  perl(Test::Fatal) >= 0.3
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Module::Runtime) >= 0.14
Provides:       perl(MooX::Types::MooseLike) = %{version}
Provides:       perl(MooX::Types::MooseLike::Base) = %{version}
%undefine       __perllib_provides
Recommends:     perl(strictures) >= 2
%{perl_requires}

%description
This module provides a possibility to build your own set of Moose-like
types. These custom types can then be used to describe fields in Moo-based
classes.

See MooX::Types::MooseLike::Base for a list of available base types. Its
source also provides an example of how to build base types, along with both
parameterizable and non-parameterizable.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
