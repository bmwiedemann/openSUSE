#
# spec file for package perl-CSS-Tiny
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


%define cpan_name CSS-Tiny
Name:           perl-CSS-Tiny
Version:        1.200.0
Release:        0
# 1.20 -> normalize -> 1.200.0
%define cpan_version 1.20
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Read/Write .css files with as little code as possible
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(CSS::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'CSS::Tiny' is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead. CSS.pm
requires about 2.6 meg or ram to load, which is a large amount of overhead
if you only want to do trivial things. Memory usage is normally scoffed at
in Perl, but in my opinion should be at least kept in mind.

This module is primarily for reading and writing simple files, and anything
we write shouldn't need to have documentation/comments. If you need
something with more power, move up to CSS.pm. With the increasing
complexity of CSS, this is becoming more common, but many situations can
still live with simple CSS files.

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
%doc Changes test.css

%changelog
