#
# spec file for package apache
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


%global base_name       el
%global short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.0
Release:        0
Summary:        The Apache Commons Extension Language
License:        Apache-1.1
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        http://repo1.maven.org/maven2/%{short_name}/%{short_name}/%{version}/%{short_name}-%{version}.pom
Patch0:         %{short_name}-%{version}-license.patch
Patch1:         %{short_name}-eclipse-manifest.patch
Patch2:         %{short_name}-enum.patch
BuildRequires:  ant
BuildRequires:  apache-commons-logging
BuildRequires:  fdupes
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  javapackages-local
BuildRequires:  junit
Requires:       mvn(commons-logging:commons-logging)
BuildArch:      noarch

%description
An implementation of standard interfaces and abstract classes for
javax.servlet.jsp.el which is part of the JSP 2.0 specification.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Libraries/Java

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1 -b .license
%patch1 -p1
%patch2 -p1

# remove all precompiled stuff
find . -type f -name "*.jar" -exec rm -f {} \;

cat > build.properties <<EOBP
build.compiler=modern
junit.jar=$(build-classpath junit)
servlet-api.jar=$(build-classpath glassfish-servlet-api)
jsp-api.jar=$(build-classpath glassfish-jsp-api)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 dist/%{short_name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "org.apache.commons:commons-el"
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc STATUS.html
%{_javadir}/%{name}.jar

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
