#
# spec file for package rdiff-backup
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 B1 Systems GmbH, Vohburg, Germany
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
Name:           rdiff-backup
Version:        2.2.0
Release:        0
Summary:        Convenient and transparent local/remote incremental mirror/backup
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://rdiff-backup.net/
Source0:        https://github.com/rdiff-backup/rdiff-backup/releases/download/v%{version}/rdiff-backup-%{version}.tar.gz
#
BuildRequires:  librsync-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  rubygem(asciidoctor)
Recommends:     python3-pylibacl
Recommends:     python3-xattr

%description
rdiff-backup backs up one directory to another, possibly over a
network. The target directory ends up a copy of the source directory,
but extra reverse diffs are stored in a special subdirectory of that
target directory, so you can still recover files lost some time ago.
The idea is to combine the best features of a mirror and an incremental
backup. rdiff-backup also preserves subdirectories, hard links, dev
files, permissions, uid/gid ownership, and modification times. Also,
rdiff-backup can operate in a bandwidth efficient manner over a pipe,
like rsync. Thus you can use rdiff-backup and ssh to securely back a
hard drive up to a remote location, and only the differences will be
transmitted. Finally, rdiff-backup is easy to use and settings have
sensical defaults.

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags}"
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root %{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/rdiff-backup

%files
%license COPYING
%doc CHANGELOG.adoc docs/FAQ.adoc docs/examples.adoc docs/index.adoc README.adoc
%{_mandir}/*/*
%{_bindir}/*
%{python3_sitearch}/rdiff_backup
%{python3_sitearch}/rdiffbackup
%{python3_sitearch}/*.egg-info
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/rdiff-backup

%changelog
