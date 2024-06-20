#
# spec file for package keybase-client
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Matthias Bach <marix@marix.org>
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


Name:           keybase-client
Version:        6.3.1
Release:        0
Summary:        Keybase command line client
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/keybase/client/
Source:         client-%{version}.tar.xz
Source1:        vendor-%{version}.tar.xz
Source2:        README.SUSE
Source3:        README.kbfs.SUSE
Source4:        README.git.SUSE
Source5:        README.tool.SUSE
Patch1:         ensure-mount-dir-exists.patch
Patch2:         ensure-service-stop-unmounts-filesystem.patch
BuildRequires:  fdupes
BuildRequires:  go1.21
BuildRequires:  golang-packaging
BuildRequires:  gzip
BuildRequires:  pkgconfig
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%{go_provides}

%description
The Keybase command line client allows to manage a keybase.io account from
the command line. It includes functionality for encryption, signing, and
signature verifcation. It can create proofs to link a PGP key to other
accounts like Twitter, Github, or a Homepage. In addition, it allows to look
up keys for such accounts that people have created a proof for.

%package -n kbfs
Summary:        Encrypted remote storage based on Keybase identities
Group:          Productivity/Security
Requires:       keybase-client
Supplements:    keybase-client

%description -n kbfs
The Keybase filesystem provides encrypted remote storage. Encryption is
handled transparently based on Keybase accounts.

In addition to plain file storage this also provides a possibility to
host public files and store Git repositories.

%package -n kbfs-git
Summary:        Git remote helper for repositories stored on Keybase
Group:          Productivity/Security
Requires:       kbfs
Requires:       keybase-client
Supplements:    keybase-client

%description -n kbfs-git

A git remote helper that allows storing Git repositories using Keybase.
Repositories can be completely private or bound to a team.
Repositories using this remote helper use the scheme keybase://.

%package -n kbfs-tool
Summary:        Keybase Filesystem command line utility
Group:          Productivity/Security
Requires:       keybase-client
Supplements:    keybase-client

%description -n kbfs-tool

A thin command line utility for interacting with the Keybase Filesystem
without using a filesystem mountpoint.

%prep
%autosetup -p1 -n client-%{version}
cd go
tar -xaf %{SOURCE1}

%build
cd go
%{goprep} github.com/keybase/client/go
%{gobuild} -tags production keybase
%{gobuild} -tags production kbfs/kbfsfuse
%{gobuild} -tags production kbfs/kbfstool
%{gobuild} -tags production kbfs/kbfsgit/git-remote-keybase

%install
cd go
%{goinstall}
cd ..
install -D -m 644 -p packaging/linux/systemd/keybase.service %{buildroot}%{_userunitdir}/keybase.service
install -D -m 644 -p packaging/linux/systemd/kbfs.service %{buildroot}%{_userunitdir}/kbfs.service
install -D -m 644 -p %{SOURCE2} %{buildroot}/%{_docdir}/%{name}/README.SUSE
install -D -m 644 -p %{SOURCE3} %{buildroot}/%{_docdir}/kbfs/README.SUSE
install -D -m 644 -p %{SOURCE4} %{buildroot}/%{_docdir}/kbfs-git/README.SUSE
install -D -m 644 -p %{SOURCE5} %{buildroot}/%{_docdir}/kbfs-tool/README.SUSE
%fdupes %{buildroot}/%{_prefix}

%check
cd go
%{gotest} -cpu 1 github.com/keybase/client/go/keybase
%ifnarch i586 arm armv7hl # kbfs tests are flacky on 32-bit archs
%{gotest} -cpu 1 github.com/keybase/client/go/kbfs/test
%{gotest} -cpu 1 github.com/keybase/client/go/kbfs/test -tags fuse
%endif
%{gotest} -cpu 1 github.com/keybase/client/go/kbfs/kbfstool
%{gotest} -cpu 1 github.com/keybase/client/go/kbfs/kbfsgit/git-remote-keybase

%post
%systemd_user_post keybase.service

%preun
%systemd_user_preun keybase.service

%post -n kbfs
%systemd_user_post kbfs.service

%preun -n kbfs
%systemd_user_preun kbfs.service

%files
%{_bindir}/keybase
%{_userunitdir}/keybase.service
%{_docdir}/%{name}
%{_docdir}/%{name}/README.SUSE
%license go/LICENSE

%files -n kbfs
%{_bindir}/kbfsfuse
%{_userunitdir}/kbfs.service
%{_docdir}/kbfs
%license go/kbfs/LICENSE

%files -n kbfs-git
%{_bindir}/git-remote-keybase
%{_docdir}/kbfs-git
%license go/kbfs/LICENSE

%files -n kbfs-tool
%{_bindir}/kbfstool
%{_docdir}/kbfs-tool
%license go/kbfs/LICENSE

%changelog
