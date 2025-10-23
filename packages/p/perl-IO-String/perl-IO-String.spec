#
# spec file for package perl-IO-String
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


%define cpan_name IO-String
Name:           perl-IO-String
Version:        1.80.0
Release:        0
# 1.08 -> normalize -> 1.80.0
%define cpan_version 1.08
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Emulate file interface for in-core strings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(IO::String) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The 'IO::String' module provides the 'IO::File' interface for in-core
strings. An 'IO::String' object can be attached to a string, and makes it
possible to use the normal file operations for reading or writing data, as
well as for seeking to various locations of the string. This is useful when
you want to use a library module that only provides an interface to file
handles on data that you have in a string variable.

Note that perl-5.8 and better has built-in support for "in memory" files,
which are set up by passing a reference instead of a filename to the open()
call. The reason for using this module is that it makes the code backwards
compatible with older versions of Perl.

The 'IO::String' module provides an interface compatible with 'IO::File' as
distributed with _IO-1.20_, but the following methods are not available:
new_from_fd, fdopen, format_write, format_page_number,
format_lines_per_page, format_lines_left, format_name, format_top_name.

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

%changelog
