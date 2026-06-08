#
# spec file for package perl-Hash-Case
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Hash-Case
Name:           perl-Hash-Case
Version:        1.70.0
Release:        0
# 1.07 -> normalize -> 1.70.0
%define cpan_version 1.07
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Play trics with HASH keys
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1
Provides:       perl(Hash::Case) = %{version}
Provides:       perl(Hash::Case::Lower) = %{version}
Provides:       perl(Hash::Case::Preserve) = %{version}
Provides:       perl(Hash::Case::Upper) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Hash::Case is the base class for various classes which tie special
treatment for the casing of keys. Be aware of the differences in
implementation: 'Lower' and 'Upper' are tied native hashes: these hashes
have no need for hidden fields or other assisting data structured. A case
'Preserve' hash will actually create three hashes.

The following strategies are implemented:

* * Hash::Case::Lower (native hash)

Keys are always considered lower case. The internals of this module
translate any incoming key to lower case before it is used.

* * Hash::Case::Upper (native hash)

Like the ::Lower, but then all keys are always translated into upper case.
This module can be of use for some databases, which do translate everything
to capitals as well. To avoid confusion, you may want to have you own
internal Perl hash do this as well.

* * Hash::Case::Preserve

The actual casing is ignored, but not forgotten.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc ChangeLog README README.md

%changelog
