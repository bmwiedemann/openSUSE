#
# spec file for package 7zip
#
# Copyright (c) 2022 SUSE LLC
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


%define stripped_version 2201
Name:           7zip
Version:        22.01
Release:        0
Summary:        File Archivier
# CPP/7zip/Compress/LzfseDecoder.cpp is under the BSD-3-Clause
# C/Sha1.c and C/Sha256.c are in the public domain
License:        BSD-3-Clause AND LGPL-2.1-or-later AND SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
URL:            https://www.7-zip.org/
Source:         https://www.7-zip.org/a/7z%{stripped_version}-src.tar.xz
Source1:        p7zip
Source2:        p7zip.1
Patch0:         fix-compatib-with-p7zip.patch
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
%ifarch x86_64 %ix86 %x86_64
BuildRequires:  uasm
%endif
Conflicts:      p7zip
Conflicts:      p7zip-full
Provides:       p7zip = %{version}
Provides:       p7zip-full = %{version}
Obsoletes:      p7zip < %{version}
Obsoletes:      p7zip-full < %{version}

%description
This package contains the 7z command line utility for archiving and
extracting various formats.

%prep
tar xaf %{SOURCE0}
%patch0 -p1
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
sed -i 's/LFLAGS_ALL = -s/LFLAGS_ALL =/' CPP/7zip/7zip_gcc.mak
%ifarch x86_64 %ix86 %x86_64
sed -i 's/$(CXX) -o $(PROGPATH)/$(CXX) -Wl,-z,noexecstack -o $(PROGPATH)/' CPP/7zip/7zip_gcc.mak
%endif

%build
cd CPP/7zip/Bundles/Alone2
%ifarch x86_64 %x86_64
%make_build -f ../../cmpl_gcc_x64.mak MY_ASM=uasm
%else
%ifarch %ix86
%make_build -f ../../cmpl_gcc_x86.mak MY_ASM=uasm
%else
%make_build -f ../../cmpl_gcc.mak
%endif
%endif

%install
%ifarch x86_64 %x86_64
install -Dm 755 CPP/7zip/Bundles/Alone2/b/g_x64/7zz %{buildroot}%{_bindir}/7zz
%else
%ifarch %ix86
install -Dm 755 CPP/7zip/Bundles/Alone2/b/g_x86/7zz %{buildroot}%{_bindir}/7zz
%else
install -Dm 755 CPP/7zip/Bundles/Alone2/b/g/7zz %{buildroot}%{_bindir}/7zz
%endif
%endif
# Create links the executables provided by p7zip
ln -s %{_bindir}/7zz %{buildroot}%{_bindir}/7z
ln -s %{_bindir}/7z %{buildroot}%{_bindir}/7za
ln -s %{_bindir}/7z %{buildroot}%{_bindir}/7zr
# Install p7zip wrapper and its manpage
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/p7zip
install -m644 -Dt %{buildroot}%{_mandir}/man1 %{SOURCE2}
# Remove a mention of the p7zip-rar package that we don't have
sed -i 's/RAR (if the non-free p7zip-rar package is installed)//g' %{buildroot}%{_mandir}/man1/p7zip.1

%files
%license DOC/copying.txt DOC/License.txt
%doc DOC/readme.txt DOC/7zC.txt DOC/Methods.txt DOC/src-history.txt
%{_bindir}/7z
%{_bindir}/7za
%{_bindir}/7zr
%{_bindir}/7zz
%{_bindir}/p7zip
%{_mandir}/man1/p7zip.1%{?ext_man}

%changelog
