#
# spec file for package perl-MooseX-Workers
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


Name:           perl-MooseX-Workers
Version:        0.24
Release:        0
%define cpan_name MooseX-Workers
Summary:        Simple sub-process management for asynchronous tasks
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Workers/
Source:         http://www.cpan.org/authors/id/R/RK/RKITOVER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Reference)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(POE)
Requires:       perl(POE::Wheel::Run)
Requires:       perl(Package::Stash)
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
MooseX::Workers is a Role that provides easy delegation of long-running
tasks into a managed child process. Process management is taken care of via
POE and its POE::Wheel::Run module.

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
%doc Changes doc LICENSE README

%changelog
