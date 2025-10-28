#
# spec file for package git-weave
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           git-weave
Version:        1.5
Release:        0
Summary:        Weave a tarball sequence into a git repository
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/git-weave/
Source:         http://www.catb.org/~esr/git-weave/%{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
Requires:       cpio
Requires:       find
Requires:       git-core
BuildArch: noarch

%description
git-weave takes a tarball sequence and a metadata file and synthesizes a live
repository. It can invert this, explode git repositories into sequences of
per-commit tarballs. The DAG is expressed as a metadata file with mailbox-like
entries.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install \
	DESTDIR=%{buildroot} \
	prefix=%{_prefix} \
	%{nil}
%python3_fix_shebang

%files
%license COPYING
%doc NEWS README
%{_bindir}/git-weave
%{_mandir}/man1/git-weave.1%{?ext_man}

%changelog
