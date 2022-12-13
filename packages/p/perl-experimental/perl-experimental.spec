#
# spec file for package perl-experimental
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name experimental
Name:           perl-experimental
Version:        0.030
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Experimental features made easy
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(version)
Requires:       perl(version)
%{perl_requires}

%description
This pragma provides an easy and convenient way to enable or disable
experimental features.

Every version of perl has some number of features present but considered
"experimental." For much of the life of Perl 5, this was only a designation
found in the documentation. Starting in Perl v5.10.0, and more aggressively
in v5.18.0, experimental features were placed behind pragmata used to
enable the feature and disable associated warnings.

The 'experimental' pragma exists to combine the required incantations into
a single interface stable across releases of perl. For every experimental
feature, this should enable the feature and silence warnings for the
enclosing lexical scope:

  use experimental 'feature-name';

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%license LICENSE

%changelog
