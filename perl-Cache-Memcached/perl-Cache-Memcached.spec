#
# spec file for package perl-Cache-Memcached
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


Name:           perl-Cache-Memcached
Version:        1.30
Release:        0
#Upstream:  You may distribute under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file.
%define cpan_name Cache-Memcached
Summary:        Client Library for Memcached (Memory Cache Daemon)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Cache-Memcached/
Source0:        http://www.cpan.org/authors/id/D/DO/DORMANDO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(String::CRC32)
Requires:       perl(String::CRC32)
%{perl_requires}

%description
This is the Perl API for memcached, a distributed memory cache daemon. More
information is available at:

  http://www.danga.com/memcached/

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
%doc ChangeLog README TODO

%changelog
