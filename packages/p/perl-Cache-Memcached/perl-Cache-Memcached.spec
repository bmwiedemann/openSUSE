#
# spec file for package perl-Cache-Memcached
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


%define cpan_name Cache-Memcached
Name:           perl-Cache-Memcached
Version:        1.300.0
Release:        0
# 1.30 -> normalize -> 1.300.0
%define cpan_version 1.30
#Upstream:  You may distribute under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file.
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Client library for memcached (memory cache daemon)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(String::CRC32)
Requires:       perl(String::CRC32)
Provides:       perl(Cache::Memcached) = %{version}
Provides:       perl(Cache::Memcached::GetParser)
%undefine       __perllib_provides
%{perl_requires}

%description
This is the Perl API for memcached, a distributed memory cache daemon. More
information is available at:

  http://www.danga.com/memcached/

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
%doc ChangeLog README TODO

%changelog
