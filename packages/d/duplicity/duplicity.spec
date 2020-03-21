#
# spec file for package duplicity
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


%define version_base 0.8.12
%define bzr_rev 1612
Name:           duplicity
Version:        %{version_base}.%{bzr_rev}
Release:        0
Summary:        Encrypted bandwidth-efficient backup using the rsync algorithm
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            http://duplicity.nongnu.org/
Source:         https://code.launchpad.net/%{name}/0.8-series/%{version_base}/+download/%{name}-%{version}.tar.gz
Patch1:         duplicity-remove_shebang.patch
BuildRequires:  fdupes
BuildRequires:  librsync-devel >= 0.9.6
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools
Requires:       gpg
Requires:       python3-fasteners
Requires:       python3-future
Requires:       python3-lockfile
Recommends:     %{name}-lang
Recommends:     lftp
Recommends:     python3-boto3

%description
Duplicity incrementally backs up files and directories by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or local)
file server. In theory many remote backends are possible; right now
local, ssh/scp, ftp, rsync, HSI, WebDAV, and Amazon S3 backends are
written.

Because duplicity uses librsync, the incremental archives are space
efficient and only record the parts of files that have changed since
the last backup. Currently duplicity supports deleted files, full unix
permissions, directories, symbolic links, fifos, etc., but not hard
links.

%lang_package

%prep
%setup -q
%patch1 -p1

%build
sed -i "s/revno = u'0'/revno = u'%{bzr_rev}'/" setup.py
%python3_build

%install
%python3_install
rm -rf %{buildroot}%{_datadir}/doc/duplicity-%{version}
perl -n -i -e 'print unless m,(%{_bindir}|%{_mandir}|%{_datadir}/doc|%{_datadir}/locale|%{python_sitearch}/testing),' files.lst
%find_lang %{name}
%fdupes %{buildroot}%{python3_sitearch}

%files
%license COPYING
%doc CHANGELOG README
%{_bindir}/duplicity
%{_bindir}/rdiffdir
%{python3_sitearch}/duplicity
%{python3_sitearch}/duplicity-*-py%{py3_ver}.egg-info
%{_mandir}/man1/duplicity.1%{?ext_man}
%{_mandir}/man1/rdiffdir.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
