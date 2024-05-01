#
# spec file for package jna
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2000-2009, JPackage Project
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           jna
Version:        5.13.0
Release:        0
Summary:        Pure Java access to native libraries
License:        Apache-2.0 OR LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            https://github.com/twall/jna
Source0:        %{name}-%{version}.tar.xz
Source1000:     %{name}-rpmlintrc
Patch0:         jna-build.patch
Patch1:         jna-callback.patch
Patch2:         jna-system-libjnidispatch.patch
Patch3:         jna-java8compat.patch
Patch4:         jna-old-libffi.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libffi-devel
BuildRequires:  objectweb-asm
BuildRequires:  pkgconfig
Requires:       java-headless >= 1.8
Provides:       jna-native = %{version}-%{release}
Obsoletes:      jna-native < %{version}-%{release}
Provides:       libjnidispatch = %{version}-%{release}
Obsoletes:      libjnidispatch < %{version}-%{release}

%description
JNA provides Java programs easy access to native shared libraries
(DLLs on Windows) without writing anything but Java code. JNA's
design aims to provide native access in a natural way with a
minimum of effort. No boilerplate or generated code is required.
While some attention is paid to performance, correctness and ease
of use take priority.

%package        contrib
Summary:        Contrib for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
Requires:       java-headless >= 1.8
Provides:       jna-platform = %{version}-%{release}
Obsoletes:      jna-platform < %{version}-%{release}
BuildArch:      noarch

%description    contrib
This package contains the contributed examples for %{name}.

%package        javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    javadoc
This package contains the javadocs for %{name}.

%prep
%setup -q

%patch -P 0 -p1 -b .orig
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%if 0%{?suse_version} < 1550
%patch -P 4 -p1
%endif

sed -i 's|@LIBDIR@|%{_libdir}/%{name}|' src/com/sun/jna/Native.java

%build
build-jar-repository -s -p lib ant
ln -s $(find-jar objectweb-asm/asm) lib/asm-8.0.1.jar
%{ant} \
    jar \
    native \
    platform-jar \
    -Dcflags_extra.native="%{optflags}" \
    -Dbuild-native=true -Drelease \
    -Dcompatibility=1.8 -Dplatform.compatibility=1.8 \
    -Ddynlink.native=true \
    jar \
    native \
    platform-jar \
    javadoc

%install
# NOTE: JNA has highly custom code to look for native jars in this
# directory.  Since this roughly matches the jpackage guidelines,
# we'll leave it unchanged.
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -m 755 build/native*/libjnidispatch*.so %{buildroot}%{_libdir}/%{name}/

install -d -m 755 %{buildroot}%{_jnidir}/%{name}
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -p -m 644 build/jna-jpms.jar %{buildroot}%{_jnidir}/%{name}.jar
ln -sf ../%{name}.jar %{buildroot}%{_jnidir}/%{name}/%{name}.jar
ln -sf %{_jnidir}/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 ./contrib/platform/dist/jna-platform-jpms.jar %{buildroot}%{_javadir}/%{name}-platform.jar
ln -sf ../%{name}-platform.jar %{buildroot}%{_javadir}/%{name}/%{name}-platform.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} build/pom-jna.xml %{buildroot}/%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a net.java.dev.jna:jna-jpms
%{mvn_install_pom} build/pom-jna-platform.xml %{buildroot}/%{_mavenpomdir}/%{name}-platform.pom
%add_maven_depmap %{name}-platform.pom %{name}-platform.jar -a net.java.dev.jna:platform,net.java.dev.jna:jna-platform-jpms -f contrib

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libjnidispatch.so
%{_jnidir}/%{name}
%{_javadir}/%{name}.jar
%license LICENSE
%doc CHANGES.md OTHERS README.md TODO

%files contrib -f .mfiles-contrib
%{_javadir}/%{name}

%files javadoc
%{_javadocdir}/jna
%license LICENSE

%changelog
