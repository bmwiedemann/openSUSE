#
# spec file for package perl-Libssh-Session
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


%define cpan_name Libssh-Session
Name:           perl-Libssh-Session
Version:        1.100.0
Release:        0
# 1.1 -> normalize -> 1.100.0
%define cpan_version 1.1
#Upstream:  This library is licensed under the Apache License 2.0. Details of this license can be found within the 'LICENSE' text file
License:        Apache-2.0
Summary:        Perl interface for libssh
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Q/QG/QGARNIER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Libssh::Session) = %{version}
Provides:       perl(Libssh::Sftp) = %{version}
%undefine       __perllib_provides
Recommends:     perl(ExtUtils::PkgConfig)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libssh-devel
# MANUAL END

%description
'Libssh::Session' is a perl interface to the libssh (http://www.libssh.org)
library. It doesn't support all the library. It's working in progress.

Right now, you can authenticate and execute commands on a SSH server.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README README.md TODO
%license LICENSE

%changelog
