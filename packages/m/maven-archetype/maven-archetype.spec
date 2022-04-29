#
# spec file for package maven-archetype
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


Name:           maven-archetype
Version:        3.2.1
Release:        0
Summary:        Maven project templating toolkit
License:        Apache-2.0
URL:            https://maven.apache.org/archetype/
Source0:        https://dlcdn.apache.org/maven/archetype/%{name}-%{version}-source-release.zip
Patch1:         0001-Avoid-reliance-on-groovy.patch
Patch2:         port-to-maven-script-interpreter-1_3.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  mvn(org.apache.maven.shared:maven-script-interpreter)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.jdom:jdom2)
BuildArch:      noarch

%description
Archetype is a Maven project templating toolkit. An archetype is
defined as an original pattern or model from which all other things of
the same kind are made. The names fits as we are trying to provide a
system that provides a consistent means of generating Maven
projects. Archetype will help authors create Maven project templates
for users, and provides users with the means to generate parameterized
versions of those project templates.

Using archetypes provides a great way to enable developers quickly in
a way consistent with best practices employed by your project or
organization. Within the Maven project we use archetypes to try and
get our users up and running as quickly as possible by providing a
sample project that demonstrates many of the features of Maven while
introducing new users to the best practices employed by Maven. In a
matter of seconds a new user can have a working Maven project to use
as a jumping board for investigating more of the features in Maven. We
have also tried to make the Archetype mechanism additive and by that
we mean allowing portions of a project to be captured in an archetype
so that pieces or aspects of a project can be added to existing
projects. A good example of this is the Maven site archetype. If, for
example, you have used the quick start archetype to generate a working
project you can then quickly create a site for that project by using
the site archetype within that existing project. You can do anything
like this with archetypes.

You may want to standardize J2EE development within your organization
so you may want to provide archetypes for EJBs, or WARs, or for your
web services. Once these archetypes are created and deployed in your
organization's repository they are available for use by all developers
within your organization.

%package javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.

%package catalog
Summary:        Maven Archetype Catalog model

%description catalog
%{summary}.

%package descriptor
Summary:        Maven Archetype Descriptor model

%description descriptor
%{summary}.

%package common
Summary:        Maven Archetype common classes

%description common
%{summary}.

%package packaging
Summary:        Maven Archetype packaging configuration for archetypes

%description packaging
%{summary}.

%package plugin
Summary:        Maven Plugin for using archetypes

%description plugin
%{summary}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%pom_change_dep ant:ant-antlr org.apache.ant:ant-antlr archetype-common
%pom_change_dep org.sonatype.aether: org.eclipse.aether: archetype-common

# Pointless for rpm build
%pom_remove_plugin -r org.apache.rat:apache-rat-plugin
%pom_remove_plugin -r org.apache.maven.plugins:maven-enforcer-plugin

# Add OSGI info to catalog and descriptor jars
pushd archetype-models/archetype-catalog
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.catalog.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd
pushd archetype-models/archetype-descriptor
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.metadata.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd

# Remove ivy as a runtime dep
%pom_remove_dep org.apache.ivy:ivy archetype-common

# Disable processing of test resources using ant
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin archetype-common

%build
%{mvn_package} :archetype-models maven-archetype
%{mvn_build} -s -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-maven-archetype
%license LICENSE
%doc NOTICE

%files catalog -f .mfiles-archetype-catalog

%files descriptor -f .mfiles-archetype-descriptor

%files common -f .mfiles-archetype-common

%files packaging -f .mfiles-archetype-packaging

%files plugin -f .mfiles-maven-archetype-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
