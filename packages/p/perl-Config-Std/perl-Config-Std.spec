#
# spec file for package perl-Config-Std
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


Name:           perl-Config-Std
Version:        0.903
Release:        0
%define cpan_name Config-Std
Summary:        Load and save configuration files in a standard format
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-Std/
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRICKER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Std)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(TAP::Harness) >= 3.31
BuildRequires:  perl(version)
Requires:       perl(Class::Std)
Requires:       perl(version)
%{perl_requires}

%description
This module implements yet another damn configuration-file system.

The configuration language is deliberately simple and limited, and the
module works hard to preserve as much information (section order, comments,
etc.) as possible when a configuration file is updated.

The whole point of Config::Std is to encourage use of one standard layout
and syntax in config files. Damian says "I could have gotten away with it,
I would have only allowed one separator. But it proved impossible to choose
between ':' and '=' (half the people I asked wanted one, half wanted the
other)." Providing round-trip file re-write is the spoonful of sugar to
help the medicine go down. The supported syntax is within the general INI
file family

See Chapter 19 of "Perl Best Practices" (O'Reilly, 2005) for more detail on
the rationale for this approach.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
