#
# spec file for package perl-Data-Dump
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


%define cpan_name Data-Dump
Name:           perl-Data-Dump
Version:        1.25
Release:        0
Summary:        Pretty printing of data structures
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides a few functions that traverse their argument list and
return a string containing Perl code that, when 'eval'ed, produces a deep
copy of the original arguments.

The main feature of the module is that it strives to produce output that is
easy to read. Example:

    @a = (1, [2, 3], {4 => 5});
    dump(@a);

Produces:

    "(1, [2, 3], { 4 => 5 })"

If you dump just a little data, it is output on a single line. If you dump
data that is more complex or there is a lot of it, line breaks are
automatically added to keep it easy to read.

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
