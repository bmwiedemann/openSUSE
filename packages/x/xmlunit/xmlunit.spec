#
# spec file for package xmlunit
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           xmlunit
Version:        2.11.0
Release:        0
Summary:        XMLUnit for Java
License:        Apache-2.0 AND BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.xmlunit.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  assertj-core
BuildRequires:  fdupes
BuildRequires:  glassfish-jaxb-api
BuildRequires:  hamcrest
BuildRequires:  javapackages-local >= 6
BuildRequires:  jaxb-api
BuildRequires:  junit
BuildRequires:  jurand
BuildArch:      noarch

%description
XMLUnit provides you with the tools to verify the XML you emit is the one you
want to create. It provides helpers to validate against an XML Schema, assert
the values of XPath queries or compare XML documents against expected outcomes.

%package assertj
Summary:        XMLUnit with AssertJ fluent API
License:        Apache-2.0
Group:          Development/Libraries/Java

%description assertj
This package provides %{summary}.

%package core
Summary:        XMLUnit for Java core package
License:        Apache-2.0
Group:          Development/Libraries/Java

%description core
This package provides %{summary}.

%package jakarta-jaxb-impl
Summary:        XMLUnit for Java JAXB support using Jakarta EE packages
License:        Apache-2.0
Group:          Development/Libraries/Java

%description jakarta-jaxb-impl
This package provides %{summary}.

%package legacy
Summary:        XMLUnit 1.x Compatibility Layer
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description legacy
This package provides %{summary}.

%package matchers
Summary:        XMLUnit for Java Hamcrest Matchers
License:        Apache-2.0
Group:          Development/Libraries/Java

%description matchers
This package provides %{summary}.

%package placeholders
Summary:        XMLUnit for Java Placeholder DSL for Comparisons
License:        Apache-2.0
Group:          Development/Libraries/Java

%description placeholders
This package provides %{summary}.

%package javadoc
Summary:        Javadoc for %{name}
License:        Apache-2.0
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}. Also contains userguide.

%prep
%autosetup -p1 -a1

# Port to hamcrest 2.1
%{java_remove_annotations} xmlunit-matchers -p org[.]hamcrest[.]Factory

%pom_disable_module xmlunit-assertj

%build
mkdir -p lib
build-jar-repository -s lib \
    assertj-core/assertj-core \
    glassfish-jaxb-api \
    hamcrest/hamcrest \
    jaxb-api/jakarta.xml.bind-api \
    junit
ant package javadoc

%install
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
for i in assertj3 core jakarta-jaxb-impl legacy matchers placeholders; do
  cp -r %{name}-${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
  install -pm 0644 %{name}-${i}/target/%{name}-${i}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
  %{mvn_install_pom} %{name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${i}.pom
  if [ "${i}" = legacy ]; then
    %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar -a xmlunit:xmlunit -f ${i}
  elif [ "${i}" = assertj3 ]; then
    %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar -a org.xmlunit:xmlunit-assertj -f ${i}
  else
    %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar -f ${i}
  fi
done
ln -s -f %{name}/%{name}-legacy.jar %{buildroot}%{_javadir}/%{name}.jar
%fdupes -s %{buildroot}%{_javadocdir}

%files assertj -f .mfiles-assertj3

%files core -f .mfiles-core
%doc README.md CONTRIBUTING.md RELEASE_NOTES.md
%license LICENSE

%files jakarta-jaxb-impl -f .mfiles-jakarta-jaxb-impl

%files legacy -f .mfiles-legacy
%{_javadir}/%{name}.jar

%files matchers -f .mfiles-matchers

%files placeholders -f .mfiles-placeholders

%files javadoc
%{_javadocdir}/%{name}

%changelog
