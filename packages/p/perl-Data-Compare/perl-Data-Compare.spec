#
# spec file for package perl-Data-Compare
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Data-Compare
Name:           perl-Data-Compare
Version:        1.28
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Compare perl data structures
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone) >= 0.43
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.48
BuildRequires:  perl(File::Find::Rule) >= 0.1
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Clone) >= 0.43
Requires:       perl(File::Find::Rule) >= 0.1
Requires:       perl(Test::More) >= 0.88
%{perl_requires}

%description
Compare two perl data structures recursively. Returns 0 if the structures
differ, else returns 1.

A few data types are treated as special cases:

* Scalar::Properties objects

This has been moved into a plugin, although functionality remains the same
as with the previous version. Full documentation is in
Data::Compare::Plugins::Scalar::Properties.

* Compiled regular expressions, eg qr/foo/

These are stringified before comparison, so the following will match:

    $r = qr/abc/i;
    $s = qr/abc/i;
    Compare($r, $s);

and the following won't, despite them matching *exactly* the same text:

    $r = qr/abc/i;
    $s = qr/[aA][bB][cC]/;
    Compare($r, $s);

Sorry, that's the best we can do.

* CODE and GLOB references

These are assumed not to match unless the references are identical - ie,
both are references to the same thing.

You may also customise how we compare structures by supplying options in a
hashref as a third parameter to the 'Compare()' function. This is not yet
available through the OO-ish interface. These options will be in force for
the *whole* of your comparison, so will apply to structures that are
lurking deep down in your data as well as at the top level, so beware!

* ignore_hash_keys

an arrayref of strings. When comparing two hashes, any keys mentioned in
this list will be ignored.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc CHANGELOG MAINTAINERS-NOTE NOTES README
%license ARTISTIC.txt GPL2.txt

%changelog
