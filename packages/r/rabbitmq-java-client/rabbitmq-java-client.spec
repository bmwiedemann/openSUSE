#
# spec file for package rabbitmq-java-client
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


%global codegen_version 3.8.9
Name:           rabbitmq-java-client
Version:        5.20.0
Release:        0
Summary:        Java AMQP client library
License:        Apache-2.0 AND GPL-2.0-or-later AND MPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.rabbitmq.com/java-client.html
Source0:        https://github.com/rabbitmq/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/rabbitmq/rabbitmq-codegen/archive/refs/tags/v%{codegen_version}.tar.gz#/rabbitmq-codegen-%{codegen_version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  python3
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
The RabbitMQ Java client library allows Java code to interface to AMQP servers.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -a1

%pom_remove_dep org.junit:junit-bom

# Exclude optional dependencies
%pom_remove_dep io.dropwizard.metrics:metrics-core
rm -f src/main/java/com/rabbitmq/client/impl/StandardMetricsCollector.java

%pom_remove_dep io.micrometer:micrometer-core
rm -f src/main/java/com/rabbitmq/client/impl/MicrometerMetricsCollector.java
rm -rf src/main/java/com/rabbitmq/client/observation/micrometer

%pom_remove_dep io.opentelemetry:opentelemetry-api
rm -f src/main/java/com/rabbitmq/client/impl/OpenTelemetryMetricsCollector.java

%pom_remove_plugin :groovy-maven-plugin

# Exclude *-sources.jar
%pom_remove_plugin :maven-source-plugin

%pom_remove_plugin :keytool-maven-plugin

%pom_xpath_remove pom:project/pom:build/pom:extensions

%build
export PYTHONPATH=rabbitmq-codegen-%{codegen_version}
python3 ./codegen.py header ${PYTHONPATH}/amqp-rabbitmq-0.9.1.json src/main/java/com/rabbitmq/client/AMQP.java
python3 ./codegen.py body ${PYTHONPATH}/amqp-rabbitmq-0.9.1.json src/main/java/com/rabbitmq/client/impl/AMQImpl.java
%{mvn_build} -f -- -DskipTests=true

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE LICENSE-APACHE2 LICENSE-GPL2 LICENSE-MPL-RabbitMQ
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE LICENSE-APACHE2 LICENSE-GPL2 LICENSE-MPL-RabbitMQ

%changelog
