#
# spec file for package faust
#
# Copyright (c) 2025 SUSE LLC
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

%define _lto_cflags %{nil}

Name:           faust
Version:        2.81.8
Release:        0
Summary:        Functional Programming Language for Real Time Signal Processing
License:        GPL-2.0-only
Group:          Development/Languages/Other
URL:            https://faust.grame.fr/
Source:         https://github.com/grame-cncm/faust/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         01-fix-no-return.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libmicrohttpd-devel
BuildRequires:  llvm-devel
Requires:       which

%description
Faust (Functional Audio Stream) is a functional programming language
specifically designed for real-time signal processing and synthesis.
A distinctive characteristic of Faust is to be fully compiled.

The Faust compiler translates DSP specifications into very efficient code for
various languages (C++, C, JAVA, JavaScript, ASM JavaScript, LLVM IR,
WebAssembly etc.) working at sample level. It targets high-performance signal
processing applications, libraries and audio plug-ins for a variety of audio
platforms and standards. A same Faust specification can be used to easily
generate various kinds of native standalone applications, iOS and Android apps,
as well as Csound, LADSPA, Max/MSP, PD, Q, SuperCollider, VST, AU plugins, etc.
(see the README in the /architecture folder for an exhaustive list).

%package devel
Summary:        Faust devel files
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}
Requires:       bash

%description devel
Devel files for embedding the Faust compiler in to your own application.

%package -n libfaust2
Summary:        Faust dynamic library
Group:          Development/Libraries/Other

%description -n libfaust2
Development files for embedding the Faust compiler in to your own application.

%package -n libHTTPDFaust0
Summary:        Faust HTTPD Library
Group:          Development/Libraries/Other

%description -n libHTTPDFaust0
Dynamic Faust HTTPD Library.

%package -n libOSCFaust1
Summary:        Faust OSC Library
Group:          Development/Libraries/Other

%description -n libOSCFaust1
Dynamic Faust OSC Library.

%package -n libfaustmachine0
Summary:        Faust Interpreter dynamic library
Group:          Development/Libraries/Other

%description -n libfaustmachine0
Dynamic Faust Interpreter library.

%package android-devel
Summary:        Faust Android build support
Group:          Development/Languages/Other
Requires:       faust = %{version}-%{release}
Requires:       faust-devel = %{version}-%{release}
BuildArch:      noarch

%description android-devel
Faust Android build support.

%package ios-devel
Summary:        Faust iOS build support
Group:          Development/Languages/Other
Requires:       faust = %{version}-%{release}
Requires:       faust-devel = %{version}-%{release}
BuildArch:      noarch

%description ios-devel
Faust iOS build support.

%prep
%autosetup -p1

%build
cd build
%cmake  \
%if %{defined fedora}
       -C backends/all.cmake \
%else
       -C ../backends/all.cmake \
%endif
       -DINCLUDE_DYNAMIC=ON \
       -DINCLUDE_STATIC=OFF \
       -DINCLUDE_LLVM=ON \
       -DINCLUDE_OSC=ON \
       -DINCLUDE_HTTP=ON \
       -DINCLUDE_ITP=ON \
       -DUSE_LLVM_CONFIG=ON \
       -DLINK_LLVM_STATIC=OFF \
       -DHTTPDYNAMIC=ON \
       -DOSCDYNAMIC=ON \
       -DITPDYNAMIC=ON \
       -DLIBSDIR=%{_lib}

%cmake_build

%install
cd build
%cmake_install

%fdupes -s %{buildroot}%{_datadir}/%{name}

for f in \
  %{buildroot}%{_bindir}/faust2atomsnippets \
  %{buildroot}%{_bindir}/faust2clap.py \
  %{buildroot}%{_bindir}/faust2md \
  %{buildroot}%{_bindir}/faust2sc.py \
  %{buildroot}%{_bindir}/faust2sublimecompletions \
  %{buildroot}%{_bindir}/faust2tidalcycles \
  %{buildroot}%{_datadir}/faust/wwise/orchestrator.py ; do
  sed -i '1s|^#! */usr/bin/env python3|#!/usr/bin/python3|' "$f"
done
sed -i '1s|^#! */usr/bin/env ruby|#!/usr/bin/ruby|' %{buildroot}%{_bindir}/faust2sc
sed -i '1s|^#! */usr/bin/env bash|#!/usr/bin/bash|' %{buildroot}%{_datadir}/faust/smartKeyboard/android/gradlew

# Drop empty placeholders that trigger rpmlint
find %{buildroot}%{_datadir}/faust/esp32/drivers/*/component.mk -type f -size 0 -print -delete

# Ensure installed scripts are executable
chmod 0755 %{buildroot}%{_datadir}/faust/autodiff/autodiff.sh
chmod 0755 %{buildroot}%{_datadir}/faust/smartKeyboard/android/gradlew
chmod 0755 %{buildroot}%{_datadir}/faust/wwise/orchestrator.py

# iOS static archive (non-ELF) – do not ship
rm -f %{buildroot}%{_libdir}/ios-libsndfile.a || true

# Max/MSP vendored static libs under /usr/share – do not ship
rm -f %{buildroot}%{_datadir}/faust/max-msp/sndfile/*/libsndfile.a || true

