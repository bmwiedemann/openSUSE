#
# spec file for package perl-Business-ISSN
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Business-ISSN
Version:        1.003
Release:        0
%define cpan_name Business-ISSN
Summary:        Perl extension for International Standard Serial Numbers
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Business-ISSN/
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
%{perl_requires}

%description
* new($issn)

The constructor accepts a scalar representing the ISSN.

The string representing the ISSN may contain characters other than [0-9xX],
although these will be removed in the internal representation. The
resulting string must look like an ISSN - the first seven characters must
be digits and the eighth character must be a digit, 'x', or 'X'.

The string passed as the ISSN need not be a valid ISSN as long as it
superficially looks like one. This allows one to use the 'fix_checksum'
method.

One should check the validity of the ISSN with 'is_valid()' rather than
relying on the return value of the constructor.

If all one wants to do is check the validity of an ISSN, one can skip the
object-oriented interface and use the c<is_valid_checksum()> function which
is exportable on demand.

If the constructor decides it can't create an object, it returns undef. It
may do this if the string passed as the ISSN can't be munged to the
internal format.

* $obj->checksum

Return the ISSN checksum.

* $obj->as_string

Return the ISSN as a string.

A terminating 'x' is changed to 'X'.

* $obj->is_valid

Returns 1 if the checksum is valid.

Returns 0 if the ISSN does not pass the checksum test. The constructor
accepts invalid ISSN's so that they might be fixed with 'fix_checksum'.

* $obj->fix_checksum

Replace the eighth character with the checksum the corresponds to the
previous seven digits. This does not guarantee that the ISSN corresponds to
the product one thinks it does, or that the ISSN corresponds to any product
at all. It only produces a string that passes the checksum routine. If the
ISSN passed to the constructor was invalid, the error might have been in
any of the other nine positions.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples
%license LICENSE

%changelog
