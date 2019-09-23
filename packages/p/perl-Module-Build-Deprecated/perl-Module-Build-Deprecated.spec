#
# spec file for package perl-Module-Build-Deprecated
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


Name:           perl-Module-Build-Deprecated
Version:        0.4210
Release:        0
%define cpan_name Module-Build-Deprecated
Summary:        Collection of Modules Removed From Module-Build
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Build-Deprecated/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.002
BuildRequires:  perl(Module::Build) >= 0.360100
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(parent)
BuildRequires:  perl(version) >= 0.87
Requires:       perl(CPAN::Meta::YAML) >= 0.002
Requires:       perl(Module::Metadata)
Requires:       perl(parent)
Requires:       perl(version) >= 0.87
%{perl_requires}

%description
This module contains a number of module that have been removed from
Module-Build:

* * Module::Build::ModuleInfo

This has been superceded by Module::Metadata

* * Module::Build::Version

This has been replaced by version

* * Module::Build::YAML

This has been replaced by CPAN::Meta::YAML

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
