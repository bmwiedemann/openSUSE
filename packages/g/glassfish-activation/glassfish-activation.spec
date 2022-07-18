#
# spec file for package glassfish-activation
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


Name:           glassfish-activation
Version:        1.2.0
Release:        0
Summary:        JavaBeans Activation Framework
License:        (BSD-3-Clause AND GPL-2.0-only WITH Classpath-exception-2.0) OR CDDL-1.1
Group:          Development/Libraries/Java
URL:            https://github.com/javaee/activation
Source0:        activation-%{version}.tar.xz
Source1:        activation-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
Obsoletes:      gnu-jaf < %{version}
Obsoletes:      jaf
BuildArch:      noarch

%description
The JavaBeans Activation Framework (JAF) is a standard extension to the
Java platform that lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to it;
discover the operations available on it; and instantiate the appropriate
bean to perform the operation(s).

%package api
Summary:        JavaBeans Activation Framework API jar
Provides:       gnu-jaf = %{version}
Obsoletes:      gnu-jaf < %{version}
Obsoletes:      jaf

%description api
The JavaBeans Activation Framework (JAF) is a standard extension to the
Java platform that lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to it;
discover the operations available on it; and instantiate the appropriate
bean to perform the operation(s).

This package contains a Java library with only the APIs

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n activation-%{version}
cp %{SOURCE1} activation/build.xml

%pom_disable_module demo

# maven-dependency-plugin doesn't work correctly without access to remote repos
%pom_remove_plugin :maven-dependency-plugin activationapi

%pom_remove_parent activation activationapi
%pom_xpath_inject pom:project "<version>%{version}</version>" activation activationapi

%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%pom_remove_plugin -r :osgiversion-maven-plugin
%pom_xpath_inject pom:project/pom:properties "<activation.osgiversion>\${project.version}</activation.osgiversion>" activation

%build
pushd activation
%{ant} package javadoc
popd

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}/
install -m 644 activation/target/javax.activation-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 activation/target/javax.activation-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
ln -sf %{name}-api.jar %{buildroot}%{_javadir}/activation.jar
ln -sf %{name}-api.jar %{buildroot}%{_javadir}/jaf.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 644 activation/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
install -pm 644 activationapi/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-api.pom
%add_maven_depmap %{name}.pom %{name}.jar
%add_maven_depmap %{name}-api.pom %{name}-api.jar -a javax.activation:activation -f api

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -r activation/target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%triggerpostun api -- gnu-jaf
if [ -f %{_javadir}/%{name}-api.jar ] ; then
    if [ -f %{_javadir}/jaf.jar ] ; then
        rm -f %{_javadir}/jaf.jar
    fi
    ln -sf %{name}-api.jar %{_javadir}/jaf.jar
fi
exit 0

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files api -f .mfiles-api
%{_javadir}/activation.jar
%{_javadir}/jaf.jar
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt
%doc README.md

%changelog
