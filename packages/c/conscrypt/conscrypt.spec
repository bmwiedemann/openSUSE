#
# spec file for package conscrypt
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global ver_major 2
%global ver_minor 6
%global ver_patch 3
%if 0%{?gcc_version} < 10
%define with_gcc 11
%endif
Name:           conscrypt
Version:        %{ver_major}.%{ver_minor}.%{ver_patch}
Release:        0
Summary:        A Java Security Provider that implements parts of the JCE and JSSE
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/%{name}/%{name}-openjdk/%{version}/%{name}-openjdk-%{version}.pom
# fixes: https://github.com/google/conscrypt/issues/1530
Patch0:         ignore-unsupported-x25519kyber768draft00-group.patch
BuildRequires:  boringssl-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  maven-local

%description
Conscrypt is a Java Security Provider (JSP) that implements parts of the Java
Cryptography Extension (JCE) and Java Secure Socket Extension (JSSE). It uses
BoringSSL to provide cryptographic primitives and Transport Layer Security
(TLS) for Java applications on Android and OpenJDK. See the capabilities
documentation for detailed information on what is provided.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1
cp %{SOURCE1} openjdk/pom.xml

%pom_xpath_remove pom:packaging openjdk
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin openjdk \
'<configuration>
  <archive>
    <manifest>
      <addDefaultImplementationEntries>true</addDefaultImplementationEntries>
      <addBuildEnvironmentEntries>true</addBuildEnvironmentEntries>
    </manifest>
    <manifestEntries>
      <Automatic-Module-Name>org.conscrypt</Automatic-Module-Name>
    </manifestEntries>
  </archive>
</configuration>'

cp -rv common/src openjdk/

cat <<__CMAKELISTS__ >openjdk/CMakeLists.txt
cmake_minimum_required(VERSION 3.5.0)
project(conscrypt_jni LANGUAGES CXX)
add_library(conscrypt_jni SHARED
	../common/src/jni/main/cpp/conscrypt/compatibility_close_monitor.cc
	../common/src/jni/main/cpp/conscrypt/jniload.cc
	../common/src/jni/main/cpp/conscrypt/jniutil.cc
	../common/src/jni/main/cpp/conscrypt/native_crypto.cc
	../common/src/jni/main/cpp/conscrypt/netutil.cc
	)
include_directories(
	%{_includedir}/boringssl
	../common/src/jni/main/include/
    ../common/src/jni/unbundled/include/
	${JAVA_HOME}/include/
	${JAVA_HOME}/include/linux/
	)
target_link_libraries(conscrypt_jni boringssl_ssl boringssl_crypto \${CMAKE_DL_LIBS})
__CMAKELISTS__

%build
pushd openjdk
%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%cmake .
%cmake_build
mkdir -p ../src/main/resources/META-INF/native/
cp libconscrypt_jni.so ../src/main/resources/META-INF/native/libconscrypt_openjdk_jni-linux-%{_arch}.so

mkdir -p ../src/main/resources/org/conscrypt/
cat <<__PROPERTIES__ > ../src/main/resources/org/conscrypt/conscrypt.properties
org.conscrypt.boringssl.version=%{pkg_version boringssl-devel}
org.conscrypt.version.major=%{ver_major}
org.conscrypt.version.minor=%{ver_minor}
org.conscrypt.version.patch=%{ver_patch}
__PROPERTIES__
popd

env -Cconstants ${CXX:-g++} -I%{_includedir}/boringssl src/gen/cpp/generate_constants.cc -o generate_constants
./constants/generate_constants >openjdk/src/main/java/org/conscrypt/NativeConstants.java

pushd openjdk
%{mvn_alias} :{*} :@1-uber

%{mvn_build} -f -- \
    -Dmaven.compiler.source=8 -Dmaven.compiler.target=8 \
    -Dsource=8
popd

%install
pushd openjdk
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}
# This helps to generate the right requires on boringssl and eventually,
# we might patch the library loading to consider just this one
install -dm 0755 %{buildroot}%{_libdir}/%{name}
install -pm 0755 build/libconscrypt_jni.so %{buildroot}%{_libdir}/%{name}/
popd

%files -f openjdk/.mfiles
%{_libdir}/%{name}
%license LICENSE NOTICE
%doc {README,IMPLEMENTATION_NOTES,CAPABILITIES}.md

%files javadoc -f openjdk/.mfiles-javadoc
%license LICENSE NOTICE

%changelog
