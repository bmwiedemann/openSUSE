#
# spec file for package duplicity
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


%if 0%{?suse_version} > 1500
%define _python python3
%define _python_sitearch %{?python3_sitearch}
%define _python3_version %{?python3_version}
%else
%define _python python311
%define _python_sitearch %{?python311_sitearch}
%define _python3_version %{?python311_version}
%endif
Name:           duplicity
Version:        3.0.4
Release:        0
Summary:        Encrypted bandwidth-efficient backup using the rsync algorithm
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://duplicity.gitlab.io/
Source:         https://gitlab.com/%{name}/%{name}/-/archive/rel.%{version}/%{name}-rel.%{version}.tar.bz2
BuildRequires:  %{_python}-devel
BuildRequires:  %{_python}-pytest
BuildRequires:  %{_python}-setuptools
BuildRequires:  %{_python}-setuptools_scm
BuildRequires:  fdupes
BuildRequires:  librsync-devel >= 0.9.6
BuildRequires:  python-rpm-macros
Requires:       %{_python}-fasteners
Requires:       %{_python}-lockfile
Requires:       gpg
Recommends:     %{_python}-boto3
Recommends:     %{name}-lang
Recommends:     lftp

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
%setup -q -n %{name}-rel.%{version}
sed -i -e 's|/usr/bin/env python3|/usr/bin/%{_python}|g' duplicity/__main__.py

%build
%if 0%{?suse_version} > 1500
%python3_build
%else
%python311_build
%endif

%install
%if 0%{?suse_version} > 1500
%python3_install
%else
%python311_install
%endif
rm -rf %{buildroot}%{_datadir}/doc/duplicity-%{version}
perl -n -i -e 'print unless m,(%{_bindir}|%{_mandir}|%{_datadir}/doc|%{_datadir}/locale|%{_python_sitearch}/testing),' files.lst
%find_lang %{name}
%fdupes %{buildroot}%{_python_sitearch}

%files
%license COPYING
%doc CHANGELOG.md README.md README-LOG.md
%{_bindir}/duplicity
%{_python_sitearch}/duplicity
%{_python_sitearch}/duplicity-*-py%{_python3_version}.egg-info
%{_mandir}/man1/duplicity.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
