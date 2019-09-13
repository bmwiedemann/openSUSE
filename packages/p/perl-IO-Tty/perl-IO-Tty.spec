#
# spec file for package perl-IO-Tty
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


Name:           perl-IO-Tty
Version:        1.12
Release:        0
%define cpan_name IO-Tty
Summary:        Low-level allocate a pseudo-Tty, import constants.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Tty/
Source:         http://www.cpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'IO::Tty' is used internally by 'IO::Pty' to create a pseudo-tty. You
wouldn't want to use it directly except to import constants, use 'IO::Pty'.
For a list of importable constants, see the IO::Tty::Constant manpage.

Windows is now supported, but ONLY under the Cygwin environment, see the
http://sources.redhat.com/cygwin/ manpage.

Please note that pty creation is very system-dependend. From my experience,
any modern POSIX system should be fine. Find below a list of systems that
'IO::Tty' should work on. A more detailed table (which is slowly getting
out-of-date) is available from the project pages document manager at
SourceForge the http://sourceforge.net/projects/expectperl/ manpage.

If you have problems on your system and your system is listed in the
"verified" list, you probably have some non-standard setup, e.g. you
compiled your Linux-kernel yourself and disabled ptys (bummer!). Please ask
your friendly sysadmin for help.

If your system is not listed, unpack the latest version of 'IO::Tty', do a
''perl Makefile.PL; make; make test; uname -a'' and send me
(_RGiersig@cpan.org_) the results and I'll see what I can deduce from that.
There are chances that it will work right out-of-the-box...

If it's working on your system, please send me a short note with details
(version number, distribution, etc. 'uname -a' and 'perl -V' is a good
start; also, the output from "perl Makefile.PL" contains a lot of
interesting info, so please include that as well) so I can get an overview.
Thanks!

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog README try

%changelog
