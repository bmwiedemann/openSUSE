#
# spec file for package perl-Tie-Cache
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Tie-Cache
Version:        0.21
Release:        0
%define cpan_name Tie-Cache
Summary:        LRU Cache in Memory
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Tie-Cache/
Source:         http://www.cpan.org/authors/id/C/CH/CHAMAS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module implements a least recently used (LRU) cache in memory through
a tie interface. Any time data is stored in the tied hash, that key/value
pair has an entry time associated with it, and as the cache fills up, those
members of the cache that are the oldest are removed to make room for new
entries.

So, the cache only "remembers" the last written entries, up to the size of
the cache. This can be especially useful if you access great amounts of
data, but only access a minority of the data a majority of the time.

The implementation is a hash, for quick lookups, overlaying a doubly linked
list for quick insertion and deletion. On a WinNT PII 300, writes to the
hash were done at a rate 3100 per second, and reads from the hash at 6300
per second. Work has been done to optimize refreshing cache entries that
are frequently read from, code like $cache{entry}, which moves the entry to
the end of the linked list internally.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc CHANGES README

%changelog
