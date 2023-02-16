#
# spec file for package git-crypt
#
# Copyright (c) 2023 SUSE LLC
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


Name:           git-crypt
Version:        0.7.0
Release:        0
Summary:        Transparent file encryption in git
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://www.agwa.name/projects/git-crypt/
Source:         https://www.agwa.name/projects/git-crypt/downloads/git-crypt-%{version}.tar.gz
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(libcrypto)
Requires:       git-core

%description
git-crypt enables transparent encryption and decryption of files in a git
repository. Files which you choose to protect are encrypted when committed, and
decrypted when checked out. git-crypt lets you freely share a repository
containing a mix of public and private content. git-crypt gracefully degrades,
so developers without the secret key can still clone and commit to a repository
with encrypted files. This lets you store your secret material (such as keys or
passwords) in the same repository as your code, without requiring you to lock
down your entire repository.

%prep
%setup -q

%build
CXXFLAGS="-std=c++11 %{optflags}"
# https://github.com/AGWA/git-crypt/issues/232
%if %{pkg_version_cmp libopenssl-devel 3} != -1
CXXFLAGS="${CXXFLAGS} -DOPENSSL_API_COMPAT=0x30000000L"
%endif
export CXXFLAGS
make %{?_smp_mflags} \
    ENABLE_MAN=yes

%install
%make_install \
    ENABLE_MAN=yes \
    PREFIX="%{_prefix}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}"

%files
%doc doc/multiple_keys.md AUTHORS COPYING NEWS.md README.md
%{_bindir}/git-crypt
%{_mandir}/man1/git-crypt.1%{ext_man}

%changelog
