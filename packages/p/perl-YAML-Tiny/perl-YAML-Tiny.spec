#
# spec file for package perl-YAML-Tiny
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


Name:           perl-YAML-Tiny
Version:        1.73
Release:        0
%define cpan_name YAML-Tiny
Summary:        Read/Write YAML files with as little code as possible
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/YAML-Tiny/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.88
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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
