#
# spec file for package perl-Test-Mojo-Pg
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


Name:           perl-Test-Mojo-Pg
Version:        0.33
Release:        0
%define cpan_name Test-Mojo-Pg
Summary:        Helper for Dealing with Pg During Tests
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Mojo-Pg/
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RICHE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Pg)
Requires:       perl(Mojo::Base)
Requires:       perl(Mojo::Pg)
%{perl_requires}

%description
Test::Mojo::Pg makes the creation and removal of a transitory database
during testing when using Mojo::Pg. This is useful when every test should
work from a 'clean' database.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc README.md
%license LICENSE

%changelog
