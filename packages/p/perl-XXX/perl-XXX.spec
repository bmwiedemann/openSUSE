#
# spec file for package perl-XXX
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name XXX
Name:           perl-XXX
Version:        0.380.0
Release:        0
# 0.38 -> normalize -> 0.380.0
%define cpan_version 0.38
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        See Your Data in the Nude
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(YAML::PP) >= 0.018
Requires:       perl(YAML::PP) >= 0.018
Provides:       perl(XXX) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'XXX.pm' exports a function called 'XXX' that you can put just about
anywhere in your Perl code to make it die with a YAML dump of the arguments
to its right.

The charm of XXX-debugging is that it is easy to type, rarely requires
parens and stands out visually so that you remember to remove it.

'XXX.pm' also exports 'WWW', 'YYY' and 'ZZZ' which do similar debugging
things.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
