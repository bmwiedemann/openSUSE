#
# spec file for package perl-IO-Tty
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name IO-Tty
Name:           perl-IO-Tty
Version:        1.310.0
Release:        0
# 1.31 -> normalize -> 1.310.0
%define cpan_version 1.31
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Pseudo ttys and constants
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(IO::Pty) = %{version}
Provides:       perl(IO::Tty) = %{version}
Provides:       perl(IO::Tty::Constant) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'IO::Tty' is used internally by IO::Pty to create a pseudo-tty. You
wouldn't want to use it directly except to import constants, use IO::Pty.
For a list of importable constants, see IO::Tty::Constant.

Windows is now supported under the Cygwin environment, see
http://cygwin.com/.

Please note that pty creation is very system-dependent. Any modern POSIX
system should be fine. The test suite is run via GitHub Actions CI on
Linux, macOS, FreeBSD, OpenBSD, and NetBSD.

If you have problems on your system and it is listed below, you probably
have a non-standard setup, e.g. you compiled your Linux-kernel yourself and
disabled ptys (bummer!). Please ask your friendly sysadmin for help.

If your system is not listed, unpack the latest version of 'IO::Tty', do a
''perl Makefile.PL; make; make test; uname -a'' and report issues at
https://github.com/cpan-authors/IO-Tty/issues.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc AI_POLICY.md ChangeLog CONTRIBUTING.md README.md SECURITY.md try
%license LICENSE

%changelog
