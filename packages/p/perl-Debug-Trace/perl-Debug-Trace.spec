#
# spec file for package perl-Debug-Trace
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Debug-Trace
Version:        0.05
Release:        0
%define cpan_name Debug-Trace
Summary:        Perl extension to trace subroutine calls
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Debug-Trace/
Source:         http://www.cpan.org/authors/id/J/JV/JV/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Debug::Trace)
%{perl_requires}

%description
Debug::Trace instruments subroutines to provide tracing information upon
every call and return.

Using Debug::Trace does not require any changes to your sources. Most
often, it will be used from the command line:

  perl -MDebug::Trace=foo,bar yourprogram.pl

This will have your subroutines foo() and bar() printing call and return
information.

Subroutine names may be fully qualified to denote subroutines in other
packages than the default main::.

By default, the trace information is output using the standard warn()
function.

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
