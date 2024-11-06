#
# spec file for package jackson-jaxrs-providers
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


Name:           jackson-jaxrs-providers
Version:        2.17.3
Release:        0
Summary:        Jackson JAX-RS providers
License:        Apache-2.0
URL:            https://github.com/FasterXML/jackson-jaxrs-providers
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildArch:      noarch

%description
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats: JSON, Smile (binary JSON), XML, CBOR (another kind of
binary JSON), YAML.

%package -n jackson-jaxrs-json-provider
Summary:        Jackson-JAXRS-JSON

%description -n jackson-jaxrs-json-provider
Functionality to handle JSON input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%if %{without jp_minimal}
%package -n jackson-jaxrs-cbor-provider
Summary:        Jackson-JAXRS-CBOR

%description -n jackson-jaxrs-cbor-provider
Functionality to handle CBOR encoded input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n jackson-jaxrs-smile-provider
Summary:        Jackson-JAXRS-Smile

%description -n jackson-jaxrs-smile-provider
Functionality to handle Smile (binary JSON) input/output for
JAX-RS implementations (like Jersey and RESTeasy) using standard
Jackson data binding.

%package -n jackson-jaxrs-xml-provider
Summary:        Jackson-JAXRS-XML

%description -n jackson-jaxrs-xml-provider
Functionality to handle Smile XML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n jackson-jaxrs-yaml-provider
Summary:        Jackson-JAXRS-YAML

%description -n jackson-jaxrs-yaml-provider
Functionality to handle YAML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.
%endif

%package datatypes
Summary:        Functionality for reading/writing core JAX-RS helper types

%description datatypes
Functionality for reading/writing core JAX-RS helper types.

%package parent
Summary:        Parent for Jackson JAX-RS providers

%description parent
Parent POM for Jackson JAX-RS providers.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p xml/src/main/resources/META-INF/LICENSE .
cp -p xml/src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%pom_remove_plugin -r :moditect-maven-plugin
%pom_remove_plugin -r :gradle-module-metadata-maven-plugin

# Disable jar with no-meta-inf-services classifier, breaks build
%pom_remove_plugin :maven-jar-plugin cbor
%pom_remove_plugin :maven-jar-plugin json
%pom_remove_plugin :maven-jar-plugin smile
%pom_remove_plugin :maven-jar-plugin xml
%pom_remove_plugin :maven-jar-plugin yaml
%pom_remove_plugin :maven-jar-plugin datatypes

# Circular dep?
%pom_remove_dep org.jboss.resteasy:resteasy-jackson2-provider json
rm json/src/test/java/com/fasterxml/jackson/jaxrs/json/resteasy/RestEasyProviderLoadingTest.java

# Disable extra test deps
%pom_remove_dep org.glassfish.jersey.core:
%pom_remove_dep org.glassfish.jersey.containers:

%build
%{mvn_build} -s -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-jackson-jaxrs-base
%doc README.md release-notes/*
%license LICENSE NOTICE

%files -n jackson-jaxrs-json-provider -f .mfiles-jackson-jaxrs-json-provider

%files -n jackson-jaxrs-cbor-provider -f .mfiles-jackson-jaxrs-cbor-provider

%files -n jackson-jaxrs-smile-provider -f .mfiles-jackson-jaxrs-smile-provider

%files -n jackson-jaxrs-xml-provider -f .mfiles-jackson-jaxrs-xml-provider

%files -n jackson-jaxrs-yaml-provider -f .mfiles-jackson-jaxrs-yaml-provider

%files datatypes -f .mfiles-jackson-datatype-jaxrs
%license LICENSE NOTICE

%files parent -f .mfiles-jackson-jaxrs-providers
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
