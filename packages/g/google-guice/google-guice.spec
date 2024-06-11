#
# spec file for package google-guice
#
# Copyright (c) 2024 SUSE LLC
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
Version:        6.0.0
Release:        0
Summary:        Dependency injection framework for Java 5 and above
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/%{short_name}
# ./create-tarball.sh %%{version}
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  aopalliance
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  google-errorprone-annotations
BuildRequires:  guava
BuildRequires:  jakarta-inject
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsr-305
BuildRequires:  objectweb-asm
Provides:       %{short_name}-multibindings = %{version}
Obsoletes:      %{short_name}-multibindings < %{version}
Obsoletes:      %{short_name}-testlibs
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

%description -n %{short_name}-assistedinject
Guice is a dependency injection framework for Java 5
and above. This package provides AssistedInject module for Guice.

%package -n %{short_name}-extensions
Summary:        Extensions for Guice
Group:          Development/Libraries/Java

%description -n %{short_name}-extensions
Guice is a dependency injection framework for Java 5
and above. This package provides extensions POM for Guice.

%package -n %{short_name}-grapher
Summary:        Grapher extension module for Guice
Group:          Development/Libraries/Java

%description -n %{short_name}-grapher
Guice is a dependency injection framework for Java 5
and above. This package provides Grapher module for Guice.

%package -n %{short_name}-jmx
Summary:        JMX extension module for Guice
Group:          Development/Libraries/Java

%description -n %{short_name}-jmx
Guice is a dependency injection framework for Java 5
and above. This package provides JMX module for Guice.

%package -n %{short_name}-jndi
Summary:        JNDI extension module for Guice
Group:          Development/Libraries/Java

%description -n %{short_name}-jndi
Guice is a dependency injection framework for Java 5
and above. This package provides JNDI module for Guice.

%package -n %{short_name}-servlet
Summary:        Servlet extension module for Guice
Group:          Development/Libraries/Java

%description -n %{short_name}-servlet
Guice is a dependency injection framework for Java 5
and above. This package provides Servlet module for Guice.

%package -n %{short_name}-throwingproviders
Summary:        ThrowingProviders extension module for Guice
Group:          Development/Libraries/Java

%description -n %{short_name}-throwingproviders
Guice is a dependency injection framework for Java 5
and above. This package provides ThrowingProviders module for Guice.

%package -n %{short_name}-bom
Summary:        Bill of Materials for Guice
Group:          Development/Libraries/Java

%description -n %{short_name}-bom
Guice is a dependency injection framework for Java 5
and above. This package provides Bill of Materials module for Guice.

%package javadoc
Summary:        API documentation for Guice
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -a1

# We don't have struts2.
%pom_disable_module struts2 extensions
# Android-specific extension
%pom_disable_module dagger-adapter extensions

# Remove additional build profiles, which we don't use anyways
# and which are only pulling additional dependencies.
%pom_xpath_remove "pom:profile[pom:id='guice.with.jarjar']" core

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
%pom_xpath_remove "pom:dependency[pom:classifier='tests']" extensions

%pom_remove_parent

%pom_disable_module persist extensions
%pom_disable_module spring extensions
%pom_disable_module testlib extensions

%build
mkdir -p lib
build-jar-repository -s lib \
    aopalliance \
    atinject \
    glassfish-servlet-api \
    google-errorprone/annotations \
    guava/guava \
    jakarta-inject \
    jsr-305 \
    objectweb-asm/asm \

%{ant} -Dtest.skip=true package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{short_name}
install -pm 0644 core/target/guice-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{name}.jar
# Provide symlinks for all jars that existed, no_aop and aop
ln -sf %{short_name}/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}/%{name}-no_aop.jar
ln -sf %{short_name}/%{name}.jar %{buildroot}%{_javadir}/%{name}-no_aop.jar

install -pm 0644 extensions/jmx/target/guice-jmx-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-jmx.jar
install -pm 0644 extensions/assistedinject/target/guice-assistedinject-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-assistedinject.jar
install -pm 0644 extensions/throwingproviders/target/guice-throwingproviders-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-throwingproviders.jar
install -pm 0644 extensions/servlet/target/guice-servlet-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-servlet.jar
install -pm 0644 extensions/jndi/target/guice-jndi-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-jndi.jar
install -pm 0644 extensions/grapher/target/guice-grapher-%{version}.jar \
    %{buildroot}%{_javadir}/%{short_name}/guice-grapher.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{short_name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-parent.pom
%add_maven_depmap %{short_name}/guice-parent.pom -f parent
%{mvn_install_pom} bom/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-bom.pom
%add_maven_depmap %{short_name}/guice-bom.pom -f bom
%{mvn_install_pom} extensions/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/extensions-parent.pom
%add_maven_depmap %{short_name}/extensions-parent.pom -a org.sonatype.sisu.inject:extensions-parent -f extensions

%{mvn_install_pom} core/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/%{name}.pom
%add_maven_depmap %{short_name}/%{name}.pom %{short_name}/%{name}.jar -a "org.sonatype.sisu:sisu-guice,com.google.inject:guice::no_aop:,org.sonatype.sisu:sisu-guice::no_aop:"

%{mvn_install_pom} extensions/jmx/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-jmx.pom
%add_maven_depmap %{short_name}/guice-jmx.pom %{short_name}/guice-jmx.jar -a org.sonatype.sisu.inject:guice-jmx -f jmx
%{mvn_install_pom} extensions/assistedinject/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-assistedinject.pom
%add_maven_depmap %{short_name}/guice-assistedinject.pom %{short_name}/guice-assistedinject.jar -a org.sonatype.sisu.inject:guice-assistedinject -f assistedinject
%{mvn_install_pom} extensions/throwingproviders/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-throwingproviders.pom
%add_maven_depmap %{short_name}/guice-throwingproviders.pom %{short_name}/guice-throwingproviders.jar -a org.sonatype.sisu.inject:guice-throwingproviders -f throwingproviders
%{mvn_install_pom} extensions/servlet/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-servlet.pom
%add_maven_depmap %{short_name}/guice-servlet.pom %{short_name}/guice-servlet.jar -a org.sonatype.sisu.inject:guice-servlet -f servlet
%{mvn_install_pom} extensions/jndi/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-jndi.pom
%add_maven_depmap %{short_name}/guice-jndi.pom %{short_name}/guice-jndi.jar -a org.sonatype.sisu.inject:guice-jndi -f jndi
%{mvn_install_pom} extensions/grapher/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}/guice-grapher.pom
%add_maven_depmap %{short_name}/guice-grapher.pom %{short_name}/guice-grapher.jar -a org.sonatype.sisu.inject:guice-grapher -f grapher

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr core/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
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

%files -n %{short_name}-servlet -f .mfiles-servlet

%files -n %{short_name}-throwingproviders -f .mfiles-throwingproviders

%files -n %{short_name}-bom -f .mfiles-bom

%files javadoc
%{_javadocdir}/%{name}
%license COPYING

%changelog
