#
# spec file for package jackson-modules-base
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


Name:           jackson-modules-base
Version:        2.17.1
Release:        0
Summary:        Jackson modules: Base
License:        Apache-2.0
URL:            https://github.com/FasterXML/jackson-modules-base
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= 2.17
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(com.thoughtworks.paranamer:paranamer)
BuildRequires:  mvn(javax.activation:javax.activation-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildArch:      noarch

%description
Jackson "base" modules: modules that build directly on databind,
and are not data-type, data format, or JAX-RS provider modules.

%package -n jackson-module-afterburner
Summary:        Jackson module that uses byte-code generation to further speed up data binding

%description -n jackson-module-afterburner
Module that will add dynamic bytecode generation for standard Jackson POJO
serializers and deserializers, eliminating majority of remaining data binding
overhead.

%package -n jackson-module-blackbird
Summary:        Jackson module that uses LambdaMetafactory based code generation to replace reflection calls.

%description -n jackson-module-blackbird
The LambdaMetafactory introduces a standard Java API for dynamically instantiating function objects.
The current OpenJDK implementation generates anonymous classes in a somewhat similar fashion to the
classic Afterburner. While the metafactory cannot generate comparably specialized implementations,
we can write needed adapters as simple Java code and use the metafactory to create distinct call
sites for every needed access path. This should allow each accessor to have a monomorphic call
profile and easily inline for maximum performance.

%package -n jackson-module-guice
Summary:        Jackson module to make integration with Guice a bit easier

%description -n jackson-module-guice
This extension allows Jackson to delegate ObjectMapper creation and value
injection to Guice when handling data bindings.

%package -n jackson-module-jaxb-annotations
Summary:        Support for using JAXB annotations as an alternative to "native" Jackson annotations

%description -n jackson-module-jaxb-annotations
This Jackson extension module provides support for using JAXB (javax.xml.bind)
annotations as an alternative to native Jackson annotations. It is most often
used to make it easier to reuse existing data beans that used with JAXB
framework to read and write XML.

%package -n jackson-module-mrbean
Summary:        Functionality for implementing interfaces and abstract types dynamically

%description -n jackson-module-mrbean
Mr Bean is an extension that implements support for "POJO type materialization"
ability for databinder to construct implementation classes for Java interfaces
and abstract classes, as part of deserialization.

%package -n jackson-module-no-ctor-deser
Summary:        Support deserialization of POJO classes without default constructor

%description -n jackson-module-no-ctor-deser
Module that allows instantiation of Java POJOs that do not have "default constructor"
(constructor that takes no arguments) but should be deserialized from JSON Object
as POJOs. In such cases, module tries to use sun.reflect.ReflectionFactory
to force instantiation that by-passes all constructors (it is the mechanism used by
JDK serialization system).

%package -n jackson-module-osgi
Summary:        Jackson module to inject OSGI services in deserialized beans

%description -n jackson-module-osgi
This module provides a way to inject OSGI services into deserialized objects.
Thanks to the JacksonInject annotations, the OsgiJacksonModule will search for
the required service in the OSGI service registry and injects it in the object
while deserializing.

%package -n jackson-module-paranamer
Summary:        Jackson module that uses Paranamer to introspect names of constructor params

%description -n jackson-module-paranamer
Module that uses Paranamer library to auto-detect names of Creator
(constructor, static factory method, annotated with @JsonCreator) methods.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_disable_module jakarta-xmlbind

# no need for Java 9 module stuff
%pom_remove_plugin -r :moditect-maven-plugin

# no need for gradle metadata
%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :find-and-replace-maven-plugin

# move to "old" glassfish-jaxb-api artifactId
%pom_change_dep -r jakarta.xml.bind:jakarta.xml.bind-api javax.xml.bind:jaxb-api
%pom_change_dep -r jakarta.activation:jakarta.activation-api javax.activation:javax.activation-api

# Disable bundling of asm
%pom_remove_plugin ":maven-shade-plugin" afterburner mrbean paranamer

sed -i 's/\r//' mrbean/src/main/resources/META-INF/{LICENSE,NOTICE}
cp -p mrbean/src/main/resources/META-INF/{LICENSE,NOTICE} .

# Fix OSGi dependency
%pom_change_dep org.osgi:org.osgi.core org.osgi:osgi.core osgi

# Allow javax,activation to be optional
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" jaxb "
<configuration>
  <instructions>
    <Import-Package>javax.activation;resolution:=optional,*</Import-Package>
  </instructions>
</configuration>"

%pom_disable_module guice7
%pom_disable_module android-record

%{mvn_file} ":{*}" jackson-modules/@1

%build
%{mvn_build} -s -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install

%files -f .mfiles-jackson-modules-base
%doc README.md release-notes
%license LICENSE NOTICE

%files -n jackson-module-afterburner -f .mfiles-jackson-module-afterburner
%doc afterburner/README.md afterburner/release-notes
%license LICENSE NOTICE

%files -n jackson-module-blackbird -f .mfiles-jackson-module-blackbird
%doc blackbird/README.md
%license LICENSE NOTICE

%files -n jackson-module-guice -f .mfiles-jackson-module-guice
%doc guice/README.md
%license LICENSE NOTICE

%files -n jackson-module-jaxb-annotations -f .mfiles-jackson-module-jaxb-annotations
%doc jaxb/README.md jaxb/release-notes
%license LICENSE NOTICE

%if %{without jp_minimal}
%files -n jackson-module-mrbean -f .mfiles-jackson-module-mrbean
%doc mrbean/README.md mrbean/release-notes
%license LICENSE NOTICE
%endif

%files -n jackson-module-no-ctor-deser -f .mfiles-jackson-module-no-ctor-deser
%doc no-ctor-deser/README.md
%license LICENSE NOTICE

%files -n jackson-module-osgi -f .mfiles-jackson-module-osgi
%doc osgi/README.md osgi/release-notes
%license LICENSE NOTICE

%if %{without jp_minimal}
%files -n jackson-module-paranamer -f .mfiles-jackson-module-paranamer
%doc paranamer/README.md paranamer/release-notes
%license LICENSE NOTICE
%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
