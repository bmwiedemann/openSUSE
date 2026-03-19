#
# spec file for package cgit
#
# Copyright (c) 2024 SUSE LLC
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


%define         git_version 2.53.0
Name:           cgit
Version:        1.3
Release:        0
Summary:        A web frontend for git repositories
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            http://git.zx2c4.com/cgit/
#Git-Clone:	https://git.zx2c4.com/cgit
Source:         https://git.zx2c4.com/cgit/snapshot/%name-%version.tar.xz
Source3:        https://www.kernel.org/pub/software/scm/git/git-%git_version.tar.xz
Source4:        https://www.kernel.org/pub/software/scm/git/git-%git_version.tar.sign
Source8:        %name.keyring
Source9:        cgitrc
# Requirements for cgitrc man page generation
BuildRequires:  asciidoc
# Requirements for cgit
BuildRequires:  libxslt
BuildRequires:  xz
BuildRequires:  nginx
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
Provides:       bundled(git) = %git_version

%description
A web interface for the Git SCM, using a built-in cache to decrease server
I/O pressure.

%prep
%autosetup -a3
rm -rf git
ln -s git-%git_version git

perl -i -pe 's{^#!%_bindir/env }{#!%_bindir/}g' filters/email-gravatar.py \
	filters/html-converters/md2html filters/syntax-highlighting.py

%build
%make_build

%install
b="%buildroot"
%make_install V=1 prefix="%_prefix" CGIT_SCRIPT_PATH="/srv/www/htdocs/cgit" install-man
mkdir -p "$b/srv/www/cgi-bin/%name" "$b/var/cache/%name" "$b/%_sysconfdir"
mv -v "$b/srv/www/htdocs/%name/%name.cgi" "$b/srv/www/cgi-bin/%name/%name.cgi"
cp -av "%_sourcedir/cgitrc" "$b/%_sysconfdir/"

%files
%license COPYING
%doc README
%_mandir/man5/cgitrc.5%ext_man
%dir /srv/www
%dir /srv/www/cgi-bin
%dir /srv/www/htdocs
/srv/www/cgi-bin/cgit/
/srv/www/htdocs/cgit/
%_prefix/lib/cgit/
%attr(0750,wwwrun,www) /var/cache/cgit/
%config(noreplace) %_sysconfdir/cgitrc

%changelog
