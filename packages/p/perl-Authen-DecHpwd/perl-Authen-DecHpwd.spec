#
# spec file for package perl-Authen-DecHpwd
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


Name:           perl-Authen-DecHpwd
Version:        2.007
Release:        0
#Upstream: GPL-1.0+
%define cpan_name Authen-DecHpwd
Summary:        DEC VMS password hashing
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Authen-DecHpwd/
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Integer) >= 0.003
BuildRequires:  perl(Digest::CRC) >= 0.14
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::String)
BuildRequires:  perl(parent)
Requires:       perl(Data::Integer) >= 0.003
Requires:       perl(Digest::CRC) >= 0.14
Requires:       perl(Scalar::String)
Requires:       perl(parent)
%{perl_requires}

%description
This module implements the 'SYS$HASH_PASSWORD' password hashing function
from VMS (also known as 'LGI$HPWD'), and some associated VMS username and
password handling functions.

The password hashing function is implemented in XS, with a hideously slow
pure Perl backup version for systems that can't handle XS.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
