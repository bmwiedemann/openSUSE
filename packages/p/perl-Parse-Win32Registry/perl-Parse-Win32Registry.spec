#
# spec file for package perl-Parse-Win32Registry
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Parse-Win32Registry
Version:        1.1
Release:        0
%define cpan_name Parse-Win32Registry
Summary:        Parse Windows Registry Files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMACFARLA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
