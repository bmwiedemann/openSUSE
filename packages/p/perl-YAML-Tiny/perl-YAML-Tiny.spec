#
# spec file for package perl-YAML-Tiny
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name YAML-Tiny
Name:           perl-YAML-Tiny
Version:        1.760.0
Release:        0
# 1.76 -> normalize -> 1.760.0
%define cpan_version 1.76
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Read/Write YAML files with as little code as possible
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.88
Provides:       perl(YAML::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
*YAML::Tiny* is a perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and memory
overhead.

Most of the time it is accepted that Perl applications use a lot of memory
and modules. The *::Tiny* family of modules is specifically intended to
provide an ultralight and zero-dependency alternative to many more-thorough
standard modules.

This module is primarily for reading human-written files (like simple
config files) and generating very simple human-readable files. Note that I
said *human-readable* and not *geek-readable*. The sort of files that your
average manager or secretary should be able to look at and make sense of.

YAML::Tiny does not generate comments, it won't necessarily preserve the
order of your hashes, and it will normalise if reading in and writing out
again.

It only supports a very basic subset of the full YAML specification.

Usage is targeted at files like Perl's META.yml, for which a small and
easily-embeddable module is extremely attractive.

Features will only be added if they are human readable, and can be written
in a few lines of code. Please don't be offended if your request is
refused. Someone has to draw the line, and for YAML::Tiny that someone is
me.

If you need something with more power move up to YAML (7 megabytes of
memory overhead) or YAML::XS (6 megabytes memory overhead and requires a C
compiler).

To restate, YAML::Tiny does *not* preserve your comments, whitespace, or
the order of your YAML data. But it should round-trip from Perl structure
to file and back again just fine.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
