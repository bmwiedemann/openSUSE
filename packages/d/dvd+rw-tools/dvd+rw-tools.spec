#
# spec file for package dvd+rw-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dvd+rw-tools
Version:        7.1
Release:        0
Summary:        Collection of Tools for Mastering Blu-ray and DVD+-RW/+-R Media
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Record
URL:            http://fy.chalmers.se/~appro/linux/DVD+RW/
# http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-7.1.tar.gz
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE utf8ize.patch sbrabec@suse.cz -- Convert some strings to UTF-8
Patch0:         utf8ize.patch
# PATCH-FIX-OPENSUSE growisofs-dvd-dl-undersized.patch bnc#164032 joeshaw@suse.de -- Allow users to burn images that would fit on a single-layer DVD to a dual-layer disc
Patch1:         growisofs-dvd-dl-undersized.patch
# NOTE: commented out. PATCH-FIX-OPENSUSE growisofs-genisoimage.patch nadvornik@suse.cz -- Make the package call genisoimage directly, not via compatibility symlink
Patch2:         growisofs-genisoimage.patch
# PATCH-FIX-OPENSUSE dvd+rw-tools-gcc43.patch ro@suse.de -- Fix build with gcc-4.3
Patch3:         dvd+rw-tools-gcc43.patch
# PATCH-FIX-OPENSUSE dvd+rw-tools-buffer.patch bnc#354838 nadvornik@suse.cz -- Fix buffer size
Patch4:         dvd+rw-tools-buffer.patch
# PATCH-FIX-UPSTREAM fix-build-with-recent-glibc.patch
Patch5:         fix-build-with-recent-glibc.patch
BuildRequires:  gcc-c++
BuildRequires:  m4
# According to Linux from scratch dvd+rw-tools needs this to function correctly with wodim
Requires:       %{_bindir}/mkisofs
Requires:       libisoburn1

%description
The dvd+rw-tools collection of tools makes it possible to burn images to
Blu-ray and DVD+-RW/+-R media.

%prep
%setup -q
%patch0
%patch1
#%%patch2
%patch3
%patch4
%patch5 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"

make %{?_smp_mflags} CC="gcc" CXX="g++"
make rpl8 btcflash %{?_smp_mflags} CC="gcc" CXX="g++"

%install
make prefix=%{buildroot}%{_prefix} manprefix=%{buildroot}%{_mandir} install

# Rename btcflash binary in order to avoid conflict with btcflash from cdrtools
mv %{buildroot}%{_bindir}/btcflash %{buildroot}%{_bindir}/dvd+rw-tools-btcflash

%files
%license LICENSE
%doc index.html
%{_bindir}/dvd+rw-booktype
%{_bindir}/dvd+rw-format
%{_bindir}/dvd+rw-mediainfo
%{_bindir}/dvd+rw-tools-btcflash
%{_bindir}/dvd-ram-control
%{_bindir}/growisofs
%{_bindir}/rpl8
%{_mandir}/man1/growisofs.1%{?ext_man}

%changelog