# Android bundled prebuilt libs (wrong arch; also arch-dependent under /usr/share) – do not ship
rm -f %{buildroot}%{_datadir}/faust/android/app/lib/libsndfile/lib/*/libsndfile.so || true

# Don’t ship a keystore/private key material
rm -f %{buildroot}%{_datadir}/faust/android/app/tools/faust2android.keystore || true

mkdir -p %{_builddir}/%{name}-%{version}.lists
ANDROID_LIST=%{_builddir}/%{name}-%{version}.lists/android.files
IOS_LIST=%{_builddir}/%{name}-%{version}.lists/ios.files
DEVEL_DATA=%{_builddir}/%{name}-%{version}.lists/devel_datadir.files

: > "$ANDROID_LIST"; : > "$IOS_LIST"; : > "$DEVEL_DATA"

# Collect Android/iOS files from datadir
if [ -d "%{buildroot}%{_datadir}/faust" ]; then
  find -L "%{buildroot}%{_datadir}/faust" -type f -ipath '*android*' -print >> "$ANDROID_LIST"
  find -L "%{buildroot}%{_datadir}/faust" -type f -ipath '*ios*'     -print >> "$IOS_LIST"

  find -L "%{buildroot}%{_datadir}/faust" -type f -print \
    | grep -vFf "$ANDROID_LIST" \
    | grep -vFf "$IOS_LIST" \
    >> "$DEVEL_DATA"
fi

# Also capture iOS bits under libdir (e.g. ios-libsndfile.a)
if [ -f "%{buildroot}%{_libdir}/ios-libsndfile.a" ]; then
  echo "%{buildroot}%{_libdir}/ios-libsndfile.a" >> "$IOS_LIST"
fi

# Strip buildroot and sort/uniq
sed -i 's|^%{buildroot}||' "$ANDROID_LIST" "$IOS_LIST" "$DEVEL_DATA"
# Escape for rpm filelists: backslashes first, then spaces and tabs
for f in "$ANDROID_LIST" "$IOS_LIST" "$DEVEL_DATA"; do
  sed -i \
    -e 's|\\|\\\\|g' \
    -e 's| |\\ |g' \
    -e 's|\t|\\t|g' \
    "$f"
done
sort -u -o "$ANDROID_LIST" "$ANDROID_LIST"
sort -u -o "$IOS_LIST" "$IOS_LIST"
sort -u -o "$DEVEL_DATA"  "$DEVEL_DATA"

# Build matching directory lists for each subpackage, so rpmlint is happy
ANDROID_DIRS=%{_builddir}/%{name}-%{version}.lists/android.dirs
IOS_DIRS=%{_builddir}/%{name}-%{version}.lists/ios.dirs
DEVEL_DIRS=%{_builddir}/%{name}-%{version}.lists/devel_datadir.dirs

gen_dirlist() {
  # $1 = filelist, $2 = outdirlist
  awk '
    {
      p=$0
      sub(/\/[^/]+$/, "", p)          # dirname
      while (p != "" && p != "/" && p != ".") {
        d[p]=1
        if (p=="/usr/share/faust") break
        sub(/\/[^/]+$/, "", p)
      }
    }
    END { for (x in d) print x }
  ' "$1" | sort -u | awk '{print "%dir " $0}' > "$2"
}

gen_dirlist "$ANDROID_LIST" "$ANDROID_DIRS"
gen_dirlist "$IOS_LIST"     "$IOS_DIRS"
gen_dirlist "$DEVEL_DATA"   "$DEVEL_DIRS"

ANDROID_ALL=%{_builddir}/%{name}-%{version}.lists/android.all
IOS_ALL=%{_builddir}/%{name}-%{version}.lists/ios.all
DEVEL_ALL=%{_builddir}/%{name}-%{version}.lists/devel_datadir.all

cat "$ANDROID_DIRS" "$ANDROID_LIST" | sort -u > "$ANDROID_ALL"
cat "$IOS_DIRS"     "$IOS_LIST"     | sort -u > "$IOS_ALL"
cat "$DEVEL_DIRS"   "$DEVEL_DATA"   | sort -u > "$DEVEL_ALL"


%ldconfig_scriptlets -n libfaust2
%ldconfig_scriptlets -n libHTTPDFaust0
%ldconfig_scriptlets -n libOSCFaust1
%ldconfig_scriptlets -n libfaustmachine0


%files
%license COPYING.txt
%doc README.md
%{_bindir}/encoderunitypackage
%{_bindir}/faust*
%{_bindir}/filename2ident
%{_bindir}/sound2reader
%{_bindir}/usage.sh
%{_mandir}/man1/faust.1.gz

%files -n libfaust2
%{_libdir}/libfaust.so.*

%files -n libfaustmachine0
%{_libdir}/libfaustmachine.so.*

%files -n libHTTPDFaust0
%{_libdir}/libHTTPDFaust.so.*

%files -n libOSCFaust1
%{_libdir}/libOSCFaust.so.*

%files android-devel -f %{_builddir}/%{name}-%{version}.lists/android.all

%files ios-devel -f %{_builddir}/%{name}-%{version}.lists/ios.all

%files devel -f %{_builddir}/%{name}-%{version}.lists/devel_datadir.all
%{_includedir}/faust/
%{_libdir}/libfaust.so
%{_libdir}/libfaustmachine.so
%{_libdir}/libHTTPDFaust.so
%{_libdir}/libOSCFaust.so
%{_libdir}/libHTTPDFaust.a
%{_libdir}/libOSCFaust.a
%{_libdir}/libfaustmachine.a

%changelog
