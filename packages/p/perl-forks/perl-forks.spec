#
# spec file for package perl-forks
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


%define cpan_name forks
Name:           perl-forks
Version:        0.36
Release:        0
Summary:        Drop-in replacement for Perl threads using fork()
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/forks/
Source:         http://www.cpan.org/authors/id/R/RY/RYBSKEJ/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Acme::Damn)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(List::MoreUtils) >= 0.15
BuildRequires:  perl(Sys::SigAction) >= 0.11
Requires:       perl(Acme::Damn)
Requires:       perl(Devel::Symdump)
Requires:       perl(List::MoreUtils) >= 0.15
Requires:       perl(Sys::SigAction) >= 0.11
%{perl_requires}

%description
The "forks" pragma allows a developer to use threads without having to have
a threaded perl, or to even run 5.8.0 or higher.

Refer to the the threads manpage module for ithreads API documentation.
Also, use

    perl -Mforks -e 'print $threads::VERSION'

to see what version of the threads manpage you should refer to regarding
supported API features.

There were a number of goals that I am trying to reach with this
implementation.

    Using this module *only* makes sense if you run on a system that has an
    implementation of the 'fork' function by the Operating System. Windows
    is currently the only known system on which Perl runs which does *not*
    have an implementation of 'fork'. Therefore, it *doesn't* make any
    sense to use this module on a Windows system. And therefore, a check is
    made during installation barring you from installing on a Windows
    system.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CREDITS MANIFEST.skip README TODO

%changelog
