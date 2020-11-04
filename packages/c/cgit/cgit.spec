#
# spec file for package cgit
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define git_version	2.25.1
Name:           cgit
Version:        1.2.3
Release:        0
Summary:        A web frontend for git repositories
License:        GPL-2.0
Group:          Development/Tools/Version Control
Url:            http://git.zx2c4.com/cgit/
#Git-Clone:	https://git.zx2c4.com/cgit
Source:         https://git.zx2c4.com/cgit/snapshot/%name-%version.tar.xz
Source2:        https://www.kernel.org/pub/software/scm/git/git-%git_version.tar.xz
Source3:        https://www.kernel.org/pub/software/scm/git/git-%git_version.tar.sign
Source4:        %name.keyring
Source9:        cgitrc
# Requirements for cgitrc man page generation
BuildRequires:  asciidoc
# Requirements for cgit
BuildRequires:  libopenssl-devel
BuildRequires:  libxslt
BuildRequires:  libzip-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %_tmppath/%name-%version-build
Provides:       bundled(git) = %version

%description
A web interface for the Git SCM, using a built-in cache to decrease server
I/O pressure.

%prep
%setup -qa2
rm -rf git
ln -s git-%git_version git

%build
perl -i -pe 's{^#!/usr/bin/env }{#!/usr/bin/}g' filters/email-gravatar.py \
	filters/html-converters/md2html filters/syntax-highlighting.py
make V=1 prefix="%_prefix" CFLAGS="%optflags" %{?_smp_mflags} all

%install
%make_install V=1 prefix="%_prefix" CFLAGS="%optflags" \
	CGIT_SCRIPT_PATH="/srv/www/htdocs/cgit" install-man
b="%buildroot"
mkdir -p "$b/srv/www/cgi-bin/cgit/" "$b/var/cache/cgit"
mv $b/srv/www/htdocs/cgit/cgit.cgi $b/srv/www/cgi-bin/cgit/cgit.cgi
mkdir -p "$b/%_sysconfdir"
cp "%_sourcedir/cgitrc" "$b/%_sysconfdir/"

%files
%defattr(-,root,root)
%doc README COPYING
%_mandir/man5/cgitrc.5%ext_man
/srv/www/cgi-bin/cgit/
/srv/www/htdocs/cgit/
%_prefix/lib/cgit/
%attr(0750,wwwrun,www) /var/cache/cgit/
%config(noreplace) %_sysconfdir/cgitrc

%changelog
