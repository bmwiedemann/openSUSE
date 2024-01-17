#
# spec file for package jansi
#
# Copyright (c) 2023 SUSE LLC
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


Name:           jansi
Version:        2.4.0
Release:        0
Summary:        Java library for generating and interpreting ANSI escape sequences
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://fusesource.github.io/jansi/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Patch0:         %{name}-jni.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  javapackages-local

%description
Jansi is a java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it, like Windows, and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%pom_remove_parent

# We don't need the Fuse JXR skin
%pom_xpath_remove "pom:build/pom:extensions"

# Plugins not needed for an RPM build
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

# We don't want GraalVM support in Fedora
%pom_remove_plugin :exec-maven-plugin
%pom_remove_dep :picocli-codegen

# Build for JDK 1.8 at a minimum
%pom_xpath_set "//pom:properties/pom:jdkTarget" 1.8

# Link the JNI headers
ln -s %{java_home}/include/jni.h src/main/native/inc_linux
ln -s %{java_home}/include/linux/jni_md.h src/main/native/inc_linux

# Set the JNI path
sed -i 's,@LIBDIR@,%{_libdir},' \
    src/main/java/org/fusesource/jansi/internal/JansiLoader.java
# Filtering complicated with ant
sed -i 's,\${project.version},%{version},' \
    src/main/resources/org/fusesource/jansi/jansi.properties

%build
# Build the native artifact
CFLAGS="$CFLAGS -I. -I%{java_home}/include -I%{java_home}/include/linux -fPIC -fvisibility=hidden"
pushd src/main/native
%__cc $CFLAGS -c jansi.c
%__cc $CFLAGS -c jansi_isatty.c
%__cc $CFLAGS -c jansi_structs.c
%__cc $CFLAGS -c jansi_ttyname.c
%__cc $CFLAGS $LDFLAGS -shared -o libjansi.so *.o -lutil
popd

# Build the Java artifacts
%{ant} jar javadoc

%install
# Install the native artifact
install -dm 0755 %{buildroot}%{_libdir}/%{name}
install -pm 0755 src/main/native/libjansi.so %{buildroot}%{_libdir}/%{name}

# jar
install -dm 0755 %{buildroot}%{_jnidir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_jnidir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
%fdupes -s %{buildroot}%{_javadocdir}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license license.txt
%doc readme.md changelog.md
%{_libdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
