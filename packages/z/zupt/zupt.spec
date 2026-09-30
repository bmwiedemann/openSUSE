#
# spec file for package zup
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2026 Alessandro de Oliveira Faria (A.K.A CABELO) <cabelo@opensuse.org>
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

%if 0%{?suse_version} < 1600
%define isOldLeap %nil
%else
%undefine isOldLeap
%endif

Name:           zupt
Version:        5.2.9
Release:        0
Summary:        Backup compression with AES-256 authenticated encryption and post-quantum key encapsulation.
License:        MIT
Group:          Productivity/Archiving/Compression
URL:            https://github.com/cristiancmoises/zupt
Source0:        %{name}-%{version}.tar.gz
%if %{defined isOldLeap}
BuildRequires:  gcc12-c++ gcc12
%else
BuildRequires:  gcc-c++ gcc
%endif

BuildRequires:  gzip

%description
Zupt compresses and encrypts backup archives. LZ77+Huffman compression, AES-256-CTR + HMAC-SHA256 per-block authentication, multi-threaded, and optional ML-KEM-768 + X25519 post-quantum hybrid encryption. Pure C11, zero dependencies, ~5,000 lines.

%prep
%autosetup -p1
#chmod +x scripts/check-source-only.sh

%build
%if %{defined isOldLeap}
export CC=gcc-12 CXX=g++-12
%endif
#scripts/check-source-only.sh
%make_build V=1 \
    CWITH_SDK=0 WITH_PQBOX=0

%install
%make_install WITH_SDK=0 WITH_PQBOX=0 PREFIX=%{_prefix}
find /home/abuild/rpmbuild/BUILDROOT/

%files
%license LICENSE
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_bindir}/zupt
%{_mandir}/man1/zupt.1.gz
%{_datadir}/bash-completion/completions/zupt
%{_datadir}/fish/vendor_completions.d/zupt.fish
%{_datadir}/licenses/zupt/LICENSE-AGPL-3.0
%{_datadir}/licenses/zupt/LICENSE-BSD-2-Clause
%{_datadir}/licenses/zupt/LICENSE-BSD-3-Clause
%{_datadir}/licenses/zupt/LICENSE-CC0-1.0
%{_datadir}/licenses/zupt/LICENSE-GPL-3.0
%{_datadir}/licenses/zupt/NOTICE
%{_datadir}/licenses/zupt/THIRD-PARTY-NOTICES.md
%{_datadir}/zsh/site-functions/_zupt

%changelog

