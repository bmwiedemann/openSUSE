#
# spec file for package perl-IO-Handle-Util
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-IO-Handle-Util
Version:        0.02
Release:        0
%define cpan_name IO-Handle-Util
Summary:        Functions for working with L<IO::Handle> like objects
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(asa)
BuildRequires:  perl(autodie)
BuildRequires:  perl(ok)
BuildRequires:  perl(parent)
Requires:       perl(IO::String)
Requires:       perl(Sub::Exporter)
Requires:       perl(asa)
Requires:       perl(autodie)
Requires:       perl(parent)
%{perl_requires}

%description
This module provides a number of helpful routines to manipulate or create
IO::Handle like objects.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENCE README

%changelog
