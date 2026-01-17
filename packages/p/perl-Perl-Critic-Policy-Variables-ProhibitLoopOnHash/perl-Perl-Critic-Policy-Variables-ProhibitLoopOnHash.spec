#
# spec file for package perl-Perl-Critic-Policy-Variables-ProhibitLoopOnHash
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


%define cpan_name Perl-Critic-Policy-Variables-ProhibitLoopOnHash
Name:           perl-Perl-Critic-Policy-Variables-ProhibitLoopOnHash
Version:        0.9.0
Release:        0
# 0.009 -> normalize -> 0.9.0
%define cpan_version 0.009
License:        MIT
Summary:        Don't write loops on hashes, only on keys and values of hashes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Perl::Critic) >= 1.126
BuildRequires:  perl(parent)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Perl::Critic) >= 1.126
Requires:       perl(parent)
Provides:       perl(Perl::Critic::Policy::Variables::ProhibitLoopOnHash) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
When "looping over hashes," we mean looping over hash keys or hash values.
If you forgot to call 'keys' or 'values' you will accidentally loop over
both.

    foreach my $foo (%hash) {...}        # not ok
    action() for %hash;                  # not ok
    foreach my $foo ( keys %hash ) {...} # ok
    action() for values %hash;           # ok

An effort is made to detect expressions:

    action() for %hash ? keys %hash : ();                             # ok
    action() for %{ $hash{'stuff'} } ? keys %{ $hash{'stuff'} } : (); # ok

(Granted, the second example there doesn't make much sense, but I have
found a variation of it in real code.)

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
%doc Changes README
%license LICENSE

%changelog
