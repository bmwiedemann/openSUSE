#
# spec file for package 7zip
#
# Copyright (c) 2021 SUSE LLC
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


%define stripped_version 2107
Name:           7zip
Version:        21.07
Release:        0
Summary:        File Archivier
# CPP/7zip/Compress/LzfseDecoder.cpp is under the BSD-3-Clause
# C/Sha1.c and C/Sha256.c are in the public domain
License:        LGPL-2.1-or-later AND BSD-3-Clause AND SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
URL:            https://www.7-zip.org/
Source:         https://www.7-zip.org/a/7z%{stripped_version}-src.tar.xz
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
This package contains the 7z command line utility for archiving and
extracting various formats.

%prep
%__tar xaf %{SOURCE0}
dos2unix DOC/*.txt
# Remove executable perms from docs
chmod -x DOC/*.txt

# Remove -Werror to make build succeed
sed -i 's/-Werror//' CPP/7zip/7zip_gcc.mak
%if 0%{?suse_version} < 1550
# (gcc 7.x) Remove -Waddress-of-packed-member to make build succeed
sed -i -e 's/-Waddress-of-packed-member//' -e 's/-Wcast-align=strict//' C/warn_gcc.mak CPP/7zip/warn_gcc.mak
%endif
# Inject CFLAGS
sed -i 's/^ -fPIC/ -fPIC %{optflags}/' CPP/7zip/7zip_gcc.mak

%build
cd CPP/7zip//Bundles/Alone2
%make_build -f ../../cmpl_gcc.mak DISABLE_RAR_COMPRESS=1

%install
install -d -m 755 %{buildroot}%{_bindir}
install -Dt %{buildroot}%{_bindir} CPP/7zip/Bundles/Alone2/b/g/7zz

%files
%license DOC/copying.txt DOC/License.txt
%doc DOC/readme.txt DOC/7zC.txt DOC/Methods.txt DOC/src-history.txt
%{_bindir}/7zz

%changelog
