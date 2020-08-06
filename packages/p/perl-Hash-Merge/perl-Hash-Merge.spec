#
# spec file for package perl-Hash-Merge
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


Name:           perl-Hash-Merge
Version:        0.302
Release:        0
%define cpan_name Hash-Merge
Summary:        Merges arbitrarily deep hashes into a single hash
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HE/HERMES/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone::Choose) >= 0.008
BuildRequires:  perl(Test::More) >= 0.9
Requires:       perl(Clone::Choose) >= 0.008
%{perl_requires}

%description
Hash::Merge merges two arbitrarily deep hashes into a single hash. That is,
at any level, it will add non-conflicting key-value pairs from one hash to
the other, and follows a set of specific rules when there are key value
conflicts (as outlined below). The hash is followed recursively, so that
deeply nested hashes that are at the same level will be merged when the
parent hashes are merged. *Please note that self-referencing hashes, or
recursive references, are not handled well by this method.*

Values in hashes are considered to be either ARRAY references, HASH
references, or otherwise are treated as SCALARs. By default, the data
passed to the merge function will be cloned using the Clone module;
however, if necessary, this behavior can be changed to use as many of the
original values as possible. (See 'set_clone_behavior').

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes MAINTAINER.md README.md

%changelog
