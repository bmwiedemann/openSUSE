#
# spec file for package perl-Session-Token
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Session-Token
Version:        1.503
Release:        0
%define cpan_name Session-Token
Summary:        Secure, efficient, simple random session token generation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Session-Token/
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FRACTAL/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Session::Token) = %{version}
%{perl_requires}

%description
This module provides a secure, efficient, and simple interface for creating
session tokens, password reset codes, temporary passwords, random
identifiers, and anything else you can think of.

When a Session::Token object is created, 1024 bytes are read from
'/dev/urandom' (Linux, Solaris, most BSDs), '/dev/arandom' (some older
BSDs), or Crypt::Random::Source::Strong::Win32 (Windows). These bytes are
used to seed the at http://www.burtleburtle.net/bob/rand/isaacafa.html
pseudo random number generator.

Once a generator is created, you can repeatedly call the 'get' method on
the generator object and it will return a new token each time.

*IMPORTANT*: If your application calls 'fork', make sure that any
generators are re-created in one of the processes after the fork since
forking will duplicate the generator state and both parent and child
processes will go on to produce identical tokens (just like perl's rand
after it is seeded).

After the generator context is created, no system calls are used to
generate tokens. This is one way that Session::Token helps with efficiency.
However, this is only important for certain use cases (generally not web
sessions).

ISAAC is a cryptographically secure PRNG that improves on the well-known
RC4 algorithm in some important areas. For instance, it doesn't have short
cycles or initial bias like RC4 does. A theoretical shortest possible cycle
in ISAAC is '2**40', although no cycles this short have ever been found
(and probably don't exist at all). On average, ISAAC cycles are '2**8295'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
%license COPYING

%changelog
