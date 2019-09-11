#
# spec file for package portmidi
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           portmidi
%define soname  0
Version:        217
Release:        0
Summary:        Real-time MIDI input/output audio tools
License:        MIT
Group:          Productivity/Multimedia/Sound/Midi
Url:            http://sourceforge.net/apps/trac/portmedia/wiki/portmidi
# http://prdownloads.sourceforge.net/portmedia/portmidi-src-217.zip
Source0:        portmidi-src-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM
Patch1:         portmidi-fix_build.patch
# PATCH-FIX-UPSTREAM
Patch2:         portmidi-fix_pmdefaults_startup_script.patch
# PATCH-FIX-UPSTREAM
Patch3:         portmidi-fix_java_cmake.patch
Source99:       portmidi-rpmlintrc
BuildRequires:  alsa-devel >= 0.9
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  java-devel
BuildRequires:  make
Requires:       libportmidi%{soname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PortMidi -- real-time MIDI input/output.
This package contains some command-line applications to test, configure and use
midi devices through PortMidi.

%package -n libportmidi%{soname}
Summary:        Real-time MIDI input/output audio library
Group:          System/Libraries
Recommends:     timidity

%description -n libportmidi%{soname}
PortMidi -- a library for real-time MIDI input/output audio.
This package contains the shared library that is required at runtime for every
application that uses PortMidi.

%package devel
Summary:        Real-time MIDI input/output audio library
Group:          Development/Libraries/Other
Requires:       libportmidi%{soname} = %{version}

%description devel
PortMidi -- real-time MIDI input/output.
This package contains the development environment to build applications and
other libraries that use PortMidi.

%package java
Summary:        Java native bindings for %{name}
Group:          Development/Libraries/Java
Requires:       libportmidi%{soname} = %{version}

%description java
PortMidi -- real-time MIDI input/output.
This package contains bindings to use %{name} from Java.

%prep
%setup -q -n "%{name}"
%patch1
%patch2
%if 0%{?suse_version} >= 1200
%patch3
%endif

perl -ne 'print $1,"\n" if /^\+{3}\s+(.+)\s+\d{4}-\d{2}-\d{2}\s+/' <"%{PATCH2}" | while read f; do
    sed -i -e 's|@@JAVADIR@@|%{_javadir}|g' "$f"
done

find . -type f -name '*.txt' -exec chmod 0644 {} \;
find . -type f -name 'README*.txt' -exec sed -i -e 's/\r$//' {} \;

%build
LIBSUFFIX=$(echo "%{_lib}" | sed 's|^lib||')
mkdir -p inst/{bin,lib}
OD="$PWD/inst"

# don't use a "build" subdir, doesn't work
OPTFLAGS="%{optflags}" \
cmake \
    -DCMAKE_VERBOSE_MAKEFILE=TRUE \
    -DCMAKE_INSTALL_PREFIX:PATH="%{_prefix}" \
    -DBIN_INSTALL_DIR="%{_bindir}" \
    -DLIB_INSTALL_DIR="%{_libdir}" \
    -DINC_INSTALL_DIR="%{_includedir}" \
    -DLIB_SOVERSION="%{soname}" \
    -DLIB_VERSION="%{soname}.%{version}" \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
    -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
    -DCMAKE_BUILD_TYPE=release \
    -DCMAKE_STRIP="/usr/bin/touch" \
    -DLIB_SUFFIX="$LIBSUFFIX" \
    -DCMAKE_RUNTIME_OUTPUT_DIRECTORY="$OD/bin" \
    -DCMAKE_LIBRARY_OUTPUT_DIRECTORY="$OD/lib" \
    -DCMAKE_ARCHIVE_OUTPUT_DIRECTORY="$OD/lib" \
    .

make %{?_smp_flags}

%install
make DESTDIR=%{buildroot} install

pushd inst/bin
for f in *; do
    [ -x "$f" ] || continue
    install -m0755 "$f" "%{buildroot}%{_bindir}/%{name}-$f"
done
popd #inst/bin
# remove static lib
rm -rf %{buildroot}%{_libdir}/libportmidi_s.a
# Added missing libporttime.so symlink
cd %{buildroot}%{_libdir}
ln -s libportmidi.so libporttime.so

%post   -n libportmidi%{soname} -p /sbin/ldconfig

%postun -n libportmidi%{soname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/pmdefaults
%{_bindir}/portmidi-latency
%{_bindir}/portmidi-mm
%{_bindir}/portmidi-midiclock
%{_bindir}/portmidi-midithread
%{_bindir}/portmidi-midithru
%{_bindir}/portmidi-sysex
%{_bindir}/portmidi-test
%{_bindir}/portmidi-qtest

%files -n libportmidi%{soname}
%defattr(-,root,root)
%doc license.txt README.txt pm_linux/README_LINUX.txt
%{_libdir}/libportmidi.so.%{soname}
%{_libdir}/libportmidi.so.%{soname}.%{version}

%files devel
%defattr(-,root,root)
%{_includedir}/portmidi.h
%{_includedir}/porttime.h
%{_libdir}/libportmidi.so
%{_libdir}/libporttime.so

%files java
%defattr(-,root,root)
%{_libdir}/libpmjni.so
%{_javadir}/pmdefaults.jar

%changelog
