#
# spec file for package jakarta-commons-modeler
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


%define base_name	modeler
%define short_name	commons-%{base_name}
Name:           jakarta-commons-modeler
Version:        2.0.1
Release:        0
Summary:        Jakarta Commons Modeler Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/dormant/commons-modeler/
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz.asc
Source10:       https://repo1.maven.org/maven2/%{short_name}/%{short_name}/%{version}/%{short_name}-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jakarta-commons-digester
BuildRequires:  jakarta-commons-logging
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
BuildRequires:  mx4j
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       apache-%{short_name} = %{version}-%{release}
BuildArch:      noarch

%description
The Modeler project creates and maintains a set of Java classes to
provide a number of facilities for Model MBeans plus unit tests and
small examples of using these facilities to instrument Java classes
with Model MBean support.

%package javadoc
Summary:        Javadoc for jakarta-commons-modeler
Group:          Development/Libraries/Java

%description javadoc
The Modeler project shall create and maintain a set of Java classes to
provide the facilities described in the preceeding section, plus unit
tests and small examples of using these facilities to instrument Java
classes with Model MBean support.

This package contains the javadoc documentation for the Jakarta Commons
Modeler Package.

%prep
%setup -q -n %{short_name}-%{version}-src

# convert DOS lineenedings to unix
sed -i 's/\r$//' NOTICE.txt
sed -i 's/\r$//' RELEASE-NOTES.txt
sed -i 's/\r$//' xdocs/*.xml
sed -i 's/\r$//' xdocs/style/*.css

%build
%{ant} \
    -Dant.jar=$(build-classpath ant) \
    -Djaxp.parser.jar=$(build-classpath xerces-j2) \
    -Djaxp.xalan.jar=$(build-classpath xalan-j2) \
    -Djmx.jar=$(build-classpath mx4j/mx4j-jmx) \
    -Djunit.jar=$(build-classpath junit) \
    -Dcommons-digester.jar=$(build-classpath commons-digester) \
    -Dcommons-logging.jar=$(build-classpath commons-logging) \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    dist

%install

# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 dist/%{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE10} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -a dist/docs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc NOTICE.txt RELEASE-NOTES.txt xdocs
%license LICENSE.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
