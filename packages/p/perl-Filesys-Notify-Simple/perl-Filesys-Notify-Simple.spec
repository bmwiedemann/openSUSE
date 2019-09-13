#
# spec file for package perl-Filesys-Notify-Simple
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Filesys-Notify-Simple
Version:        0.13
Release:        0
%define cpan_name Filesys-Notify-Simple
Summary:        Simple and dumb file system watcher
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Filesys-Notify-Simple/
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::SharedFork)
%{perl_requires}

%description
Filesys::Notify::Simple is a simple but unified interface to get
notifications of changes to a given filesystem path. It utilizes inotify2
on Linux, fsevents on OS X, kqueue on FreeBSD and
FindFirstChangeNotification on Windows if they're installed, with a
fallback to the full directory scan if they're not available.

There are some limitations in this module. If you don't like it, use
File::ChangeNotify.

  * There is no file name based filter. Do it in your own code.

  * You can not get types of events (created, updated, deleted).

  * Currently 'wait' method blocks.

In return, this module doesn't depend on any non-core modules. Platform
specific optimizations with Linux::Inotify2, Mac::FSEvents,
Filesys::Notify::KQueue and Win32::ChangeNotify are truely optional.

NOTE: Using Win32::ChangeNotify may put additional limitations.

  * Win32::ChangeNotify uses FindFirstChangeNotificationA so that Unicode
characters can not be handled. On cygwin (1.7 or later), Unicode characters
should be able to be handled when Win32::ChangeNotify is not used.

  * If more than 64 directories are included under the specified paths, an
error occurrs.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
