#
# spec file for package clusterssh
#
# Copyright (c) 2020 SUSE LLC
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


Name:           clusterssh
%define dullver 4.16
Version:        4.16
Release:        0
Summary:        Multiplex SSH sessions onto many hosts using multiple terminals
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Networking/SSH
URL:            https://github.com/duncs/clusterssh/wiki
Source:         https://github.com/duncs/clusterssh/archive/v%dullver.tar.gz
Source2:        %name-rpmlintrc
Patch1:         perl_shebang.patch
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Changes)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(X11::Protocol)
BuildRequires:  perl(X11::Protocol::WM)
Requires:       perl(CPAN::Changes)
Requires:       perl(Carp)
Requires:       perl(English)
Requires:       perl(Exception::Class)
Requires:       perl(Exception::Class)
Requires:       perl(Fcntl)
Requires:       perl(File::Basename)
Requires:       perl(File::Path)
Requires:       perl(File::Slurp)
Requires:       perl(File::Temp)
Requires:       perl(File::Temp)
Requires:       perl(File::Which)
Requires:       perl(File::Which)
Requires:       perl(FindBin)
Requires:       perl(Getopt::Long)
Requires:       perl(Getopt::Long)
Requires:       perl(Locale::Maketext)
Requires:       perl(Locale::Maketext)
Requires:       perl(Module::Build)
Requires:       perl(Net::hostent)
Requires:       perl(POSIX)
Requires:       perl(Pod::Usage)
Requires:       perl(Readonly)
Requires:       perl(Readonly)
Requires:       perl(Socket)
Requires:       perl(Sort::Naturally)
Requires:       perl(Sys::Hostname)
Requires:       perl(Test::Differences)
# Test::PerlTidy not available atm
# Requires:       perl(Test::PerlTidy)
Requires:       xorg-x11-fonts-100dpi
Requires:       xorg-x11-fonts-75dpi
Requires:       xterm
Requires:       perl(Test::Pod)
Requires:       perl(Test::Pod::Coverage)
Requires:       perl(Test::Trap)
Requires:       perl(Tk)
Requires:       perl(Tk::ROText)
Requires:       perl(Tk::Xlib)
Requires:       perl(Try::Tiny)
Requires:       perl(X11::Keysyms)
Requires:       perl(X11::Protocol)
Requires:       perl(X11::Protocol::Constants)
Requires:       perl(X11::Protocol::WM)
%perl_requires

%description
Cluster SSH opens terminal windows with connections to specified
hosts and an administration console. Any text typed into the
administration console is replicated to all other connected and
active windows. This tool is intended for, but not limited to,
cluster administration where the same configuration or commands must
be run on each node within the cluster. Performing these commands all
at once via this tool ensures all nodes are kept in sync.

%prep
%autosetup -n %name-%dullver -p1

%build
perl Build.PL installdirs=vendor
./Build

%check
# rm t/changes.t

# Readme is not in the tarball
# couldn't open README for reading: No such file or directory at t/boilerplate.t line 9.
rm t/boilerplate.t

./Build test

%install
./Build install destdir="%buildroot" create_packlist=0
%perl_gen_filelist

install -D -m 0644 %buildroot/%_bindir/clusterssh_bash_completion.dist \
        %buildroot/%_datadir/bash-completion/completions/clusterssh
rm %buildroot/%_bindir/clusterssh_bash_completion.dist

%files
%doc AUTHORS Changes THANKS TODO
%_bindir/c*
%_datadir/bash-completion/
%_mandir/man1/*
%_mandir/man3/*
%perl_vendorlib/*

%changelog
