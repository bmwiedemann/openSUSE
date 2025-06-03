#
# spec file for package perl-Authen-DecHpwd
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


%define cpan_name Authen-DecHpwd
Name:           perl-Authen-DecHpwd
Version:        2.7.0
Release:        0
# 2.007 -> normalize -> 2.7.0
%define cpan_version 2.007
#Upstream: GPL-1.0-or-later
License:        GPL-2.0-or-later
Summary:        DEC VMS password hashing
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Integer) >= 0.3
BuildRequires:  perl(Digest::CRC) >= 0.140
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::String)
BuildRequires:  perl(parent)
Requires:       perl(Data::Integer) >= 0.3
Requires:       perl(Digest::CRC) >= 0.140
Requires:       perl(Scalar::String)
Requires:       perl(parent)
Provides:       perl(Authen::DecHpwd) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module implements the 'SYS$HASH_PASSWORD' password hashing function
from VMS (also known as 'LGI$HPWD'), and some associated VMS username and
password handling functions.

The password hashing function is implemented in XS, with a hideously slow
pure Perl backup version for systems that can't handle XS.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
