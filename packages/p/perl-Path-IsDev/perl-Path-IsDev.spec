#
# spec file for package perl-Path-IsDev
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Path-IsDev
Version:        1.001003
Release:        0
%define cpan_name Path-IsDev
Summary:        Determine if a given Path resembles a development source tree
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Path-IsDev/
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Tiny) >= 0.010
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Path::Tiny) >= 0.004
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
Requires:       perl(Class::Tiny) >= 0.010
Requires:       perl(File::HomeDir)
Requires:       perl(Module::Runtime)
Requires:       perl(Path::Tiny) >= 0.004
Requires:       perl(Role::Tiny)
Requires:       perl(Role::Tiny::With)
Requires:       perl(Sub::Exporter)
Recommends:     perl(Path::Tiny) >= 0.058
%{perl_requires}

%description
This module is more or less a bunch of heuristics for determining if a
given path is a development tree root of some kind.

This has many useful applications, notably ones that require behaviours for
"installed" modules to be different to those that are still "in
development"

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
