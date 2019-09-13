#
# spec file for package apache-commons-daemon
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


%define short_name commons-daemon
Name:           apache-%{short_name}
Version:        1.0.15
Release:        0
Summary:        Commons Daemon - Controlling of Java Daemons
License:        Apache-2.0
Group:          System/Daemons
Url:            http://commons.apache.org/daemon/
Source0:        http://www.eu.apache.org/dist/commons/daemon/source/commons-daemon-%{version}-src.tar.gz
Source1:        http://www.eu.apache.org/dist/commons/daemon/source/commons-daemon-%{version}-src.tar.gz.asc
Source2:        apache-commons-daemon.keyring
Patch0:         apache-commons-daemon-JAVA_OS.patch
Patch1:         apache-commons-daemon-s390x.patch
Patch2:         apache-commons-daemon-ppc64.patch
Patch3:         apache-commons-daemon-aarch64.patch
Patch4:         apache-commons-daemon-riscv64.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  libcap-devel
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
Provides:       jakarta-%{short_name}-javadoc = %{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{version}
BuildArch:      noarch

%description javadoc
The Javadoc Documentation for Commons Daemon.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# remove java binaries from sources
rm -rf src/samples/build/

# remove files for different OS
rm -rf src/samples/*.cmd

chmod -R 0644 src/samples/*

%pom_remove_parent .

%build
pushd src/native/unix
xmlto man man/jsvc.1.xml

# build native jsvc
%configure --with-java=%{java_home}
# this is here because 1.0.2 archive contains old *.o
make %{?_smp_mflags} clean
make %{?_smp_mflags}
popd
ant \
    -Dcompile.source=8 -Dcompile.target=8 \
    jar test javadoc

%install
# install native jsvc
install -Dm 0755 src/native/unix/jsvc %{buildroot}%{_bindir}/jsvc
install -Dpm 644 src/native/unix/jsvc.1 %{buildroot}%{_mandir}/man1/jsvc.1

# jars
install -Dpm 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# pom
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.commons:%{short_name}"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%license LICENSE.txt
%doc PROPOSAL.html NOTICE.txt RELEASE-NOTES.txt src/samples
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_datadir}/maven-metadata/%{name}.xml

%files jsvc
%license LICENSE.txt
%{_bindir}/jsvc
%{_mandir}/man1/jsvc.1*

%files javadoc
%license LICENSE.txt
%doc src/docs/*
%doc %{_javadocdir}/%{name}

%changelog
