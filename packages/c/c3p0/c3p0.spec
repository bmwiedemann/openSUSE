#
# spec file for package c3p0
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2000-2008, JPackage Project
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


Name:           c3p0
Version:        0.12.0
Release:        0
Summary:        JDBC DataSources/Resource Pools
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            https://www.mchange.com/projects/c3p0/
Source0:        https://repo1.maven.org/maven2/com/mchange/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/com/mchange/%{name}/%{version}/%{name}-%{version}.pom
Source100:      %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  javapackages-local >= 6
BuildRequires:  mchange-commons >= 0.4.0
BuildRequires:  unzip
BuildArch:      noarch

%description
c3p0 is a library for augmenting traditional (DriverManager-based)
JDBC drivers with JNDI-bindable DataSources, including DataSources
that implement Connection and Statement Pooling, as described by the
jdbc3 spec and jdbc2 standard extension.

%package javadoc
Summary:        Javadoc for c3p0
Group:          Documentation/HTML

%description javadoc
Javadoc documentation for c3p0.

%prep
%setup -q -T -c
mkdir -p src/main/java
unzip %{SOURCE0} -d src/main/java
cp %{SOURCE100} build.xml

%build
mkdir -p lib
build-jar-repository -s lib mchange-commons
ant jar javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 target/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a c3p0:c3p0

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license src/main/java/LICENSE*

%files javadoc
%{_javadocdir}/%{name}

%changelog
