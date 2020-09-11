#
# spec file for package perl-YAML-LibYAML-API
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-YAML-LibYAML-API
Version:        0.012
Release:        0
%define cpan_name YAML-LibYAML-API
Summary:        Wrapper around the C libyaml library
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(YAML::PP) >= 0.024
BuildRequires:  perl(YAML::PP::Common)
Requires:       perl(YAML::PP::Common)
%{perl_requires}

%description
This module provides a thin wrapper around the C libyaml API.

Currently it provides functions for parsing and emitting events.

libyaml also provides a loader/dumper API to load/dump YAML into a list of
nodes. There's no wrapper for these functions yet.

This is just one of the first releases. The function names will eventually
be changed.

The sources of 'libyaml-dev' are included in this distribution. You can
build this module with the system libyaml instead, if you remove the
libyaml sources and call 'Makefile.PL' with 'WITH_SYSTEM_LIBYAML=1'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
