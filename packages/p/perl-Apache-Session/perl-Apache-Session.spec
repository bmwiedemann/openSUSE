#
# spec file for package perl-Apache-Session
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


%define cpan_name Apache-Session
Name:           perl-Apache-Session
Version:        1.940.0
Release:        0
# 1.94 -> normalize -> 1.940.0
%define cpan_version 1.94
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Persistence framework for session data
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Deep) >= 0.82
BuildRequires:  perl(Test::Exception) >= 0.15
Provides:       perl(Apache::Session) = %{version}
Provides:       perl(Apache::Session::DB_File) = 1.10.0
Provides:       perl(Apache::Session::File) = 1.540.0
Provides:       perl(Apache::Session::Flex) = 1.10.0
Provides:       perl(Apache::Session::Generate::MD5) = 2.120.0
Provides:       perl(Apache::Session::Generate::ModUniqueId) = 0.20.0
Provides:       perl(Apache::Session::Generate::ModUsertrack) = 0.20.0
Provides:       perl(Apache::Session::Informix) = 1.10.0
Provides:       perl(Apache::Session::Lock::File) = 1.40.0
Provides:       perl(Apache::Session::Lock::MySQL) = 1.10.0
Provides:       perl(Apache::Session::Lock::Null) = 1.10.0
Provides:       perl(Apache::Session::Lock::Semaphore) = 1.40.0
Provides:       perl(Apache::Session::Lock::Sybase) = 1.0.0
Provides:       perl(Apache::Session::MySQL) = 1.10.0
Provides:       perl(Apache::Session::MySQL::NoLock) = 0.10.0
Provides:       perl(Apache::Session::Oracle) = 1.10.0
Provides:       perl(Apache::Session::Postgres) = 1.10.0
Provides:       perl(Apache::Session::Serialize::Base64) = 1.10.0
Provides:       perl(Apache::Session::Serialize::Storable) = 1.10.0
Provides:       perl(Apache::Session::Serialize::Sybase) = 1.0.0
Provides:       perl(Apache::Session::Serialize::UUEncode) = 1.10.0
Provides:       perl(Apache::Session::Store::DBI) = 1.20.0
Provides:       perl(Apache::Session::Store::DB_File) = 1.10.0
Provides:       perl(Apache::Session::Store::File) = 1.40.0
Provides:       perl(Apache::Session::Store::Informix) = 1.20.0
Provides:       perl(Apache::Session::Store::MySQL) = 1.40.0
Provides:       perl(Apache::Session::Store::Oracle) = 1.100.0
Provides:       perl(Apache::Session::Store::Postgres) = 1.30.0
Provides:       perl(Apache::Session::Store::Sybase) = 1.10.0
Provides:       perl(Apache::Session::Sybase) = 1.0.0
%undefine       __perllib_provides
%{perl_requires}

%description
Apache::Session is a persistence framework which is particularly useful for
tracking session data between httpd requests. Apache::Session is designed
to work with Apache and mod_perl, but it should work under CGI and other
web servers, and it also works outside of a web server altogether.

Apache::Session consists of five components: the interface, the object
store, the lock manager, the ID generator, and the serializer. The
interface is defined in Session.pm, which is meant to be easily subclassed.
The object store can be the filesystem, a Berkeley DB, a MySQL DB, an
Oracle DB, a Postgres DB, Sybase, or Informix. Locking is done by lock
files, semaphores, or the locking capabilities of the various databases.
Serialization is done via Storable, and optionally ASCII-fied via MIME or
pack(). ID numbers are generated via MD5. The reader is encouraged to
extend these capabilities to meet his own requirements.

A derived class of Apache::Session is used to tie together the three
following components. The derived class inherits the interface from
Apache::Session, and specifies which store and locker classes to use.
Apache::Session::MySQL, for instance, uses the MySQL storage class and also
the MySQL locking class. You can easily plug in your own object store or
locker class.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES Contributing.txt README TODO

%changelog
