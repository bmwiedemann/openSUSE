#
# spec file for package perl-Crypt-MySQL
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Crypt-MySQL
Version:        0.04
Release:        0
%define cpan_name Crypt-MySQL
Summary:        Emulate the MySQL PASSWORD() function
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-MySQL/
Source:         http://www.cpan.org/authors/id/I/IK/IKEBE/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Module::Build)
#BuildRequires: perl(Crypt::MySQL)
#BuildRequires: perl(DBD::mysql)
#BuildRequires: perl(DBI)
Requires:       perl(Digest::SHA1)
%{perl_requires}

%description
Crypt::MySQL emulates MySQL PASSWORD() SQL function, without
libmysqlclient. You can compare encrypted passwords, without real MySQL
environment.

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
