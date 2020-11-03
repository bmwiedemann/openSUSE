#
# spec file for package apache-commons-daemon
#
# Copyright (c) 2020 SUSE LLC
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


%define short_name commons-daemon
Name:           apache-%{short_name}
Version:        1.2.3
Release:        0
Summary:        Commons Daemon - Controlling of Java Daemons
License:        Apache-2.0
Group:          System/Daemons
URL:            https://commons.apache.org/daemon/
Source0:        https://archive.apache.org/dist/commons/daemon/source/%{short_name}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/daemon/source/%{short_name}-%{version}-src.tar.gz.asc
Source2:        apache-commons-daemon.keyring
Source10:       apache-commons-daemon-build.xml
Patch0:         apache-commons-daemon-JAVA_OS.patch
Patch1:         apache-commons-daemon-riscv64.patch
BuildRequires:  ant
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  libcap-devel
BuildRequires:  make
BuildRequires:  xmlto
Provides:       jakarta-%{short_name} = %{version}
Obsoletes:      jakarta-%{short_name} < %{version}
Provides:       jakarta-%{short_name}-java = %{version}
Obsoletes:      jakarta-%{short_name}-java < %{version}

%description
The Daemon Component contains a set of Java and native code, including
a set of Java interfaces applications must implement and Unix native
code to control a Java daemon from a Unix operating system.

%package        jsvc
Summary:        Java daemon launcher
Group:          System/Daemons
Provides:       jsvc = %{version}-%{release}
Obsoletes:      jsvc < %{version}
Provides:       jakarta-%{short_name}:%{_sbindir}/jsvc

%description    jsvc
Jsvc is a set of libraries and applications for making Java applications run on
UNIX more easily. It allows the application (e.g. Tomcat) to perform some
privileged operations as root (e.g. bind to a port < 1024), and then switch
identity to a non-privileged user.

%package javadoc
Summary:        Commons Daemon Javadoc
Group:          Documentation/Other
Provides:       jakarta-%{short_name}-javadoc = %{version}
Obsoletes:      jakarta-%{short_name}-javadoc < %{version}
BuildArch:      noarch

%description javadoc
The Javadoc Documentation for Commons Daemon.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE10} build.xml
%patch0 -p1
%patch1 -p1

# remove java binaries from sources
rm -rf src/samples/build/

# remove files for different OS
rm -rf src/samples/*.cmd

# mark example files as non-executable
chmod -R 0644 src/samples/*

%pom_remove_parent .

# build manpage for jsvc
pushd src/native/unix
xmlto man man/jsvc.1.xml

%build
# build native jsvc
pushd src/native/unix
sh support/buildconf.sh

%configure
%make_build
popd

# build jar
%{ant}

%install
# native jsvc
install -Dpm 0755 src/native/unix/jsvc %{buildroot}%{_bindir}/jsvc
install -Dpm 0644 src/native/unix/jsvc.1 %{buildroot}%{_mandir}/man1/jsvc.1

# jar
install -Dpm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_jnidir}/%{short_name}.jar
ln -sf %{_jnidir}/%{short_name}.jar %{buildroot}%{_jnidir}/%{name}.jar

# pom
install -Dpm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name}"

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc PROPOSAL.html RELEASE-NOTES.txt src/samples
%doc src/docs/*
%{_jnidir}/%{name}.jar

%files jsvc
%license LICENSE.txt NOTICE.txt
%{_bindir}/jsvc
%{_mandir}/man1/jsvc.1%{?ext_man}

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
