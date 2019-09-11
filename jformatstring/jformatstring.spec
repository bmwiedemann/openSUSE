#
# spec file for package jformatstring
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jformatstring
Version:        0.10~20131207
Release:        0
Summary:        Java library for format string checks
License:        GPL-2.0-only
Group:          Development/Libraries/Java
URL:            https://jformatstring.dev.java.net/
Source0:        http://cdn-fastly.deb.debian.org/debian/pool/main/j/jformatstring/jformatstring_%{version}.orig.tar.gz
Source1:        http://search.maven.org/remotecontent?filepath=com/google/code/findbugs/jFormatString/3.0.0/jFormatString-3.0.0.pom
Source2:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
Patch0:         jformatstring-build.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Provides:       jFormatString = %{version}-%{release}
Obsoletes:      jFormatString < %{version}-%{release}
BuildArch:      noarch

%description
This project is derived from Sun's implementation of java.util.Formatter. It
is designed to allow compile time checks as to whether or not a use of format
string will be erronous when executed at runtime.

This code is derived from the OpenJDK implementation, jdk1.7.0-b35. As such,
it is licensed under the same license as OpenJDK, GPL v2 + the Classpath
exception.

This project is preliminary, and the API is subject to change. The library
produced by compiling this project is used by the FindBugs project. To avoid
any licensing questions due to incompatible licenses (FindBugs is licensed
under the LGPL), it is broken out as a separate project. While there may be
some confusion/discussion about the licenses, the FindBugs project does not
interpret the FindBugs LGPL license to be any stronger than GPL v2 + the
Classpath exception.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
mkdir -p lib
cp %{SOURCE2} LICENSE

%build
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jarFile
mkdir -p javadoc
javadoc -notimestamp -d javadoc -source 1.6 \
           $(find src/java -name \*.java | xargs)

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 build/jFormatString.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/jFormatString.jar
ln -s jFormatString.jar %{buildroot}%{_javadir}/jFormatString-%{version}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
mkdir -p %{buildroot}%{_javadocdir}
cp -pr javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%{_javadir}/*

%files javadoc
%{_javadocdir}/*

%changelog
