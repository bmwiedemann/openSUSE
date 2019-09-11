#
# spec file for package perl-Apache-Session
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Apache-Session
Version:        1.93
Release:        0
%define cpan_name Apache-Session
Summary:        A persistence framework for session data
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Apache-Session/
Source:         http://www.cpan.org/authors/id/C/CH/CHORNY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Deep) >= 0.082
BuildRequires:  perl(Test::Exception) >= 0.15
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc b CHANGES Contributing.txt eg README TODO

%changelog
