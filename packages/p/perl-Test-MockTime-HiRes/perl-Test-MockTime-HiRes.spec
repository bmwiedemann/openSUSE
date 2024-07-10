#
# spec file for package perl-Test-MockTime-HiRes
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


%define cpan_name Test-MockTime-HiRes
Name:           perl-Test-MockTime-HiRes
Version:        0.08
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Replaces actual time with simulated high resolution time
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TA/TARAO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::Requires)
Requires:       perl(Test::MockTime)
%{perl_requires}

%description
'Test::MockTime::HiRes' is a Time::HiRes compatible version of
Test::MockTime. You can wait milliseconds in simulated time.

It also provides 'mock_time' to restrict the effect of the simulation in a
code block.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
