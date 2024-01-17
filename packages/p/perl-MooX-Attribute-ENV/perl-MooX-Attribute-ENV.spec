#
# spec file for package perl-MooX-Attribute-ENV
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name MooX-Attribute-ENV
Name:           perl-MooX-Attribute-ENV
Version:        0.04
Release:        0
Summary:        Allow Moo attributes to get their values from %ENV
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Moo)
%{perl_requires}

%description
This is a Moo extension. It allows other attributes for Moo/has. If any of
these are given, then Moo/BUILDARGS is wrapped so that values for object
attributes can, if not supplied in the normal construction process, come
from the environment.

The environment will be searched for either the given case, or upper case,
version of the names discussed below.

When a prefix is mentioned, it will be prepended to the mentioned name,
with a '_' in between.

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
%doc Changes README.md

%changelog
