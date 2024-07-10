#
# spec file for package jffi
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


%global cluster jnr
%global sover 1.2
Name:           jffi
Version:        1.3.13
Release:        0
Summary:        Java Foreign Function Interface
License:        Apache-2.0 OR LGPL-3.0-or-later
Group:          Development/Libraries/Java
URL:            https://github.com/%{cluster}/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
Source3:        p2.inf
Patch0:         jffi-fix-dependencies-in-build-xml.patch
Patch1:         jffi-add-built-jar-to-test-classpath.patch
Patch2:         jffi-fix-system-ffi.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  maven-local
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  pkgconfig(libffi)

%description
An optimized Java interface to libffi.

%package native
Summary:        The %{name} JAR with native bits
Group:          Development/Libraries/Java

%description native
This package contains %{name} JAR with native bits.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%if 0%{?suse_version} <= 1500
sed -i -e '/case FFI_BAD_ARGTYPE:/,3d' jni/jffi/CallContext.c
%endif

# ppc{,64} fix
# https://bugzilla.redhat.com/show_bug.cgi?id=561448#c9
sed -i.cpu -e '/m\$(MODEL)/d' {jni,libtest}/GNUmakefile

%if %{?pkg_vcmp:%pkg_vcmp maven-antrun-plugin >= 3}%{!?pkg_vcmp:0}
sed -i -e 's#tasks\>#target\>#g' pom.xml
%pom_xpath_set "pom:plugin[pom:artifactId='maven-antrun-plugin']/pom:version" "3.0.0"
%pom_add_plugin "org.codehaus.mojo:build-helper-maven-plugin:3.2.0" pom.xml "
    <executions>
        <execution>
            <id>add-source-directory</id>
            <phase>generate-sources</phase>
            <configuration>
                <sources>
                    <source>\${project.build.directory}/java</source>
                </sources>
            </configuration>
            <goals>
                <goal>add-source</goal>
            </goals>
        </execution>
    </executions>
"
%endif

# remove uneccessary directories
rm -rf archive/* jni/libffi/ lib/junit*

find . -name '*.jar' -delete

build-jar-repository -s -p lib/ junit hamcrest/core

%{mvn_package} ':::native:' native
%{mvn_file} ':{*}' %{name}/@1 @1

%build
export CFLAGS=-O2
# ant will produce JAR with native bits
ant jar build-native -Duse.system.libffi=1

# maven will look for JAR with native bits in archive/
cp -p dist/jffi-*-Linux.jar archive/

%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)
cp target/%{name}-%{version}-complete.jar target/%{name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

mkdir -p META-INF/
cp %{SOURCE3} META-INF/
jar -uf %{buildroot}%{_jnidir}/%{name}/%{name}.jar META-INF/p2.inf

# install *.so
install -dm0755 %{buildroot}%{_libdir}/%{name}
unzip dist/jffi-*-Linux.jar
mv jni/*-Linux %{buildroot}%{_libdir}/%{name}/
# create version-less symlink for .so file
pushd %{buildroot}%{_libdir}/%{name}/*
chmod +x lib%{name}-%{sover}.so
ln -s lib%{name}-%{sover}.so lib%{name}.so
popd

%files -f .mfiles
%license LICENSE

%files native -f .mfiles-native
%{_libdir}/%{name}
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
