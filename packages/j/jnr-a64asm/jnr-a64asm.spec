#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global cluster jnr
Name:           %{cluster}-a64asm
Version:        1.0.0
Release:        0
Summary:        AArch64 assembler for the Java Native Runtime
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://github.com/%{cluster}/%{name}/
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
This is a pure-java port of asmjit for AARCH64 architecture
(http://code.google.com/p/asmjit/). This is remote assembler for jnr-ffi to
support aarch64 architecture.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" . "
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
          </instructions>
        </configuration>
        <executions>
          <execution>
            <id>bundle-manifest</id>
            <phase>process-classes</phase>
            <goals>
              <goal>manifest</goal>
            </goals>
          </execution>
        </executions>"

%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" . "
        <configuration>
          <archive>
            <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
            <manifestEntries>
              <Automatic-Module-Name>org.jnrproject.a64asm</Automatic-Module-Name>
            </manifestEntries>
          </archive>
        </configuration>"

%{mvn_file} : %{cluster}/%{name}

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
