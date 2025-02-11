#
# spec file for package perl-Any-Moose
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


%define cpan_name Any-Moose
Name:           perl-Any-Moose
Version:        0.270.0
Release:        0
# 0.27 -> normalize -> 0.270.0
%define cpan_version 0.27
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        (DEPRECATED) use Moo instead!
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mouse) >= 0.400
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Mouse) >= 0.400
Provides:       perl(Any::Moose) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
(DEPRECATED) use Moo instead!

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
