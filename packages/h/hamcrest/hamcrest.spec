#
# spec file for package hamcrest
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


%bcond_with jmock
%bcond_with easymock
Name:           hamcrest
Version:        1.3
Release:        0
Summary:        Library of matchers for building test expressions
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/hamcrest/JavaHamcrest
Source0:        https://github.com/hamcrest/JavaHamcrest/archive/hamcrest-java-%{version}.tar.gz
Source8:        hamcrest-core-MANIFEST.MF
Source9:        hamcrest-library-MANIFEST.MF
Source11:       hamcrest-integration-MANIFEST.MF
Source12:       hamcrest-generator-MANIFEST.MF
Patch0:         %{name}-%{version}-build.patch
Patch1:         %{name}-%{version}-no-jarjar.patch
Patch3:         %{name}-%{version}-javadoc.patch
Patch4:         %{name}-%{version}-qdox-2.0.patch
Patch5:         %{name}-%{version}-fork-javac.patch
Patch6:         %{name}-%{version}-javadoc9.patch
Patch7:         %{name}-%{version}-javadoc10.patch
Patch8:         %{name}-%{version}-random-build-crash.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  qdox >= 2.0
Requires:       %{name}-core = %{version}-%{release}
Requires:       qdox >= 2.0
BuildArch:      noarch
%if %{with jmock}
BuildRequires:  jmock
Requires:       jmock
%endif
%if %{with easymock}
BuildRequires:  easymock
Requires:       easymock
%endif

%description
Provides a library of matcher objects (also known as constraints or
predicates) allowing 'match' rules to be defined declaratively, to be
used in other frameworks. Typical scenarios include testing frameworks,
mocking libraries and UI validation rules.

%package core
Summary:        Core API of hamcrest matcher framework.
Group:          Development/Libraries/Java

%description core
The core API of hamcrest matcher framework to be used by third-party framework providers.
This includes the a foundation set of matcher implementations for common operations.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo files for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
Requires:       junit

%description demo
Demo files for %{name}.

%prep
%setup -q -n JavaHamcrest-%{name}-java-%{version}

find . -type f -name "*.jar" | xargs -t rm
ln -sf $(build-classpath qdox) lib/generator/
%if %{with jmock}
ln -sf $(build-classpath jmock) lib/integration/
%else
rm -fr hamcrest-integration/src/main/java/org/hamcrest/integration/JMock1Adapter.java
rm -fr hamcrest-integration/src/main/java/org/hamcrest/JMock1Matchers.java
rm -fr hamcrest-unit-test/src/main/java/org/hamcrest/integration/JMock1AdapterTest.java
%endif
%if %{with easymock}
ln -sf $(build-classpath easymock3) lib/integration/
%else
rm -fr hamcrest-integration/src/main/java/org/hamcrest/integration/EasyMock2Adapter.java
rm -fr hamcrest-integration/src/main/java/org/hamcrest/EasyMock2Matchers.java
%endif

%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

sed -i 's/\r//' LICENSE.txt

%build
export CLASSPATH=$(build-classpath qdox)
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 -Dversion=%{version} -Dbuild.sysclasspath=last clean core generator library bigjar javadoc

# inject OSGi manifests
jar ufm build/%{name}-core-%{version}.jar %{SOURCE8}
jar ufm build/%{name}-library-%{version}.jar %{SOURCE9}
jar ufm build/%{name}-integration-%{version}.jar %{SOURCE11}
jar ufm build/%{name}-generator-%{version}.jar %{SOURCE12}

%install
sed -i 's/@VERSION@/%{version}/g' pom/*.pom

# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}

rm -f pom/%{name}-parent.pom
for i in pom/%{name}*.pom; do
  %pom_remove_parent ${i}
  %pom_xpath_inject "pom:project" "
  <groupId>org.hamcrest</groupId>
  <version>%{version}</version>" ${i}
done

install -m 644 build/%{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}/core.jar
install -m 644 pom/%{name}-core.pom %{buildroot}%{_mavenpomdir}/%{name}/core.pom
%add_maven_depmap %{name}/core.pom %{name}/core.jar -f core

install -m 644 build/%{name}-all-%{version}.jar %{buildroot}%{_javadir}/%{name}/all.jar
install -m 644 pom/%{name}-all.pom %{buildroot}%{_mavenpomdir}/%{name}/all.pom
%add_maven_depmap %{name}/all.pom %{name}/all.jar

install -m 644 build/%{name}-generator-%{version}.jar %{buildroot}%{_javadir}/%{name}/generator.jar
install -m 644 pom/%{name}-generator.pom %{buildroot}%{_mavenpomdir}/%{name}/generator.pom
%add_maven_depmap %{name}/generator.pom %{name}/generator.jar

install -m 644 build/%{name}-integration-%{version}.jar %{buildroot}%{_javadir}/%{name}/integration.jar
install -m 644 pom/%{name}-integration.pom %{buildroot}%{_mavenpomdir}/%{name}/integration.pom
%add_maven_depmap %{name}/integration.pom %{name}/integration.jar

install -m 644 build/%{name}-library-%{version}.jar %{buildroot}%{_javadir}/%{name}/library.jar
install -m 644 pom/%{name}-library.pom %{buildroot}%{_mavenpomdir}/%{name}/library.pom
%add_maven_depmap %{name}/library.pom %{name}/library.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/temp/hamcrest-all-%{version}-javadoc.jar.contents/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr %{name}-examples %{buildroot}%{_datadir}/%{name}/

%files -f .mfiles
%defattr(0644,root,root,0755)
%license LICENSE.txt

%files core -f .mfiles-core
%defattr(0644,root,root,0755)
%license LICENSE.txt

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%changelog
