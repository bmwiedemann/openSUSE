#
# spec file for package kbfs
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018, Matthias Bach <marix@marix.org>
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


Name:           kbfs
Version:        2.11.0
Release:        0
Summary:        Encrypted remote storage based on Keybase identities
License:        BSD-3-Clause AND LGPL-3.0-or-later
Group:          Productivity/Security
URL:            https://github.com/keybase/kbfs/
Source:         https://github.com/keybase/kbfs/archive/v%{version}.tar.gz
Source1:        README.SUSE
Source2:        README.SUSE.git
Source3:        README.SUSE.tool
Patch1:         ensure-mount-dir-exists.patch
Patch2:         ensure-service-stop-unmounts-filesystem.patch
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  go1.15
BuildRequires:  golang-packaging
BuildRequires:  gzip
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
Requires:       keybase-client
Supplements:    keybase-client
%{go_nostrip}
%{?systemd_ordering}
%{go_provides}

%description
The Keybase filesystem provides encrypted remote storage. Encryption is
handled transparently based on Keybase accounts.

In addition to plain file storage this also provides a possibility to
host public files and store Git repositories.

%package git
Summary:        Git remote helper for repositories stored on Keybase
Group:          Productivity/Security
Requires:       kbfs
Requires:       keybase-client
Supplements:    keybase-client

%description git

A git remote helper that allows storing Git repositories using Keybase.
Repositories can be completely private or bound to a team.
Repositories using this remote helper use the scheme keybase://.

%package tool
Summary:        Keybase Filesystem command line utility
Group:          Productivity/Security
Requires:       keybase-client
Supplements:    keybase-client

%description tool

A thin command line utility for interacting with the Keybase Filesystem
without using a filesystem mountpoint.

%prep
%autosetup -p1

%build
%{goprep} github.com/keybase/%{name}
%{gobuild} -tags production kbfsfuse
%{gobuild} -tags production kbfstool
%{gobuild} -tags production kbfsgit/git-remote-keybase

%install
%{goinstall}
%{gofilelist}
install -D -m 644 packaging/linux/systemd/kbfs.service %{buildroot}%{_userunitdir}/kbfs.service
install -D -m 644 -p %{SOURCE1} %{buildroot}/%{_docdir}/%{name}/README.SUSE
install -D -m 644 -p %{SOURCE2} %{buildroot}/%{_docdir}/%{name}-git/README.SUSE
install -D -m 644 -p %{SOURCE3} %{buildroot}/%{_docdir}/%{name}-tool/README.SUSE
%fdupes %{buildroot}/%{_prefix}

%check
%{gotest} github.com/keybase/%{name}/kbfsfuse
%{gotest} github.com/keybase/%{name}/kbfstool
%{gotest} github.com/keybase/%{name}/kbfsgit

%post
%systemd_user_post kbfs.service

%preun
%systemd_user_preun kbfs.service

%files -f file.lst
%{_bindir}/kbfsfuse
%{_userunitdir}/kbfs.service
%{_docdir}/%{name}
%{_docdir}/%{name}/README.SUSE
%license LICENSE

%files git
%{_bindir}/git-remote-keybase
%{_docdir}/%{name}-git
%{_docdir}/%{name}-git/README.SUSE
%license LICENSE

%files tool
%{_bindir}/kbfstool
%{_docdir}/%{name}-tool
%{_docdir}/%{name}-tool/README.SUSE
%license LICENSE

%changelog
