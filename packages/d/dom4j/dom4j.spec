#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2000-2007, JPackage Project
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


%global base_name dom4j
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
Version:        2.1.4
Release:        0
Summary:        Open Source XML framework for Java
License:        BSD-3-Clause
URL:            https://dom4j.github.io/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/org/%{base_name}/%{base_name}/%{version}/%{base_name}-%{version}.pom
Source2:        %{base_name}-build.xml
Patch0:         0001-no-jaxen-dom4.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-jaxb-api
BuildRequires:  javapackages-local >= 6
Obsoletes:      %{base_name}-manual < %{version}
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-bootstrap
%else
Name:           %{base_name}
%endif
%if %{without bootstrap}
BuildRequires:  fdupes
BuildRequires:  jaxen
Conflicts:      %{base_name}-bootstrap
Obsoletes:      %{base_name}-bootstrap
%else
BuildRequires:  jaxen-bootstrap
Conflicts:      %{base_name}
%endif

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM and SAX and is seamlessly integrated with full XPath support.

%if %{without bootstrap}
%package demo
Summary:        Open Source XML framework for Java - demo
Group:          Development/Libraries/Java
Requires:       %{base_name} = %{version}

%description demo
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM and SAX and is seamlessly integrated with full XPath support.

%package javadoc
Summary:        Javadoc for %{base_name}

%description javadoc
Javadoc for %{base_name}.
%endif

%prep
%setup -q -n %{base_name}-%{version}
%if %{with bootstrap}
%patch0 -p1
%endif

cp %{SOURCE1} pom.xml
cp %{SOURCE2} build.xml

# Remove xpp2 support
rm -r src/main/java/org/dom4j/xpp
rm src/main/java/org/dom4j/io/XPPReader.java

# Remove datatype code which depends on msv
rm -r src/main/java/org/dom4j/datatype
%pom_remove_dep net.java.dev.msv:xsdlib

# Remove xpp3 support
rm src/main/java/org/dom4j/io/XPP3Reader.java
%pom_remove_dep xpp3:xpp3
%pom_remove_dep pull-parser:pull-parser
%pom_remove_dep javax.xml.stream:stax-api

%build
mkdir -p lib
build-jar-repository -s lib jaxen glassfish-jaxb-api
%{ant} jar javadoc

%install

# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{base_name}-%{version}.jar %{buildroot}%{_javadir}/%{base_name}.jar

%if %{without bootstrap}
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}.pom
%add_maven_depmap %{base_name}.pom %{base_name}.jar -a %{base_name}:%{base_name}

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{base_name}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/%{base_name}
%fdupes -s %{buildroot}%{_javadocdir}

# demo
install -dm 0755 %{buildroot}%{_datadir}/%{base_name}/src
cp -pr xml %{buildroot}%{_datadir}/%{base_name}
cp -pr src/example %{buildroot}%{_datadir}/%{base_name}/src
%fdupes -s %{buildroot}%{_datadir}/%{base_name}

%files -f .mfiles
%license LICENSE
%doc README.md

%files demo
%{_datadir}/%{base_name}

%files javadoc
%license LICENSE
%{_javadocdir}/%{base_name}

%else

%files
%{_javadir}/%{base_name}.jar

%endif

%changelog
