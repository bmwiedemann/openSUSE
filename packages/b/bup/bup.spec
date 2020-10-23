#
# spec file for package bup
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

%define with_test 0
Name:           bup
Version:        0.31
Release:        0
Summary:        Backup program based on git
License:        LGPL-2.0-only
Group:          Productivity/Archiving/Backup
URL:            https://bup.github.io/
Source0:        https://github.com/bup/bup/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         %{name}-python.patch
BuildRequires:  git-core >= 1.5.3.1
BuildRequires:  pandoc
BuildRequires:  perl-Time-HiRes
BuildRequires:  python3-devel
BuildRequires:  python3-fuse
BuildRequires:  python3-pylibacl
BuildRequires:  python3-pyxattr
BuildRequires:  python3-tornado
%if %{with_test}
BuildRequires:  rsync
%endif
Requires:       git-core >= 1.5.3.1
Requires:       par2
Requires:       python3
Requires:       python3-fuse
Requires:       python3-pylibacl
Requires:       python3-pyxattr
Requires:       python3-tornado

%description
Very efficient backup system based on the git packfile format,
providing fast incremental saves and global deduplication
(among and within files, including virtual machine images).

%prep
%setup -q
%patch1 -p1
# rpmlint: fix incorrect-fsf-address
find . -type f | xargs sed -i -e 's:59 Temple Place\, Suite 330\, Boston\, MA  02111-1307  USA:51 Franklin Street\, Fifth Floor\, Boston\, MA 02110-1301 USA:g'
# fix binpath
sed -i -e "s|PREFIX=%{_prefix}/local|PREFIX=/usr|g" Makefile
# fix docpath
sed -i -e "s|/share/doc/bup|/share/doc/packages/bup|g" Makefile
# fix env-script-interpreter
sed -i -e "s|\/usr\/bin\/env bash|\/bin\/bash|g" cmd/import-rdiff-backup-cmd.sh
# rpmlint
find -type f -name ".gitignore" -exec rm {} \;

%build
# FIXME: you should use the %%configure macro
# With macro %%configure package will not build.
./configure
%make_build PYTHON=python

%install
%if 0%{!?make_install:1}
%define make_install make install 'DESTDIR=%{buildroot}'
%endif
%make_install PYTHON=python

%check
%if %{with_test}
make check
%endif

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_docdir}/%{name}/
%dir %{_prefix}/lib/%{name}/
%dir %{_prefix}/lib/%{name}/bup/
%dir %{_prefix}/lib/%{name}/cmd/
%dir %{_prefix}/lib/%{name}/web/
%dir %{_prefix}/lib/%{name}/web/static/
%{_prefix}/lib/%{name}/bup/*
%{_prefix}/lib/%{name}/cmd/*
%{_prefix}/lib/%{name}/web/*
%{_prefix}/lib/%{name}/web/static/*
%{_mandir}/man1/*

%changelog
