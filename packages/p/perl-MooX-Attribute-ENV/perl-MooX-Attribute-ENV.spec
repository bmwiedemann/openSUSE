#
# spec file for package perl-MooX-Attribute-ENV
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooX-Attribute-ENV
Version:        0.02
Release:        0
%define cpan_name MooX-Attribute-ENV
Summary:        Allow Moo attributes to get their values from %ENV
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::Exception) >= 0.420000
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Moo)
%{perl_requires}

%description
This is a Moo extension. It allows other attributes for Moo/has. If any of
these are given, then instead of the normal value-setting "chain" for
attributes of given, default; the chain will be given, environment,
default.

The environment will be searched for either the given case, or upper case,
version of the names discussed below.

When a prefix is mentioned, it will be prepended to the mentioned name,
with a '_' in between.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md

%changelog
