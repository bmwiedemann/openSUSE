#
# spec file for package resteasy
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Stasiek Michalski <stasiek@michalski.cc>.
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


%global namedreltag .Final
%global namedversion %{version}%{namedreltag}
Name:           resteasy
Version:        3.0.26
Release:        0
Summary:        Framework for RESTful Web services and Java applications
License:        Apache-2.0 AND CDDL-1.0
URL:            https://resteasy.jboss.org/
Source0:        https://github.com/resteasy/Resteasy/archive/%{namedversion}/Resteasy-%{namedversion}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.slf4j:slf4j-api)
Requires:       resteasy-atom-provider = %{version}-%{release}
Requires:       resteasy-client = %{version}-%{release}
Requires:       resteasy-core = %{version}-%{release}
Requires:       resteasy-jackson2-provider = %{version}-%{release}
Requires:       resteasy-jaxb-provider = %{version}-%{release}
BuildArch:      noarch

%description

%global desc \
RESTEasy contains a JBoss project that provides frameworks to help\
build RESTful Web Services and RESTful Java applications. It is a fully\
certified and portable implementation of the JAX-RS specification.
%global extdesc %{desc}\
\
This package contains
%{desc}

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
This package contains the API documentation for %{name}.

%package        core
Summary:        Core modules for %{name}

%description    core
%{extdesc} %{summary}.

%package        atom-provider
Summary:        Module atom-provider for %{name}

%description    atom-provider
%{extdesc} %{summary}.

%package        jackson2-provider
Summary:        Module jackson2-provider for %{name}

%description    jackson2-provider
%{extdesc} %{summary}.

%package        jaxb-provider
Summary:        Module jaxb-provider for %{name}

%description    jaxb-provider
%{extdesc} %{summary}.

%package        client
Summary:        Client for %{name}

%description    client
%{extdesc} %{summary}.

%prep
%setup -q -n Resteasy-%{namedversion}

%pom_disable_module arquillian
%pom_disable_module eagledns
%pom_disable_module jboss-modules
%pom_disable_module profiling-tests
%pom_disable_module resteasy-bom
%pom_disable_module resteasy-cache
%pom_disable_module resteasy-cdi
%pom_disable_module resteasy-dependencies-bom
%pom_disable_module resteasy-guice
%pom_disable_module resteasy-jaxrs-testsuite
%pom_disable_module resteasy-jsapi
%pom_disable_module resteasy-jsapi-testing
%pom_disable_module resteasy-links
%pom_disable_module resteasy-servlet-initializer
%pom_disable_module resteasy-spring
%pom_disable_module resteasy-wadl
%pom_disable_module resteasy-wadl-undertow-connector
%pom_disable_module security
%pom_disable_module server-adapters
%pom_disable_module testsuite
%pom_disable_module tjws

pushd providers
%pom_disable_module fastinfoset
%pom_disable_module jackson
%pom_disable_module jettison
%pom_disable_module json-p-ee7
%pom_disable_module multipart
%pom_disable_module resteasy-html
%pom_disable_module resteasy-validator-provider-11
%pom_disable_module yaml
popd

find -name '*.jar' -print -delete

%pom_remove_plugin :maven-clover2-plugin

# remove activation.jar dependencies
%pom_remove_dep -r javax.activation:activation resteasy-jaxrs resteasy-spring

# remove resteasy-dependencies pom
%pom_remove_dep "org.jboss.resteasy:resteasy-dependencies"

# remove redundant jcip-dependencies dep from resteasy-jaxrs
%pom_remove_dep net.jcip:jcip-annotations resteasy-jaxrs

# remove junit dependency from all modules
%pom_remove_dep junit:junit resteasy-client
%pom_remove_dep junit:junit providers/resteasy-atom
%pom_remove_dep junit:junit providers/jaxb
%pom_remove_dep junit:junit resteasy-jaxrs

# depend on servlet-api from pki-servlet-4.0-api
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api resteasy-jaxrs
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/abdera-atom
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jaxb
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jackson2

%pom_remove_plugin :maven-clean-plugin

%{mvn_package} ":resteasy-jaxrs" core
%{mvn_package} ":providers-pom" core
%{mvn_package} ":resteasy-jaxrs-all" core
%{mvn_package} ":resteasy-pom" core
%{mvn_package} ":resteasy-atom-provider" atom-provider
%{mvn_package} ":resteasy-jackson2-provider" jackson2-provider
%{mvn_package} ":resteasy-jaxb-provider" jaxb-provider
%{mvn_package} ":resteasy-client" client

# Disable useless artifacts generation, package __noinstall do not work
%pom_add_plugin org.apache.maven.plugins:maven-source-plugin . '
<configuration>
 <skipSource>true</skipSource>
</configuration>'

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install

%files
%doc README.md
%license License.html

%files core -f .mfiles-core
%license License.html

%files atom-provider -f .mfiles-atom-provider
%license License.html

%files jackson2-provider -f .mfiles-jackson2-provider
%license License.html

%files jaxb-provider -f .mfiles-jaxb-provider
%license License.html

%files client -f .mfiles-client
%license License.html

%files javadoc -f .mfiles-javadoc
%license License.html

%changelog
