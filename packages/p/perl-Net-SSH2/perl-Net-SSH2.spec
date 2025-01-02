#
# spec file for package perl-Net-SSH2
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Net-SSH2
Name:           perl-Net-SSH2
Version:        0.740.0
Release:        0
# 0.74 -> normalize -> 0.740.0
%define cpan_version 0.74
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Support for the SSH 2 protocol via libssh2
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
Provides:       perl(Net::SSH2) = %{version}
Provides:       perl(Net::SSH2::Channel)
Provides:       perl(Net::SSH2::Dir)
Provides:       perl(Net::SSH2::File)
Provides:       perl(Net::SSH2::KnownHosts)
Provides:       perl(Net::SSH2::Listener)
Provides:       perl(Net::SSH2::PublicKey)
Provides:       perl(Net::SSH2::SFTP)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libgcrypt-devel
BuildRequires:  libssh2-devel
BuildRequires:  openssl-devel
# MANUAL END

%description
Net::SSH2 is a Perl interface to the libssh2 (http://www.libssh2.org)
library. It supports the SSH2 protocol (there is no support for SSH1) with
all of the key exchanges, ciphers, and compression of libssh2.

Even if the module can be compiled and linked against very old versions of
the library, nothing below 1.5.0 should really be used (older versions were
quite buggy and unreliable) and version 1.7.0 or later is recommended.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes const-c.inc const-xs.inc example

%changelog
