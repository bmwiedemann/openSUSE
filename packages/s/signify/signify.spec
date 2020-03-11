#
# spec file for package signify
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


Name:           signify
Version:        29
Release:        0
Summary:        OpenBSD tool to sign and verify signatures on files (portable version)
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
URL:            https://github.com/aperezdc/signify
Source0:        https://github.com/aperezdc/%{name}/archive/v%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbsd) >= 0.8

%description
Signify - Sign and Verify.
A portable version of the OpenBSD tool to sign and verify signatures on files.
See http://www.tedunangst.com/flak/post/signify for more information.

%prep
%setup -q

%build
export EXTRA_CFLAGS="%{optflags} -D_GNU_SOURCE"
export PREFIX="%{_prefix}"
%make_build

%install
export EXTRA_CFLAGS="%{optflags} -D_GNU_SOURCE"
export PREFIX="%{_prefix}"
%make_install

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
