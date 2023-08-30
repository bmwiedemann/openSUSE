#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global base_name jaxen
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%bcond_without dom4j
Version:        1.2.0
Release:        0
Summary:        An XPath engine written in Java
License:        BSD-3-Clause
URL:            https://github.com/jaxen-xpath/jaxen
Source0:        %{url}/archive/v%{version}/%{base_name}-%{version}.tar.gz
Source1:        %{base_name}-build.xml
BuildRequires:  ant
BuildRequires:  javapackages-local >= 6
BuildRequires:  jdom
BuildRequires:  xerces-j2
BuildRequires:  xml-apis
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-bootstrap
%else
Name:           %{base_name}
%endif
%if %{without bootstrap}
BuildRequires:  %{base_name}-bootstrap
BuildRequires:  dom4j-bootstrap
BuildRequires:  fdupes
BuildRequires:  xom
#!BuildIgnore:  %{base_name}
#!BuildIgnore:  mvn(jaxen:jaxen)
Conflicts:      %{base_name}-bootstrap
Obsoletes:      %{base_name}-bootstrap
%else
Conflicts:      %{base_name}
%endif

%description
Jaxen is an open source XPath library written in Java. It is adaptable
to many different object models, including DOM, XOM, dom4j, and JDOM.
Is it also possible to write adapters that treat non-XML trees such as compiled
Java byte code or Java beans as XML, thus enabling you to query these trees
with XPath too.

%if %{without bootstrap}
%package        demo
Summary:        Samples for %{name}
Requires:       %{name} = %{version}-%{release}

%description    demo
%{summary}.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
%{summary}.
%endif

%prep
%setup -q -n %{base_name}-%{version}
cp %{SOURCE1} build.xml

%if %{with bootstrap}
rm -rf src/java/main/org/jaxen/dom4j
%pom_remove_dep dom4j:dom4j

rm -rf src/java/main/org/jaxen/xom
%pom_remove_dep xom:xom
%endif

%build
mkdir -p lib
build-jar-repository -s lib xml-apis xerces-j2 jdom
%if %{without bootstrap}
build-jar-repository -s lib dom4j xom
%endif
%{ant} jar
%if %{without bootstrap}
%{ant} javadoc
%endif

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{base_name}-%{version}.jar %{buildroot}%{_javadir}/%{base_name}.jar

%if %{without bootstrap}
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}.pom
%add_maven_depmap %{base_name}.pom %{base_name}.jar

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{base_name}/samples
cp -pr src/java/samples/* %{buildroot}%{_datadir}/%{base_name}/samples
%fdupes -s %{buildroot}%{_datadir}/%{base_name}

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{base_name}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/%{base_name}
%fdupes -s %{buildroot}%{_javadocdir}/%{base_name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{base_name}

%files demo
%{_datadir}/%{base_name}

%else

%files
%{_javadir}/%{base_name}.jar

%endif

%changelog
