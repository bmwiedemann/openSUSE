#
# spec file for package perl-Config-General
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Config-General
Version:        2.63
Release:        0
%define cpan_name Config-General
Summary:        Generic Config Module
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-General/
Source0:        http://www.cpan.org/authors/id/T/TL/TLINDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changelog README

%changelog
