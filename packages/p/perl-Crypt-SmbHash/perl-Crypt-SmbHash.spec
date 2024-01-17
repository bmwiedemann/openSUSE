#
# spec file for package perl-Crypt-SmbHash
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


Name:           perl-Crypt-SmbHash
Version:        0.12
Release:        0
Summary:        perl module Crypt::SmbHash
License:        Artistic-1.0 OR GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/perldoc?Crypt::SmbHash
Source:         http://search.cpan.org/CPAN/authors/id/B/BJ/BJKUIT/Crypt-SmbHash-%{version}.tar.gz
BuildRequires:  perl-Digest-MD4
BuildRequires:  perl-macros
Requires:       perl-Digest-MD4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
This module provides functions to generate LM/NT hashes as used by
Samba

%prep
%setup -n Crypt-SmbHash-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-, root, root)
%doc Changes MANIFEST README

%changelog
