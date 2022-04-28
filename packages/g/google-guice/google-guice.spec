#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global short_name guice
Name:           google-%{short_name}
Version:        4.1
Release:        0
Summary:        Dependency injection framework for Java 5 and above
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/%{short_name}
# ./create-tarball.sh %%{version}
Source0:        %{name}-%{version}.tar.xz
Source1:        create-tarball.sh
Patch0:         guice-4.1-fixup-ant.patch
Patch1:         guice-4.1-disabledextensions.patch
Patch2:         guice-4.1-javadoc.patch
Patch3:         google-guice-throwingproviderbinder.patch
BuildRequires:  ant
BuildRequires:  aqute-bnd
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  guava
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Requires:       mvn(com.google.guava:guava)
Requires:       mvn(javax.inject:javax.inject)
BuildArch:      noarch

%description
Guice alleviates the need for factories and the use of "new" in Java
code. Guice's @Inject is a different "new". Writing factories will
still be needed in some cases, but code will not directly depend on
them.

Guice embraces Java's type safe nature, especially when it comes to
features introduced in Java 5 such as generics and annotations.

%package -n %{short_name}-parent
Summary:        Guice parent POM
Group:          Development/Libraries/Java

%description -n %{short_name}-parent
Guice is a dependency injection framework for Java 5
and above. This package provides parent POM for Guice modules.

%package -n %{short_name}-assistedinject
Summary:        AssistedInject extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-assistedinject
Guice is a dependency injection framework for Java 5
and above. This package provides AssistedInject module for Guice.

%package -n %{short_name}-extensions
Summary:        Extensions for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice-parent:pom:)

%description -n %{short_name}-extensions
Guice is a dependency injection framework for Java 5
and above. This package provides extensions POM for Guice.

%package -n %{short_name}-grapher
Summary:        Grapher extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject.extensions:guice-assistedinject)
Requires:       mvn(com.google.inject.extensions:guice-multibindings)
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-grapher
Guice is a dependency injection framework for Java 5
and above. This package provides Grapher module for Guice.

%package -n %{short_name}-jmx
Summary:        JMX extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-jmx
Guice is a dependency injection framework for Java 5
and above. This package provides JMX module for Guice.

%package -n %{short_name}-jndi
Summary:        JNDI extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-jndi
Guice is a dependency injection framework for Java 5
and above. This package provides JNDI module for Guice.

%package -n %{short_name}-multibindings
Summary:        MultiBindings extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-multibindings
Guice is a dependency injection framework for Java 5
and above. This package provides MultiBindings module for Guice.

%package -n %{short_name}-servlet
Summary:        Servlet extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-servlet
Guice is a dependency injection framework for Java 5
and above. This package provides Servlet module for Guice.

%package -n %{short_name}-testlib
Summary:        TestLib extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-testlib
Guice is a dependency injection framework for Java 5
and above. This package provides TestLib module for Guice.

%package -n %{short_name}-throwingproviders
Summary:        ThrowingProviders extension module for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice)

%description -n %{short_name}-throwingproviders
Guice is a dependency injection framework for Java 5
and above. This package provides ThrowingProviders module for Guice.

%package -n %{short_name}-bom
Summary:        Bill of Materials for Guice
Group:          Development/Libraries/Java
Requires:       mvn(com.google.inject:guice-parent:pom:)

%description -n %{short_name}-bom
Guice is a dependency injection framework for Java 5
and above. This package provides Bill of Materials module for Guice.

%package javadoc
Summary:        API documentation for Guice
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
find . -name "*.jar" -and ! -name "munge.jar" -delete
find . -name "*.class" -delete

%pom_disable_module struts2 extensions
# Android-specific extension
%pom_disable_module dagger-adapter extensions

# Fix OSGi metadata due to not using jarjar
%pom_xpath_set "pom:instructions/pom:Import-Package" \
  "!com.google.inject.*,*" core

# Animal sniffer is only causing problems. Disable it for now.
%pom_remove_plugin :animal-sniffer-maven-plugin core
%pom_remove_plugin :animal-sniffer-maven-plugin extensions

%pom_remove_plugin :maven-gpg-plugin

# We don't have the custom doclet used by upstream. Remove
# maven-javadoc-plugin to generate javadocs with default style.
%pom_remove_plugin -r :maven-javadoc-plugin

# remove test dependency to make sure we don't produce requires
# see #1007498
%pom_remove_dep :guava-testlib extensions
%pom_xpath_remove "pom:dependency[pom:classifier[text()='tests']]" extensions

%pom_change_dep -r -f ::::: :::::
%pom_remove_parent

%pom_remove_parent core
%pom_xpath_inject pom:project "
  <groupId>com.google.inject</groupId>
  <version>4.1.0</version>" core

for mdl in assistedinject dagger-adapter grapher jmx jndi multibindings persist servlet spring struts2 testlib throwingproviders; do
  %pom_remove_parent extensions/${mdl}
  %pom_xpath_inject pom:project "
  <groupId>com.google.inject.extensions</groupId>
  <version>4.1.0</version>" extensions/${mdl}
done

%pom_disable_module persist extensions
%pom_disable_module spring extensions

%pom_disable_module jdk8-tests

%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-bundle-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_plugin :maven-remote-resources-plugin extensions
%pom_remove_plugin :maven-bundle-plugin extensions
%pom_remove_plugin :maven-source-plugin extensions

%pom_xpath_remove "pom:dependency[pom:scope[text()='test']]" core
%pom_xpath_remove "pom:profiles" core
%pom_xpath_remove "pom:build" core
%pom_xpath_remove "pom:optional" core

