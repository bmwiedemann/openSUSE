#
# spec file for package perl-Socket6
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


%define cpan_name Socket6
Name:           perl-Socket6
Version:        0.28
Release:        0
Summary:        IPv6 Sockets (Perl Module)
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Socket6/
Source:         http://www.cpan.org/authors/id/U/UM/UMEMOTO/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The IPv6 related part of the C socket.h defines and structure
manipulators.

%prep
%setup -q -n Socket6-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%{perl_vendorarch}/auto/Socket6
%{perl_vendorarch}/Socket6.pm
%{_mandir}/man3/Socket6.3pm%{ext_man}
%doc MANIFEST README ChangeLog

%changelog
