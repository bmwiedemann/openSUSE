#
# spec file for package glassfish-jax-rs-api
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


Name:           glassfish-jax-rs-api
Version:        2.1.6
Release:        0
Summary:        JAX-RS API Specification (JSR 339)
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/jakartaee/rest
Source0:        https://github.com/jakartaee/rest/archive/refs/tags/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
BuildArch:      noarch

%description
JAX-RS Java API for RESTful Web Services (JSR 339).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n rest-%{version}
find . -name '*.jar' -delete
find . -name '*.class' -delete

# Plugins not needed for RPM builds
%pom_remove_plugin org.apache.maven.plugins:maven-jxr-plugin jaxrs-api
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin jaxrs-api
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin jaxrs-api
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jaxrs-api
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin jaxrs-api

%pom_xpath_remove "pom:build/pom:finalName" jaxrs-api

# Avoid duplicate invokation of javadoc plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions" jaxrs-api

%pom_xpath_remove "pom:profiles" jaxrs-api
rm -f jaxrs-api/src/main/java/module-info.java

%build
pushd jaxrs-api
# Compatibility symlink
%{mvn_file} :{*} @1 %{name}

# Compatibility alias
%{mvn_alias} : javax.ws.rs:javax.ws.rs-api

%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
    -Dsource=8
popd

%install
pushd jaxrs-api
%mvn_install
popd
%fdupes -s %{buildroot}%{_javadocdir}

%files -f jaxrs-api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md CONTRIBUTING.md

%files javadoc -f jaxrs-api/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
