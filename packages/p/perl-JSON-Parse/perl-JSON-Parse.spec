#
# spec file for package perl-JSON-Parse
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


Name:           perl-JSON-Parse
Version:        0.57
Release:        0
%define cpan_name JSON-Parse
Summary:        Read JSON into a Perl variable
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
A module for parsing JSON. (JSON means "JavaScript Object Notation" and it
is specified in RFC 7159.)

JSON::Parse offers the function parse_json, which takes a string containing
JSON, and returns an equivalent Perl structure. It also offers validation
of JSON via valid_json, which returns true or false depending on whether
the JSON is correct or not, and assert_valid_json, which produces a
descriptive fatal error if the JSON is invalid. A function
json_file_to_perl reads JSON from a file, and there is a safer version of
parse_json called parse_json_safe which doesn't throw exceptions.

For special cases of parsing, there are also methods new and run, which
create a JSON parsing object and run it on text. See METHODS.

JSON::Parse accepts only UTF-8 as input. See UTF-8 only and Handling of
Unicode.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
for file in $(find . -type f); do
    sed -i "s|/home/ben/software/install/bin/perl|%{_bindir}/perl|g; \
            s|/home/ben/projects/Json3/blib/lib|%{perl_vendorarch}|g; \
            s|use lib '/home/ben/projects/Json3/blib/arch';||g;" "$file"
done
# hunspell=`pkg-config --libs hunspell | sed -e 's,-l,,; s,  *,,g'`
# MANUAL END

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
%doc Changes examples README

%changelog
