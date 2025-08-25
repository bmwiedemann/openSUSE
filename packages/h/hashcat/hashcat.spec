#
# spec file for package hashcat
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global lname	libhashcat7_1_2

Name:           hashcat
Version:        7.1.2
Release:        0
Summary:        CPU-based password recovery utility
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Security
URL:            https://hashcat.net/
Source:         https://hashcat.net/files/%name-%version.tar.gz
Source2:        https://hashcat.net/files/%name-%version.tar.gz.asc
#  Key ID: 2048R/8A16544F. Fingerprint: A708 3322 9D04 0B41 99CC 0052 3C17 DA8B 8A16 544F
Source3:        %name.keyring
Source9:        %name-rpmlintrc
Patch1:         system-libs.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  xxhash-devel
%if 0%{?suse_version} >= 1690
BuildRequires:  pkgconfig(lzma-sdk)
%else
%global sylzma USE_SYSTEM_LZMA=0
Provides:       bundled(lzma-sdk) = 24.09
%endif
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  %ix86 x86_64

%description
Hashcat is a password recovery utility, supporting seven
unique modes of testing for over 100 optimized hashing algorithms.

%package -n %lname
Summary:        Implementation of the hashcat engine
Group:          System/Libraries

%description -n %lname
Hashcat is a password recovery utility, supporting seven
unique modes of testing for over 100 optimized hashing algorithms.

%package devel
Summary:        Header files for making hashcat plugins
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Hashcat is a password recovery utility, supporting seven
unique modes of testing for over 100 optimized hashing algorithms.

This subpackage contains the header files.

%prep
%autosetup -p1
find . -name .lock -type f -delete

%build
%global margs DOCUMENT_FOLDER="%_docdir/%name" our_CFLAGS="%optflags" LIBRARY_FOLDER="%_libdir" BUILD_MODE=cross %{?sylzma}
%make_build %margs

%install
%make_install %margs

b="%buildroot"
ln -s libhashcat.so.%version "$b/%_libdir/libhashcat.so"

# fix placement of arch-dep files
mkdir "$b/%_libdir/%name"
mv "$b/%_datadir/%name/modules" "$b/%_libdir/%name/"
ln -s "%_libdir/%name/modules" "$b/%_datadir/%name/"
mv "$b/%_datadir/%name/bridges" "$b/%_libdir/%name/"
ln -s "%_libdir/%name/bridges" "$b/%_datadir/%name/"

# script-without-shebang: add shebang to python scripts
for file in \
  /usr/bin/bitlocker2hashcat.py \
  /usr/bin/keybag2hashcat.py \
  /usr/bin/shiro1-to-hashcat.py \
  /usr/bin/veeamvbk2hashcat.py
do
  sed -i '1i#!/usr/bin/python3' "$b$file"
done

# env-script-interpreter: replace /usr/bin/env <interpreter> with <interpreter>
# perl scripts
find "$b/%_bindir" -type f -name '*.pl' -exec \
  sed -i '1s|^#!\s*/usr/bin/env\s\+\(.*\)$|#!/usr/bin/\1|' {} +
# python scripts
%python3_fix_shebang

# hidden-file-or-dir: remove .gitkeep files
find "$b/%_libdir/%name" -type f -name .gitkeep -delete

# wrong-script-end-of-line-encoding /usr/bin/shiro1-to-hashcat.py
dos2unix "$b/%_bindir/shiro1-to-hashcat.py"

# spurious-executable-perm: remove executable bit from non-executable files
find "$b/%_docdir/%name" -type f -exec chmod -x {} \;

%fdupes %buildroot/%_prefix

%ldconfig_scriptlets -n %lname

%files
%doc README.md
%_bindir/hashcat
%_docdir/%name/
%_libdir/%name/
%_datadir/%name/
# conversion scripts
%_bindir/*2hashcat.*
%_bindir/radmin3_to_hashcat.pl
%_bindir/shiro1-to-hashcat.py

%files -n %lname
%_libdir/libhashcat.so.%version

%files devel
%_includedir/hashcat/
%_libdir/libhashcat.so

%changelog
