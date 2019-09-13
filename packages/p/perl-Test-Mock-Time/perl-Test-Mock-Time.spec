#
# spec file for package perl-Test-Mock-Time
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Test-Mock-Time
Version:        0.1.7
Release:        0
%define cpan_name Test-Mock-Time
Summary:        Deterministic time & timers for event loop tests
License:        MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Mock-Time/
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POWERMAN/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Export::Attrs)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Export::Attrs)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Test::MockModule)
%{perl_requires}

%description
This module replaces actual time with simulated time everywhere (core
time(), Time::HiRes, EV, AnyEvent with EV, Mojolicious, …) and provide a
way to write deterministic tests for event loop based applications with
timers.

*IMPORTANT!* This module *must* be loaded by your script/app/test before
other related modules (Time::HiRes, Mojolicious, EV, etc.).

%prep
%setup -q -n %{cpan_name}-v%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
