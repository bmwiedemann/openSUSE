#
# spec file for package perl-File-Flock
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


Name:           perl-File-Flock
Version:        2014.01
Release:        0
#Upstream:  same terms as Perl itself.
%define cpan_name File-Flock
Summary:        File Locking with Flock
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Flock/
Source0:        http://www.cpan.org/authors/id/M/MU/MUIR/modules/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Data::Structure::Util)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(IO::Event) >= 0.812
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::SharedFork)
Requires:       perl(AnyEvent)
Requires:       perl(Data::Structure::Util)
Requires:       perl(File::Slurp)
Requires:       perl(IO::Event) >= 0.812
Requires:       perl(Test::SharedFork)
%{perl_requires}

%description
Lock files using the flock() call. If the file to be locked does not exist,
then the file is created. If the file was created then it will be removed
when it is unlocked assuming it's still an empty file.

Locks can be created by new'ing a *File::Flock* object. Such locks are
automatically removed when the object goes out of scope. The *unlock()*
method may also be used.

*lock_rename()* is used to tell File::Flock when a file has been renamed
(and thus the internal locking data that is stored based on the filename
should be moved to a new name). *unlock()* the new name rather than the
original name.

Locks are released on process exit when the process that created the lock
exits. Subprocesses that exit do not remove locks. Use forget_locks() or
POSIX::_exit() to prevent unlocking on process exit.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes README

%changelog
