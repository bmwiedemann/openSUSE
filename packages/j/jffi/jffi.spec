#
# spec file for package jffi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.2.12
Release:        0
Summary:        Java Foreign Function Interface
License:        LGPL-3.0-or-later OR Apache-2.0
Group:          Development/Libraries/Java
URL:            http://github.com/jnr/jffi
Source0:        https://github.com/%{cluster}/%{name}/archive/%{name}-%{version}.tar.gz
Source3:        p2.inf
Patch0:         jffi-fix-dependencies-in-build-xml.patch
Patch1:         jffi-add-built-jar-to-test-classpath.patch
Patch2:         jffi-fix-compilation-flags.patch
Patch3:         jffi-1.2.12-no_javah.patch
Patch4:         jffi-fix-system-ffi.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  make
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

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
%patch0
%patch1
%patch2
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 1.8}%{!?pkg_vcmp:0}
%patch3 -p1
%endif
%patch4 -p1

# ppc{,64} fix
# https://bugzilla.redhat.com/show_bug.cgi?id=561448#c9
sed -i.cpu -e '/m\$(MODEL)/d' jni/GNUmakefile libtest/GNUmakefile

# remove uneccessary directories
rm -rf archive/* jni/libffi/ jni/win32/ lib/CopyLibs/ lib/junit*

find ./ -name '*.jar' -exec rm -f '{}' \;
find ./ -name '*.class' -exec rm -f '{}' \;

build-jar-repository -s -p lib/ junit hamcrest/core

%{mvn_package} 'com.github.jnr:jffi::native:' native
%{mvn_file} ':{*}' %{name}/@1 @1

%build
# ant will produce JAR with native bits
ant jar build-native -Duse.system.libffi=1

# maven will look for JAR with native bits in archive/
cp -p dist/jffi-*-Linux.jar archive/

%{mvn_build}

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

mkdir -p META-INF/
cp %{SOURCE3} META-INF/
jar uf %{buildroot}%{_jnidir}/%{name}/%{name}.jar META-INF/p2.inf

# install *.so
install -dm 755 %{buildroot}%{_libdir}/%{name}
unzip dist/jffi-*-Linux.jar
mv jni/*-Linux %{buildroot}%{_libdir}/%{name}/
# create version-less symlink for .so file
pushd %{buildroot}%{_libdir}/%{name}/*
chmod +x lib%{name}-%{sover}.so
ln -s lib%{name}-%{sover}.so lib%{name}.so
popd

%check
# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile
ant -Duse.system.libffi=1 test

%files -f .mfiles
%license COPYING.GPL COPYING.LESSER LICENSE

%files native -f .mfiles-native
%{_libdir}/%{name}
%license COPYING.GPL COPYING.LESSER LICENSE

%files javadoc -f .mfiles-javadoc
%license COPYING.GPL COPYING.LESSER LICENSE

%changelog
