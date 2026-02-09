#
# spec file for package perl-Test-Future-IO-Impl
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Test-Future-IO-Impl
Name:           perl-Test-Future-IO-Impl
Version:        0.170.0
Release:        0
# 0.17 -> normalize -> 0.170.0
%define cpan_version 0.17
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Acceptance tests for Future::IO implementations
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.400.400
BuildRequires:  perl(Test2::V0)
Requires:       perl(Test2::V0)
Provides:       perl(Test::Future::IO::Impl) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module contains a collection of acceptance tests for implementations
of Future::IO.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
