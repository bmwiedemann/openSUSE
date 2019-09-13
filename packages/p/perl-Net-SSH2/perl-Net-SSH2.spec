#
# spec file for package perl-Net-SSH2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-SSH2
Version:        0.70
Release:        0
%define cpan_name Net-SSH2
Summary:        Support for the SSH 2 protocol via libssh2
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc BUILDING.WIN32 Changes const-c.inc const-xs.inc example README

%changelog
