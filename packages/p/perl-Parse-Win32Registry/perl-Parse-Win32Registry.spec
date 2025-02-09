#
# spec file for package perl-Parse-Win32Registry
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


%define cpan_name Parse-Win32Registry
Name:           perl-Parse-Win32Registry
Version:        1.100.0
Release:        0
# 1.1 -> normalize -> 1.100.0
%define cpan_version 1.1
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse Windows Registry Files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMACFARLA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Parse::Win32Registry) = %{version}
Provides:       perl(Parse::Win32Registry::ACE)
Provides:       perl(Parse::Win32Registry::ACL)
Provides:       perl(Parse::Win32Registry::Base)
Provides:       perl(Parse::Win32Registry::Entry)
Provides:       perl(Parse::Win32Registry::File)
Provides:       perl(Parse::Win32Registry::GUID)
Provides:       perl(Parse::Win32Registry::Iterator)
Provides:       perl(Parse::Win32Registry::Key)
Provides:       perl(Parse::Win32Registry::SID)
Provides:       perl(Parse::Win32Registry::SecurityDescriptor)
Provides:       perl(Parse::Win32Registry::Value)
Provides:       perl(Parse::Win32Registry::Win95::File)
Provides:       perl(Parse::Win32Registry::Win95::Key)
Provides:       perl(Parse::Win32Registry::Win95::RGDB)
Provides:       perl(Parse::Win32Registry::Win95::RGDBKey)
Provides:       perl(Parse::Win32Registry::Win95::RGKN)
Provides:       perl(Parse::Win32Registry::Win95::Value)
Provides:       perl(Parse::Win32Registry::WinNT::Entry)
Provides:       perl(Parse::Win32Registry::WinNT::File)
Provides:       perl(Parse::Win32Registry::WinNT::Hbin)
Provides:       perl(Parse::Win32Registry::WinNT::Key)
Provides:       perl(Parse::Win32Registry::WinNT::Security)
Provides:       perl(Parse::Win32Registry::WinNT::Value)
%undefine       __perllib_provides
%{perl_requires}

%description
Parse::Win32Registry is a module for parsing Windows Registry files,
allowing you to read the keys and values of a registry file without going
through the Windows API.

It provides an object-oriented interface to the keys and values in a
registry file. Registry files are structured as trees of keys, with each
key containing further subkeys or values.

The module is intended to be cross-platform, and run on those platforms
where Perl will run.

It supports both Windows NT registry files (Windows NT, 2000, XP, 2003,
Vista, 7) and Windows 95 registry files (Windows 95, 98, Millennium
Edition).

It is intended to be used to parse offline registry files. If a registry
file is currently in use, you will not be able to open it. However, you can
save part or all of a currently loaded registry file using the Windows reg
command if you have the appropriate administrative access.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
