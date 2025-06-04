#
# spec file for package perl-IO-HTML
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


%define cpan_name IO-HTML
Name:           perl-IO-HTML
Version:        1.4.0
Release:        0
# 1.004 -> normalize -> 1.4.0
%define cpan_version 1.004
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Open an HTML file with automatic charset detection
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
Provides:       perl(IO::HTML) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
IO::HTML provides an easy way to open a file containing HTML while
automatically determining its encoding. It uses the HTML5 encoding sniffing
algorithm specified in section 8.2.2.2 of the draft standard.

The algorithm as implemented here is:

* 1.

If the file begins with a byte order mark indicating UTF-16LE, UTF-16BE, or
UTF-8, then that is the encoding.

* 2.

If the first '$bytes_to_check' bytes of the file contain a '<meta>' tag
that indicates the charset, and Encode recognizes the specified charset
name, then that is the encoding. (This portion of the algorithm is
implemented by 'find_charset_in'.)

The '<meta>' tag can be in one of two formats:

  <meta charset="...">
  <meta http-equiv="Content-Type" content="...charset=...">

The search is case-insensitive, and the order of attributes within the tag
is irrelevant. Any additional attributes of the tag are ignored. The first
matching tag with a recognized encoding ends the search.

* 3.

If the first '$bytes_to_check' bytes of the file are valid UTF-8 (with at
least 1 non-ASCII character), then the encoding is UTF-8.

* 4.

If all else fails, use the default character encoding. The HTML5 standard
suggests the default encoding should be locale dependent, but currently it
is always 'cp1252' unless you set '$IO::HTML::default_encoding' to a
different value. Note: 'sniff_encoding' does not apply this step; only
'html_file' does that.

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
%doc Changes examples README
%license LICENSE

%changelog
