#
# spec file for package perl-Sub-Exporter-Progressive
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


Name:           perl-Sub-Exporter-Progressive
Version:        0.001013
Release:        0
%define cpan_name Sub-Exporter-Progressive
Summary:        Only use Sub::Exporter if you need it
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sub-Exporter-Progressive/
Source0:        http://www.cpan.org/authors/id/F/FR/FREW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
Sub::Exporter is an incredibly powerful module, but with that power comes
great responsibility, er- as well as some runtime penalties. This module is
a 'Sub::Exporter' wrapper that will let your users just use Exporter if all
they are doing is picking exports, but use 'Sub::Exporter' if your users
try to use 'Sub::Exporter''s more advanced features, like renaming exports,
if they try to use them.

Note that this module will export '@EXPORT', '@EXPORT_OK' and
'%EXPORT_TAGS' package variables for 'Exporter' to work. Additionally, if
your package uses advanced 'Sub::Exporter' features like currying, this
module will only ever use 'Sub::Exporter', so you might as well use it
directly.

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
%doc Changes LICENSE README

%changelog
