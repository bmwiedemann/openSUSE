#
# spec file for package perl-Config-Any
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Config-Any
Version:        0.32
Release:        0
%define cpan_name Config-Any
Summary:        Load configuration from different file formats, transparently
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-Any/
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Pluggable::Object) >= 3.6
Requires:       perl(Module::Pluggable::Object) >= 3.6
%{perl_requires}

%description
Config::Any provides a facility for Perl applications and libraries to load
configuration data from multiple different file formats. It supports XML,
YAML, JSON, Apache-style configuration, Windows INI files, and even Perl
code.

The rationale for this module is as follows: Perl programs are deployed on
many different platforms and integrated with many different systems.
Systems administrators and end users may prefer different configuration
formats than the developers. The flexibility inherent in a multiple format
configuration loader allows different users to make different choices,
without generating extra work for the developers. As a developer you only
need to learn a single interface to be able to use the power of different
configuration formats.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
