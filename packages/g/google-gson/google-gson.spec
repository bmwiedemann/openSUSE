#
# spec file for package google-gson
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


Name:           google-gson
Version:        2.8.9
Release:        0
Summary:        Java lib for conversion of Java objects into JSON representation
License:        Apache-2.0
URL:            https://github.com/google/gson
Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz
Patch0:         osgi-export-internal.patch
# Remove dependency on unavailable templating-maven-plugin
Patch1:         no-template-plugin.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(javax.annotation:jsr250-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
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

# remove unnecessary dependency on parent POM
%pom_remove_parent

# presence of these files breaks builds with Java 8
# find -name "module-info.java" -print -delete

# Use felix maven-bundle-plugin only for OSGi metadata
%pom_remove_plugin :bnd-maven-plugin gson
%pom_remove_plugin :templating-maven-plugin gson
%pom_remove_plugin :copy-rename-maven-plugin gson
%pom_remove_plugin :proguard-maven-plugin gson
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" gson "<configuration>
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
  </executions>"

%pom_xpath_set "pom:plugins/pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration" "<release>8</release>"

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
