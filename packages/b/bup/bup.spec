#
# spec file for package bup
#
# Copyright (c) 2025 SUSE LLC
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
%if 0%{?suse_version} < 1600
%define pythons python311
%endif
Name:           bup
Version:        0.33.7
Release:        0
Summary:        Backup program based on git
License:        LGPL-2.0-only
Group:          Productivity/Archiving/Backup
URL:            https://bup.github.io/
Source0:        https://github.com/bup/bup/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  git-core >= 1.5.6
%ifnarch %ix86
BuildRequires:  pandoc
%endif
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module fuse}
BuildRequires:  %{python_module pylibacl}
BuildRequires:  %{python_module pyxattr}
BuildRequires:  %{python_module tornado}
BuildRequires:  perl(Time::HiRes)
%if %{with_test}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  rsync
%endif
Requires:       %{python_flavor}
Requires:       %{python_flavor}-fuse
Requires:       %{python_flavor}-pylibacl
Requires:       %{python_flavor}-pyxattr
Requires:       %{python_flavor}-tornado
Requires:       git-core >= 1.5.6
Requires:       par2

%description
Very efficient backup system based on the git packfile format,
providing fast incremental saves and global deduplication
(among and within files, including virtual machine images).

%prep
%autosetup -p1
# fix binpath
sed -i -e "s|PREFIX=/usr/local|PREFIX=%{_prefix}|g" GNUmakefile
# fix docpath
sed -i -e "s|/share/doc/bup|/share/doc/packages/bup|g" GNUmakefile
# fix env-script-interpreter
sed -i -e "s|\/usr\/bin\/env bash|\/bin\/bash|g" lib/cmd/bup-import-rdiff-backup
# rpmlint
find -type f -name ".gitignore" -exec rm {} \;

%build
# FIXME: you should use the %%configure macro
# With macro %%configure package will not build.
./configure
%make_build

%install
%if 0%{!?make_install:1}
%define make_install make install 'DESTDIR=%{buildroot}'
%endif
%make_install

%check
%if %{with_test}
make check
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_prefix}/lib/%{name}/
%dir %{_prefix}/lib/%{name}/bup/
%dir %{_prefix}/lib/%{name}/cmd/
%dir %{_prefix}/lib/%{name}/web/
%dir %{_prefix}/lib/%{name}/web/static/
%{_prefix}/lib/%{name}/bup/*
%{_prefix}/lib/%{name}/cmd/*
%{_prefix}/lib/%{name}/web/*
%{_prefix}/lib/%{name}/web/static/*
%ifnarch %ix86
%{_docdir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/man5/*
%endif

%changelog
