#
# spec file for package perl-Import-Into
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Import-Into
Version:        1.002005
Release:        0
%define cpan_name Import-Into
Summary:        Import packages into other packages
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Import-Into/
Source0:        http://www.cpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Runtime)
Requires:       perl(Module::Runtime)
%{perl_requires}

%description
Writing exporters is a pain. Some use the Exporter manpage, some use the
Sub::Exporter manpage, some use the Moose::Exporter manpage, some use the
Exporter::Declare manpage ... and some things are pragmas.

Exporting on someone else's behalf is harder. The exporters don't provide a
consistent API for this, and pragmas need to have their import method
called directly, since they effect the current unit of compilation.

'Import::Into' provides global methods to make this painless.

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
