#
# spec file for package plexus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global short_name classworlds
%bcond_with tests
Name:           plexus-%{short_name}
Version:        2.5.2
Release:        0
Summary:        Plexus Classworlds Classloader Framework
License:        Apache-2.0 AND Plexus
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-classworlds
Source0:        https://github.com/sonatype/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       %{short_name} = %{version}-%{release}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
BuildRequires:  commons-logging
BuildRequires:  xml-apis
%endif

%description
Classworlds is a framework for container developers
who require complex manipulation of Java's ClassLoaders.
Java's native ClassLoader mechanisms and classes can cause
much headache and confusion for certain types of
application developers. Projects which involve dynamic
loading of components or otherwise represent a 'container'
can benefit from the classloading control provided by
classworlds.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} build.xml
%if %{with tests}
mkdir -p target/test-lib
rm -f target/test-lib/{ant-1.9.0,commons-logging-1.0.3,xml-apis-1.3.02}.jar
ln -s $(build-classpath ant/ant) target/test-lib/ant-1.9.0.jar
ln -s $(build-classpath commons-logging) target/test-lib/commons-logging-1.0.3.jar
ln -s $(build-classpath xml-apis) target/test-lib/xml-apis-1.3.02.jar
%endif

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-dependency-plugin

%pom_remove_parent .
%pom_xpath_inject "pom:project" "<groupId>org.codehaus.plexus</groupId>" .

%build
%{ant} \
%if %{without tests}
    -Dtest.skip=true \
%endif
    jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/plexus/%{short_name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a %{short_name}:%{short_name}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt LICENSE-2.0.txt
%{_javadir}/plexus
%{_javadir}/%{short_name}.jar

%files javadoc
%license LICENSE.txt LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
