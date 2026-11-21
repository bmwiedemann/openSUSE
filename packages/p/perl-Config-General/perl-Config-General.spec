#
# spec file for package perl-Config-General
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Config-General
Name:           perl-Config-General
Version:        2.690.0
Release:        0
# 2.69 -> normalize -> 2.690.0
%define cpan_version 2.69
License:        Artistic-2.0
Summary:        Generic Config Module
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TL/TLINDEN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Config::General) = %{version}
Provides:       perl(Config::General::Extended) = 2.70.0
Provides:       perl(Config::General::Interpolated) = 2.160.0
%undefine       __perllib_provides
%{perl_requires}

%description
This module opens a config file and parses its contents for you. The *new*
method requires one parameter which needs to be a filename. The method
*getall* returns a hash which contains all options and its associated
values of your config file.

The format of config files supported by *Config::General* is inspired by
the well known Apache config format, in fact, this module is 100%
compatible to Apache configs, but you can also just use simple name/value
pairs in your config files.

In addition to the capabilities of an Apache config file it supports some
enhancements such as here-documents, C-style comments or multiline options.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changelog README

%changelog
