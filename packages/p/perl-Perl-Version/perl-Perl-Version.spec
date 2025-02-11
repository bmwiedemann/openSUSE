#
# spec file for package perl-Perl-Version
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


%define cpan_name Perl-Version
Name:           perl-Perl-Version
Version:        1.18.0
Release:        0
# 1.018 -> normalize -> 1.18.0
%define cpan_version 1.018
License:        Artistic-2.0
Summary:        Parse and manipulate Perl version strings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::More) >= 1
Provides:       perl(Perl::Version) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Perl::Version provides a simple interface for parsing, manipulating and
formatting Perl version strings.

Unlike version.pm (which concentrates on parsing and comparing version
strings) Perl::Version is designed for cases where you'd like to parse a
version, modify it and get back the modified version formatted like the
original.

For example:

    my $version = Perl::Version->new( '1.2.3' );
    $version->inc_version;
    print "$version\n";

prints

    1.3.0

whereas

    my $version = Perl::Version->new( 'v1.02.03' );
    $version->inc_version;
    print "$version\n";

prints

    v1.03.00

Both are representations of the same version and they'd compare equal but
their formatting is different.

Perl::Version tries hard to guess and recreate the format of the original
version and in most cases it succeeds. In rare cases the formatting is
ambiguous. Consider

    1.10.03

Do you suppose that second component '10' is zero padded like the third
component? Perl::Version will assume that it is:

    my $version = Perl::Version->new( '1.10.03' );
    $version->inc_revision;
    print "$version\n";

will print

    2.00.00

If all of the components after the first are the same length (two
characters in this case) and any of them begins with a zero Perl::Version
will assume that they're all zero padded to the same length.

The first component and any alpha suffix are handled separately. In each
case if either of them starts with a zero they will be zero padded to the
same length when stringifying the version.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples Notes.txt SECURITY.md
%license LICENSE

%changelog
