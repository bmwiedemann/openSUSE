#
# spec file for package jsch
#
# Copyright (c) 2025 SUSE LLC
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
Name:           jsch
Version:        0.2.22
Release:        0
Summary:        Pure Java implementation of SSH2
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/mwiede/jsch/
Source0:        https://github.com/mwiede/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
Patch0:         jsch-junixsocket.patch
Patch1:         jsch-log4j.patch
BuildRequires:  ant
BuildRequires:  bouncycastle >= 1.77
BuildRequires:  fdupes
# We need this for module-info.class
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  jna
BuildRequires:  jna-contrib
BuildRequires:  slf4j
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%package        javadoc
Summary:        Pure Java implementation of SSH2
Group:          Development/Libraries/Java

%description    javadoc
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%package        demo
Summary:        Pure Java implementation of SSH2
Group:          Development/Libraries/Java

%description    demo
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} build.xml

# We don't have junixsocket
%pom_remove_dep com.kohlschutter.junixsocket:
rm -f \
    src/main/java/com/jcraft/jsch/JUnixSocketFactory.java
%patch -P 0 -p1

# Do not depend on log4j
%pom_remove_dep org.apache.logging.log4j:
rm -f \
    src/main/java/com/jcraft/jsch/Log4j2Logger.java \
    src/test/java/com/jcraft/jsch/Log4j2LoggerTest.java
%patch -P 1 -p1

%build
mkdir -p lib
build-jar-repository -s lib jna jna-platform slf4j/api bcprov
%{ant} -Dproject.version=%{version} jar javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a com.jcraft:jsch

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# examples
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -pr examples/* %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
