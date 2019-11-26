#
# spec file for package tiger-types
#
# Copyright (c) 2019 SUSE LLC
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


Name:           tiger-types
Version:        2.2
Release:        0
Summary:        Type arithmetic library for Java5
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/kohsuke/tiger-types
Source0:        https://github.com/kohsuke/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/javaee/glassfish/5.0.1/LICENSE
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
This library provides functions that perform type arithemtic over the
type system of Java5. For example, one can compute that List<String>
is a sub-type of Collection<String> but not Collection<Object>, you
can compute the erasure of java.lang.reflect.Type, or you can
determine the array component type T from A[T].

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
# add OSGi support required by glassfish hk2
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<configuration>
  <instructions>
      <Embed-Dependency>*;scope=provided;inline=true</Embed-Dependency>
      <Export-Package>org.jvnet.tiger_types.*</Export-Package>
  </instructions>
  <unpackBundle>true</unpackBundle>
</configuration>
<executions>
  <execution>
      <id>osgi-bundle</id>
      <phase>package</phase>
      <goals>
          <goal>bundle</goal>
      </goals>
  </execution>
</executions>'

# not needed
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin
%pom_xpath_remove "pom:build/pom:extensions"

%{mvn_file} :%{name} %{name}

cp -p %{SOURCE1} LICENSE

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
