#
# spec file for package perl-Config-Grammar
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Config-Grammar
Version:        1.13
Release:        0
%define cpan_name Config-Grammar
Summary:        Grammar-based, user-friendly config parser
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSCHWEI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Config::Grammar is a module to parse configuration files. The optional
second parameter to the parse() method can be used to specify the file
encoding to use for opening the file (see documentation for Perl's use open
pragma).

The configuration may consist of multiple-level sections with assignments
and tabular data. The parsed data will be returned as a hash containing the
whole configuration. Config::Grammar uses a grammar that is supplied upon
creation of a Config::Grammar object to parse the configuration file and
return helpful error messages in case of syntax errors. Using the *makepod*
method you can generate documentation of the configuration file format.

The *maketmpl* method can generate a template configuration file. If your
grammar contains regexp matches, the template will not be all that helpful
as Config::Grammar is not smart enough to give you sensible template data
based in regular expressions. The related function *maketmplmin* generates
a minimal configuration template without examples, regexps or comments and
thus allows an experienced user to fill in the configuration data more
efficiently.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
