#
# spec file for package zstd-jni
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


%global ver 1.5.7
%global rev 11
%global uver %{ver}-%{rev}
Name:           zstd-jni
Version:        %{ver}.%{rev}
Release:        0
Summary:        JNI binding for Zstd
License:        BSD-2-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/luben/%{name}
Source0:        %{url}/archive/refs/tags/v%{uver}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/github/luben/%{name}/%{uver}/%{name}-%{uver}.pom
Source100:      %{name}-build.xml
Patch0:         00-load-system-library.patch
Patch1:         max-page-size.patch
BuildRequires:  ant
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  javapackages-local >= 6

%description
JNI bindings for Zstd native library that provides fast and high compression
lossless algorithm for Android, Java and all JVM languages:
• static compress/decompress methods
• implementation of InputStream and OutputStream for transparent
  compression of data streams fully compatible with the “zstd” program.
• minimal performance overhead

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
API documentation for %{name}

%prep
%setup -q -n %{name}-%{uver}
%patch -P 0 -p1
%ifarch ppc64le
%patch -P 1 -p1
%endif
cp %{SOURCE100} build.xml

cat <<__JAVA__ >src/main/java/com/github/luben/zstd/util/ZstdVersion.java
package com.github.luben.zstd.util;

public class ZstdVersion {
	public static final String VERSION = "%{uver}";
}
__JAVA__

# Specify the library name, depends on 00-load-system-library.patch
sed -i -e 's#@SYS_LIBRARY_PREFIX@#%{_libdir}/%{name}#' \
	src/main/java/com/github/luben/zstd/util/Native.java

%build
ant jar javadoc

%cmake
%cmake_build

%install
# shared library
install -dm 0755 %{buildroot}%{_libdir}/%{name}
install -spm 0755 build/lib%{name}-%{uver}.so %{buildroot}%{_libdir}/%{name}

# jar
install -dm 0755 %{buildroot}%{_jnidir}/%{name}
install -pm 0644 target/%{name}-%{uver}.jar %{buildroot}%{_jnidir}/%{name}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md
%{_libdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
