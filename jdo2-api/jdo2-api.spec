#
# spec file for package jdo2-api
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


Name:           jdo2-api
Version:        2.2
Release:        0
Summary:        Implementation of JSR 243: Java Data Objects 2.0
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://db.apache.org/jdo/
Source0:        http://svn.apache.org/repos/asf/db/jdo/tags/%{version}/dist/db/jdo/%{version}/%{name}-%{version}-src.tar.gz
Source1:        %{name}-%{version}-build.xml
# changed javax.transaction transaction-api 1.1 with geronimo-jta_1.1_spec
# fix pom version
Source2:        http://repo1.maven.org/maven2/javax/jdo/%{name}/%{version}/%{name}-%{version}.pom
Patch0:         jdo2-api-2.2-pom.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  geronimo-jpa-3_0-api
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildConflicts: java-devel >= 11
Requires:       javapackages-tools
BuildArch:      noarch

%description
The Java Data Objects 2 (JDO) API is a standard interface-based
Java model abstraction of persistence, developed as Java Specification
Request 243 under the auspices of the Java Community Process.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c
cd %{name}-%{version}
cp -p %{SOURCE1} build.xml
cp -p %{SOURCE2} pom.xml
%patch0

%{mvn_file} : %{name}

%build
pushd %{name}-%{version}
%{ant} -Dant.build.javac.source=8 -Dant.build.javac.target=8 jar javadoc
popd

%{mvn_artifact} %{name}-%{version}/pom.xml %{name}-%{version}/%{name}-%{version}.jar

%install
%mvn_install -J %{name}-%{version}/dist/docs/api
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