%build
mkdir -p lib/build
build-jar-repository -s -p lib/build \
  guava javax.inject glassfish-servlet-api aqute-bnd
%{ant} clean.all no_aop
pushd build/no_aop
mkdir -p extensions/servlet/lib/build
%pom_remove_dep :aopalliance core
%pom_remove_dep :asm core
%pom_remove_dep :cglib core
%{ant} -Dversion=%{version} dist javadoc
popd

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{short_name}
install -pm 0644 build/no_aop/build/guice-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{name}.jar
# Provide symlinks for all jars that existed, no_aop and aop
ln -sf %{short_name}/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}/%{name}-no_aop.jar
ln -sf %{short_name}/%{name}.jar %{buildroot}%{_javadir}/%{name}-no_aop.jar

install -pm 0644 build/no_aop/build/dist/guice-jmx-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-jmx.jar
install -pm 0644 build/no_aop/build/dist/guice-assistedinject-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-assistedinject.jar
install -pm 0644 build/no_aop/build/dist/guice-multibindings-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-multibindings.jar
install -pm 0644 build/no_aop/build/dist/guice-throwingproviders-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-throwingproviders.jar
install -pm 0644 build/no_aop/build/dist/guice-servlet-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-servlet.jar
install -pm 0644 build/no_aop/build/dist/guice-jndi-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-jndi.jar
install -pm 0644 build/no_aop/build/dist/guice-testlib-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-testlib.jar
install -pm 0644 build/no_aop/build/dist/guice-grapher-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-grapher.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{short_name}
install -pm 0644 build/no_aop/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-parent.pom
%add_maven_depmap %{short_name}/guice-parent.pom -f parent
install -pm 0644 build/no_aop/bom/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-bom.pom
%add_maven_depmap %{short_name}/guice-bom.pom -f bom
install -pm 0644 build/no_aop/extensions/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/extensions-parent.pom
%add_maven_depmap %{short_name}/extensions-parent.pom -a org.sonatype.sisu.inject:extensions-parent -f extensions

install -pm 0644 build/no_aop/core/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/%{name}.pom
%add_maven_depmap %{short_name}/%{name}.pom %{short_name}/%{name}.jar -a "org.sonatype.sisu:sisu-guice,com.google.inject:guice::no_aop:,org.sonatype.sisu:sisu-guice::no_aop:"

install -pm 0644 build/no_aop/extensions/jmx/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-jmx.pom
%add_maven_depmap %{short_name}/guice-jmx.pom %{short_name}/guice-jmx.jar -a org.sonatype.sisu.inject:guice-jmx -f jmx
install -pm 0644 build/no_aop/extensions/assistedinject/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-assistedinject.pom
%add_maven_depmap %{short_name}/guice-assistedinject.pom %{short_name}/guice-assistedinject.jar -a org.sonatype.sisu.inject:guice-assistedinject -f assistedinject
install -pm 0644 build/no_aop/extensions/multibindings/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-multibindings.pom
%add_maven_depmap %{short_name}/guice-multibindings.pom %{short_name}/guice-multibindings.jar -a org.sonatype.sisu.inject:guice-multibindings -f multibindings
install -pm 0644 build/no_aop/extensions/throwingproviders/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-throwingproviders.pom
%add_maven_depmap %{short_name}/guice-throwingproviders.pom %{short_name}/guice-throwingproviders.jar -a org.sonatype.sisu.inject:guice-throwingproviders -f throwingproviders
install -pm 0644 build/no_aop/extensions/servlet/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-servlet.pom
%add_maven_depmap %{short_name}/guice-servlet.pom %{short_name}/guice-servlet.jar -a org.sonatype.sisu.inject:guice-servlet -f servlet
install -pm 0644 build/no_aop/extensions/jndi/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-jndi.pom
%add_maven_depmap %{short_name}/guice-jndi.pom %{short_name}/guice-jndi.jar -a org.sonatype.sisu.inject:guice-jndi -f jndi
install -pm 0644 build/no_aop/extensions/testlib/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-testlib.pom
%add_maven_depmap %{short_name}/guice-testlib.pom %{short_name}/guice-testlib.jar -a org.sonatype.sisu.inject:guice-testlib -f testlib
install -pm 0644 build/no_aop/extensions/grapher/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-grapher.pom
%add_maven_depmap %{short_name}/guice-grapher.pom %{short_name}/guice-grapher.jar -a org.sonatype.sisu.inject:guice-grapher -f grapher

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/no_aop/build/docs/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_javadir}/%{short_name}
%{_javadir}/%{name}*.jar
%{_javadir}/%{short_name}/*-no_aop.jar

%files -n %{short_name}-parent -f .mfiles-parent
%license COPYING

%files -n %{short_name}-assistedinject -f .mfiles-assistedinject

%files -n %{short_name}-extensions -f .mfiles-extensions

%files -n %{short_name}-grapher -f .mfiles-grapher

%files -n %{short_name}-jmx -f .mfiles-jmx

%files -n %{short_name}-jndi -f .mfiles-jndi

%files -n %{short_name}-multibindings -f .mfiles-multibindings

%files -n %{short_name}-servlet -f .mfiles-servlet

%files -n %{short_name}-testlib -f .mfiles-testlib

%files -n %{short_name}-throwingproviders -f .mfiles-throwingproviders

%files -n %{short_name}-bom -f .mfiles-bom

%files javadoc
%{_javadocdir}/%{name}
%license COPYING

%changelog
