#
# spec file for package rash
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


Name:           rash
Version:        0.2
Release:        0
Summary:        The Reckless rAcket SHell
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Shells
URL:            https://rash-lang.org
Source0:        https://github.com/willghatch/racket-rash/archive/v%{version}/racket-rash-%{version}.tar.gz
Source1:        https://github.com/willghatch/racket-udelim/archive/master/racket-udelim-master.tar.gz
Source2:        https://github.com/Metaxal/text-table/archive/master/racket-text-table-master.tar.gz
Source3:        https://github.com/willghatch/racket-basedir/archive/master/racket-basedir-master.tar.gz
Source4:        rash-rpmlintrc
BuildRequires:  ca-certificates
BuildRequires:  libedit0
BuildRequires:  libsqlite3-0
BuildRequires:  racket-devel
BuildRequires:  racket-doc
Requires:       libedit0
Requires:       libsqlite3-0
Requires:       racket
Recommends:     racket-doc
Requires(post): racket
Requires(preun): racket
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rash is a shell language, library, and REPL(Read–Eval–Print-Loop) for Racket.

Use as a REPL that is as convenient for pipelining programs as Bash is, but
has all the power of Racket. Use as a scripting language with #lang rash.
Embed in normal Racket files with (require rash), and mix freely with any
other Racket language or library.

Rash is in active development, but it is largely stable (and the parts that
are not are marked as such). It can be used as an interactive shell.  It
currently lacks the interactive polish of Zsh or Fish, but it is so much
better as a language.

%prep
%setup -q -n racket-rash-%{version}
tar -xf %{S:1} && mv racket-udelim-master udelim
tar -xf %{S:2} && mv text-table-master text-table
tar -xf %{S:3} && mv racket-basedir-master basedir

%build

%install
export HOME=$PWD/root
for pkg in udelim text-table shell-pipeline linea basedir rash
do
    pushd $pkg
    raco pkg install --binary --batch --auto --user
    popd
done
find -name .gitignore -print -delete
mkdir -p %{buildroot}%{_datadir}/racket/pkgs
cp -a udelim text-table shell-pipeline linea basedir rash \
	%{buildroot}%{_datadir}/racket/pkgs
for pkg in udelim text-table shell-pipeline linea basedir
do
    test -e $pkg/README.md || continue
    mv $pkg/README.md $pkg/README.$pkg
done
mv README.md README.rash

(cat > rash.c)<<-'EOF'
	#include <stdlib.h>
	#include <unistd.h>
	int main (int argc, char **argv, char *envp[])
	{
	    char **nargv = (char**)malloc((sizeof(char *))*(argc+6));
	    int n = 0, i;

	    nargv[n++] = argv[0];
	    nargv[n++] = "-N";
	    nargv[n++] = argv[0];
	    nargv[n++] = "-l-";
	    nargv[n++] = "rash/repl.rkt";
	    for (i=1; i<=argc; i++)
	        nargv[n++] = argv[i];
	    nargv[n] = NULL;

	    execve("%{_bindir}/racket", nargv, envp);
	}
	EOF
mkdir -p %{buildroot}%{_bindir}
gcc %{optflags} -g3 -o %{buildroot}%{_bindir}/rash rash.c
%if 0%{?suse_version} < 1550
mkdir -p %{buildroot}/bin
ln -sf %{_bindir}/rash %{buildroot}/bin/rash
%endif

%post
for pkg in udelim text-table shell-pipeline linea basedir rash
do
    raco pkg install --link --installation --batch --auto --no-setup %{_datadir}/racket/pkgs/$pkg || :
done

%preun
for pkg in rash basedir linea shell-pipeline text-table udelim
do
    raco pkg remove --force --installation --batch --auto --no-trash --no-setup $pkg || :
done

%files
%defattr(-,root,root)
%license LICENSE
%doc README.rash */README.*
%if 0%{?suse_version} < 1550
/bin/rash
%endif
%{_bindir}/rash
%{_datadir}/racket/pkgs

%changelog
