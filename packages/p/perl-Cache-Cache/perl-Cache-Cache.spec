#
# spec file for package perl-Cache-Cache
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Cache-Cache
Name:           perl-Cache-Cache
Version:        1.80.0
Release:        0
# 1.08 -> normalize -> 1.80.0
%define cpan_version 1.08
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        The Cache interface
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA1) >= 2.20
BuildRequires:  perl(Error) >= 0.15
BuildRequires:  perl(IPC::ShareLite) >= 0.90
Requires:       perl(Digest::SHA1) >= 2.20
Requires:       perl(Error) >= 0.15
Requires:       perl(IPC::ShareLite) >= 0.90
Provides:       perl(Cache::BaseCache)
Provides:       perl(Cache::BaseCacheTester)
Provides:       perl(Cache::Cache) = %{version}
Provides:       perl(Cache::CacheMetaData)
Provides:       perl(Cache::CacheSizer)
Provides:       perl(Cache::CacheTester)
Provides:       perl(Cache::CacheUtils)
Provides:       perl(Cache::FileBackend)
Provides:       perl(Cache::FileCache)
Provides:       perl(Cache::MemoryBackend)
Provides:       perl(Cache::MemoryCache)
Provides:       perl(Cache::NullCache)
Provides:       perl(Cache::Object)
Provides:       perl(Cache::SharedMemoryBackend)
Provides:       perl(Cache::SharedMemoryCache)
Provides:       perl(Cache::SizeAwareCache)
Provides:       perl(Cache::SizeAwareCacheTester)
Provides:       perl(Cache::SizeAwareFileCache)
Provides:       perl(Cache::SizeAwareMemoryCache)
Provides:       perl(Cache::SizeAwareSharedMemoryCache)
%undefine       __perllib_provides
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES CREDITS DISCLAIMER README STYLE
%license COPYING

%changelog
