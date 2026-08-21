#
# spec file for package perl-Socket-MsgHdr
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Socket-MsgHdr
Name:           perl-Socket-MsgHdr
Version:        0.60.0
Release:        0
# 0.06 -> normalize -> 0.60.0
%define cpan_version 0.06
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Sendmsg, recvmsg and ancillary data operations
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FELIPE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Socket::MsgHdr) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Socket::MsgHdr provides advanced socket messaging operations via sendmsg
and recvmsg. Like their C counterparts, these functions accept few
parameters, instead stuffing a lot of information into a complex structure.

This structure describes the message sent or received (buf), the peer on
the other end of the socket (name), and ancillary or so-called control
information (cmsghdr). This ancillary data may be used for file descriptor
passing, IPv6 operations, and a host of implemenation-specific extensions.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
