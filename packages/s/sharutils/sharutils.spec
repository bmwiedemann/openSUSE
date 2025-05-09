#
# spec file for package sharutils
#
# Copyright (c) 2024 SUSE LLC
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


Name:           sharutils
Version:        4.15.2
Release:        0
Summary:        GNU shar utilities
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://www.gnu.org/software/sharutils/
Source0:        https://ftp.gnu.org/gnu/sharutils/sharutils-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/sharutils/sharutils-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch0:         sharutils-testsuite.diff
Patch1:         sharutils-CVE-2018-1000097-fix_buffer_overflow.patch
Patch2:         gnulib-libio.patch
Patch3:         sharutils-4.14.2-Pass-compilation-with-Werror-format-security.patch
BuildRequires:  libopenssl-devel
BuildRequires:  xz
Requires(pre):  %{install_info_prereq}
Requires(pre):  coreutils
Provides:       sharutil = %{version}
Obsoletes:      sharutil < %{version}

%description
This is the set of GNU shar utilities.

shar makes shell archives out of many files, preparing them for
transmission by electronic mail services.  Use unshar to unpack shell
archives after reception.

uuencode prepares a file for transmission over an electronic channel
which ignores or otherwise mangles the eight bit (high order bit) of
bytes.	uudecode does the converse transformation.

%{?lang_package}

%prep
%setup -q
%patch -P 0
%patch -P 1
%patch -P 2 -p1
%patch -P 3 -p1
chmod +w src/scripts.x

%build
mkdir -p ../bin
ln -snf /bin/true ../bin/compress
PATH=$PWD/../bin:$PATH
%global optflags %{optflags} -fcommon -std=gnu11
%configure \
	--with-openssl

%make_build

%check
%make_build check

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files lang -f %{name}.lang

%files
%doc README NEWS THANKS
%license COPYING
%{_bindir}/*
%{_infodir}/*.gz
%{_mandir}/*/*.gz

%changelog
