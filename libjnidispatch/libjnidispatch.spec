#
# spec file for package libjnidispatch
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libjnidispatch
Version:        4.5.1
Release:        0
Summary:        Java Native Access (shared library)
License:        LGPL-2.1-or-later OR Apache-2.0
Group:          Development/Libraries/Java
Url:            https://github.com/twall/jna
Source0:        https://github.com/twall/jna/archive/%{version}.tar.gz
Source1000:     libjnidispatch-rpmlintrc
Patch0:         jna-build.patch
Patch1:         jna-getpeer.patch
Patch2:         jna-4.5.1-nojavah.patch
Patch4:         jna-msgsize.patch
Patch5:         jna-callback.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  libffi-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXt-devel
Requires:       java >= 1.8
Provides:       jna-native = %{version}-%{release}
Obsoletes:      jna-native < %{version}-%{release}

%description
Native library stub to dynamically invoke native code used by Java Native
Access library.

%package -n jna
Summary:        Java Native Access
Group:          Development/Libraries/Java
Requires:       libjnidispatch = %{version}
BuildArch:      noarch

%description -n jna
JNA provides Java programs easy access to native shared libraries without
writing anything but Java code. No JNI or native code is required. This
functionality is comparable to Windows' Platform/Invoke and Python's ctypes.
Access is dynamic at runtime without code generation.  JNA's design aims to
provide native access in a natural way with a minimum of effort. No boilerplate
or generated code is required. While some attention is paid to performance,
correctness and ease of use take priority.

The JNA library uses a small native library (%{name}) stub to dynamically
invoke native code. The developer uses a Java interface to describe functions
and structures in the target native library.  This makes it quite easy to take
advantage of native platform features without incurring the high overhead of
configuring and building JNI code for multiple platforms.

%package -n jna-javadoc
Summary:        Javadoc for Java Native Access
Group:          Documentation/HTML
BuildArch:      noarch

%description -n jna-javadoc
Javadoc reference for the Java Native Access library.

%prep
%setup -q -n jna-%{version}
# Cleanup the dist tarball
find . -name '*jar' | xargs rm
rm -rf dist
dos2unix OTHERS
# Then apply patch
%patch0 -p1 -b .orig
%patch1 -p1
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 10}%{!?pkg_vcmp:0}
%patch2 -p1
%endif
%patch4 -p1
%patch5 -p1

#FIXME: DirectTest fails
#rm test/com/sun/jna/DirectTest.java test/com/sun/jna/PerformanceTest.java

sed -i 's|soname,\$@|soname,%{name}.so|' native/Makefile
sed -i 's#<version>4.2.0</version>#<version>%{version}</version>#g' pom*.xml

%build
build-jar-repository -s -p lib ant
ant \
    jar \
    native \
    platform-jar \
    -Dcflags_extra.native="%{optflags}" \
    -Dbuild-native=true -Drelease \
    -Dcompatibility=1.8 \
    -Ddynlink.native=true \
    javadoc

%install
if [ -d build-d64 ]; then
suffix="-d64"
fi

install -d -m 755 %{buildroot}%{_libdir}
install -p -m 644 build${suffix}/native-*/libjnidispatch.so %{buildroot}%{_libdir}/libjnidispatch.so

install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build${suffix}/jna.jar %{buildroot}%{_javadir}/jna.jar
install -p -m 644 ./contrib/platform/dist/jna-platform.jar %{buildroot}%{_javadir}/jna-platform.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom-jna.xml %{buildroot}/%{_mavenpomdir}/jna.pom
install -p -m 644 pom-jna-platform.xml %{buildroot}/%{_mavenpomdir}/jna-platform.pom
%add_maven_depmap jna.pom jna.jar
%add_maven_depmap jna-platform.pom jna-platform.jar -a net.java.dev.jna:platform
%if %{defined _maven_repository}
mv %{buildroot}%{_mavendepmapfragdir}/%{name} %{buildroot}%{_mavendepmapfragdir}/jna
%else
mv %{buildroot}%{_datadir}/maven-metadata/%{name}.xml %{buildroot}%{_datadir}/maven-metadata/jna.xml
%endif

install -d -m 755 %{buildroot}%{_javadocdir}/jna
cp -pr doc/javadoc/* %{buildroot}%{_javadocdir}/jna
%fdupes -s %{buildroot}%{_javadocdir}/jna

%files
%license LICENSE
%attr(0755,root,root) %{_libdir}/libjnidispatch.so

%files -n jna
%license LICENSE
%doc CHANGES.md OTHERS README.md TODO
%{_javadir}/*
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/jna
%else
%{_datadir}/maven-metadata/jna.xml*
%endif

%files -n jna-javadoc
%{_javadocdir}/jna

%changelog
