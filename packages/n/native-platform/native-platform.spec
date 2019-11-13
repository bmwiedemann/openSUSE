#
# spec file for package native-platform
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


Name:           native-platform
Version:        0.14
Release:        0
Summary:        Java bindings for various native APIs
License:        Apache-2.0
URL:            https://github.com/adammurdoch/native-platform
Source0:        https://github.com/adammurdoch/native-platform/archive/%{version}.tar.gz
# From Debian
Source4:        %{name}-0.7-Makefile
# Try to load native library from /usr/lib*/native-platform
# instead of extractDir or classpath.
Patch0:         0001-Load-lib-from-system.patch
# Use generate libraries without arch references
# Add support for arm and other x64 arches
Patch1:         0002-Use-library-name-without-arch.patch
BuildRequires:  fdupes
# build tools and deps
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jopt-simple
BuildRequires:  ncurses-devel
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve

%description
A collection of cross-platform Java APIs
for various native APIs.

These APIs support Java 5 and later. Some
of these APIs overlap with APIs available
in later Java versions.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find .  -name "*.jar" -delete
find .  -name "*.class" -delete

%patch0 -p1
%patch1 -p1

cp -p %{SOURCE4} Makefile

chmod 644 readme.md
sed -i 's/\r//' readme.md

# TODO
mv src/curses/cpp/*.cpp src/main/cpp
mv src/shared/cpp/* src/main/cpp

%build
CFLAGS="${CFLAGS:-%{optflags}}" ; export CFLAGS ;
CPPFLAGS="${CPPFLAGS:-%{optflags}}" ; export CPPFLAGS ;
CXXFLAGS="${CXXFLAGS:-%{optflags}}" ; export CXXFLAGS ;
make %{?_smp_mflags} JAVA_HOME=%{_jvmdir}/java

%{mvn_artifact} net.rubygrapefruit:%{name}:%{version} build/%{name}.jar
%{mvn_file} : %{name}

%install
%mvn_install -J build/docs/javadoc
%fdupes -s %{buildroot}%{_javadocdir}

mkdir -p %{buildroot}%{_libdir}/%{name}
install -pm 0755 build/binaries/libnative-platform-curses.so %{buildroot}%{_libdir}/%{name}/
install -pm 0755 build/binaries/libnative-platform.so %{buildroot}%{_libdir}/%{name}/

%files -f .mfiles
%{_libdir}/%{name}
%doc readme.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
