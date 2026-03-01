#
# spec file for package plexus-compiler
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           plexus-compiler
Version:        2.16.2
Release:        0
Summary:        Compiler call initiators for Plexus
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-compiler
Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        LICENSE.MIT
Source100:      %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  ecj
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  objectweb-asm
BuildRequires:  plexus-utils
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildArch:      noarch

%description
Plexus Compiler adds support for using various compilers from a
unified api. Support for javac is available in main package. For
additional compilers see %{name}-extras package.

%package extras
Summary:        Extra compiler support for %{name}
License:        Apache-2.0
Group:          Development/Libraries/Java

%description extras
Additional support for csharp, eclipse and jikes compilers

%package javadoc
Summary:        Javadoc for %{name}
License:        Apache-1.1 AND Apache-2.0 AND MIT
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version} -a100

cp %{SOURCE1} LICENSE
cp %{SOURCE2} LICENSE.MIT

%pom_disable_module plexus-compiler-aspectj plexus-compilers
# missing com.google.errorprone:error_prone_core
%pom_disable_module plexus-compiler-javac-errorprone plexus-compilers

# don't build/install compiler-test module, it needs maven2 test harness
%pom_disable_module plexus-compiler-test

# don't generate requires on test dependency (see #1007498)
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='plexus-compiler-test']]" plexus-compilers

%pom_change_dep org.codehaus.plexus:plexus-testing :::test plexus-compilers/plexus-compiler-eclipse

%pom_remove_dep -r :plexus-xml

%pom_remove_plugin :maven-site-plugin

%build
mkdir -p lib
build-jar-repository -s lib \
  atinject \
  ecj \
  objectweb-asm/asm \
  org.eclipse.sisu.inject \
  org.eclipse.sisu.plexus \
  plexus/utils \
  slf4j/api

# Tests are skipped because of unavailable plexus-compiler-test artifact
%{ant} \
  -Dtest.skip=true \
  package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
for i in plexus-compiler-api plexus-compiler-manager \
    plexus-compilers/plexus-compiler-csharp \
    plexus-compilers/plexus-compiler-eclipse \
    plexus-compilers/plexus-compiler-javac; do
  install -pm 0644 ${i}/target/$(basename ${i})-%{version}.jar %{buildroot}%{_javadir}/%{name}/$(basename ${i}).jar
done

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
# These ones belong to the *-extras package
for i in plexus-compilers/plexus-compiler-csharp \
    plexus-compilers/plexus-compiler-eclipse; do
  bsnm=$(basename ${i})
  %{mvn_install_pom} ${i}/pom.xml  %{buildroot}%{_mavenpomdir}/%{name}/$bsnm.pom
  %add_maven_depmap %{name}/$bsnm.pom %{name}/$bsnm.jar -f extras
done
# These ones end-up in the main package
for i in plexus-compiler-api plexus-compiler-manager \
    plexus-compilers/plexus-compiler-javac; do
  bsnm=$(basename ${i})
  %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/$bsnm.pom
  %add_maven_depmap %{name}/$bsnm.pom %{name}/$bsnm.jar
done

# javadoc
for i in plexus-compiler-api plexus-compiler-manager \
    plexus-compilers/plexus-compiler-javac \
    plexus-compilers/plexus-compiler-csharp \
    plexus-compilers/plexus-compiler-eclipse; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/${i}
  cp -pr ${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE LICENSE.MIT

%files extras -f .mfiles-extras

%files javadoc
%license LICENSE LICENSE.MIT
%{_javadocdir}/%{name}

%changelog
