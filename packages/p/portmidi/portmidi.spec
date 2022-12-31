#
# spec file for package portmidi
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


%if 0%{?suse_version} >= 1590
%bcond_without java
%else
%bcond_with    java
%endif

%define soname  2
Name:           portmidi
Version:        2.0.4
Release:        0
Summary:        Real-time MIDI input/output audio tools
License:        MIT
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://github.com/PortMidi/portmidi
Source:         https://github.com/PortMidi/portmidi/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  alsa-devel >= 0.9
BuildRequires:  gcc-c++
# we can reduce the minimum cmake version, if not building the java bindings
%if %{with java}
BuildRequires:  cmake >= 3.21
BuildRequires:  java-devel >= 11
%else
BuildRequires:  cmake >= 3.20
Obsoletes:      portmidi-java <= %{version}-%{release}
%endif
Requires:       libportmidi%{soname} = %{version}

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
Requires:       java
Requires:       libportmidi%{soname} = %{version}

%description java
PortMidi -- real-time MIDI input/output.
This package contains bindings to use %{name} from Java.

%prep
%autosetup -p1
find -type f -iname \*.txt -print0 | xargs -r0 chmod a-x
find -type f -iname \*.txt -print0 | xargs -r0 perl -p -i -e 's|\r\n|\n|g'

%if ! %{with java}
sed -i 's|cmake_minimum_required(VERSION 3.21)|cmake_minimum_required(VERSION 3.20)|' CMakeLists.txt
%endif

%build
%cmake \
  %if %{with java}
  -DBUILD_JAVA_NATIVE_INTERFACE:BOOL=ON \
  -DBUILD_PMDEFAULTS:BOOL=ON \
  %endif
  -DBUILD_PORTMIDI_TESTS:BOOL=ON \
  -DCMAKE_SKIP_BUILD_RPATH=ON
%cmake_build

%install
%cmake_install
pushd build
for binary in $(find pm_test/ -maxdepth 1 -type f -executable) ; do
  bin="$(basename ${binary})"
  install -D -m 0755 "${binary}" %{buildroot}%{_bindir}/portmidi-${bin}
done
popd

%if %{with java}
install -D -m 0644 pm_java/pmdefaults/pmdefaults.jar %{buildroot}%{_javadir}/pmdefaults.jar
cat > %{buildroot}%{_bindir}/pmdefaults <<EOF
#!/bin/bash
exec java -jar "@@JAVADIR@@/pmdefaults.jar" "$@" >/dev/null
EOF
chmod a+rx %{buildroot}%{_bindir}/pmdefaults
%endif

%post   -n libportmidi%{soname} -p /sbin/ldconfig
%postun -n libportmidi%{soname} -p /sbin/ldconfig

%files
%{_bindir}/portmidi-fast
%{_bindir}/portmidi-fastrcv
%{_bindir}/portmidi-latency
%{_bindir}/portmidi-midiclock
%{_bindir}/portmidi-midithread
%{_bindir}/portmidi-midithru
%{_bindir}/portmidi-mm
%{_bindir}/portmidi-multivirtual
%{_bindir}/portmidi-pmlist
%{_bindir}/portmidi-qtest
%{_bindir}/portmidi-recvvirtual
%{_bindir}/portmidi-sendvirtual
%{_bindir}/portmidi-sysex
%{_bindir}/portmidi-testio
%{_bindir}/portmidi-virttest

%files -n libportmidi%{soname}
%license license.txt
%doc README.txt pm_linux/README_LINUX.txt
%{_libdir}/libportmidi.so.*

%files devel
%{_libdir}/libportmidi.so
%{_includedir}/portmidi.h
%{_includedir}/pmutil.h
%{_includedir}/porttime.h
%{_libdir}/cmake/PortMidi/
%{_libdir}/pkgconfig/portmidi.pc

%post   java -p /sbin/ldconfig
%postun java -p /sbin/ldconfig

%if %{with java}
%files java
%{_bindir}/pmdefaults
%{_libdir}/libpmjni.so*
%{_javadir}/pmdefaults.jar
%endif

%changelog
