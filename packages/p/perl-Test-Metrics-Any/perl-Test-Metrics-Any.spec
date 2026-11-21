#
# spec file for package perl-Test-Metrics-Any
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


%define cpan_name Test-Metrics-Any
Name:           perl-Test-Metrics-Any
Version:        0.20.0
Release:        0
# 0.02 -> normalize -> 0.20.0
%define cpan_version 0.02
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Assert that code produces metrics via Metrics::Any
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Metrics::Any::Adapter)
BuildRequires:  perl(Metrics::Any::Adapter::Test)
BuildRequires:  perl(Module::Build) >= 0.400.400
BuildRequires:  perl(Test2::V0)
Requires:       perl(Metrics::Any::Adapter)
Requires:       perl(Metrics::Any::Adapter::Test)
Provides:       perl(Test::Metrics::Any) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This test module helps write unit tests which assert that the code under
test reports metrics via Metrics::Any.

Loading this module automatically sets the Metrics::Any::Adapter type to
'Test'.

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
