#
# spec file for package keybase-client
#
# Copyright (c) 2022 SUSE LLC
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
Version:        5.9.1
Release:        0
Summary:        Keybase command line client
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/keybase/client/
Source:         client-%{version}.tar.xz
Source1:        README.SUSE
Source2:        keybase.service
Source3:        vendor-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  go1.16
BuildRequires:  golang-packaging
BuildRequires:  gzip
BuildRequires:  pkgconfig
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  pkgconfig(systemd)
%{go_nostrip}
%{?systemd_ordering}
%{go_provides}

%description
The Keybase command line client allows to manage a keybase.io account from
the command line. It includes functionality for encryption, signing, and
signature verifcation. It can create proofs to link a PGP key to other
accounts like Twitter, Github, or a Homepage. In addition, it allows to look
up keys for such accounts that people have created a proof for.

%prep
%setup -q -n client-%{version}
tar -xaf %{SOURCE3}

%build
%{goprep} github.com/keybase/client/go
%{gobuild} -tags production keybase

%install
%{goinstall}
%{gofilelist}
install -D -m 644 -p %{SOURCE2} %{buildroot}%{_userunitdir}/keybase.service
install -D -m 644 -p %{SOURCE1} %{buildroot}/%{_docdir}/%{name}/README.SUSE
%fdupes %{buildroot}/%{_prefix}

%check
%{gotest} github.com/keybase/client/go/keybase

%post
%systemd_user_post keybase.service

%preun
%systemd_user_preun keybase.service

%files -f file.lst
%{_bindir}/keybase
%{_userunitdir}/keybase.service
%{_docdir}/%{name}
%{_docdir}/%{name}/README.SUSE
%license LICENSE

%changelog
