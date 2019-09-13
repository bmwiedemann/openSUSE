#
# spec file for package perl-Cache-Cache
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


Name:           perl-Cache-Cache
Version:        1.08
Release:        0
#Upstream: CHECK(GPL-1.0+ or Artistic-1.0)
%define cpan_name Cache-Cache
Summary:        The Cache Interface
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Cache-Cache/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA1) >= 2.02
BuildRequires:  perl(Error) >= 0.15
BuildRequires:  perl(IPC::ShareLite) >= 0.09
Requires:       perl(Digest::SHA1) >= 2.02
Requires:       perl(Error) >= 0.15
Requires:       perl(IPC::ShareLite) >= 0.09
%{perl_requires}

%description
The Cache modules are designed to assist a developer in persisting data for
a specified period of time. Often these modules are used in web
applications to store data locally to save repeated and redundant expensive
calls to remote machines or databases. People have also been known to use
Cache::Cache for its straightforward interface in sharing data between runs
of an application or invocations of a CGI-style script or simply as an easy
to use abstraction of the filesystem or shared memory.

The Cache::Cache interface is implemented by classes that support the get,
set, remove, size, purge, and clear instance methods and their
corresponding static methods for persisting data across method calls.

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
%doc CHANGES COPYING CREDITS DISCLAIMER README STYLE

%changelog
