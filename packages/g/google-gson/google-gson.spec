#
# spec file for package google-gson
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           google-gson
Version:        2.8.5
Release:        0
Summary:        Java lib for conversion of Java objects into JSON representation
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/gson
Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz
Patch0:         osgi-export-internal.patch
Patch1:         no-template-plugin.patch
# Java 11 changed the DateTime.FULL output for Locale.FRANCE
Patch2:         fix-test.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n gson-gson-parent-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -f \
  gson/src/main/java-templates/com/google/gson/internal/GsonBuildConfig.java \
  gson/src/test/java/com/google/gson/functional/GsonVersionDiagnosticsTest.java \
  gson/src/test/java/com/google/gson/internal/GsonBuildConfigTest.java

# Use felix maven-bundle-plugin only for OSGi metadata
%pom_remove_plugin :bnd-maven-plugin gson
%pom_remove_plugin org.codehaus.mojo:templating-maven-plugin gson
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']" "<configuration>
    <instructions>
      <_include>bnd.bnd</_include>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>" gson


%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
