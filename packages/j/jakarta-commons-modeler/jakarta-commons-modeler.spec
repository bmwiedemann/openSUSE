#
# spec file for package jakarta-commons-modeler
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define base_name	modeler
%define short_name	commons-%{base_name}
Name:           jakarta-commons-modeler
Version:        2.0
Release:        0
Summary:        Jakarta Commons Modeler Package
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/commons/modeler/
Source0:        %{short_name}-%{version}-src.tar.bz2
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jakarta-commons-digester
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  mx4j
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-apis
Requires:       jakarta-commons-beanutils >= 1.3
Requires:       jakarta-commons-collections >= 2.0
Requires:       jakarta-commons-digester >= 1.2
Requires:       jakarta-commons-logging >= 1.0
Requires:       jaxp_parser_impl
Requires:       jaxp_transform_impl
Requires:       mx4j
Requires:       xml-commons-apis
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
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
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
ant \
    -Dant.jar=$(build-classpath ant) \
    -Djaxp.parser.jar=$(build-classpath jaxp_parser_impl) \
    -Djaxp.xalan.jar=$(build-classpath jaxp_trasform_impl) \
    -Djmx.jar=$(build-classpath mx4j/mx4j-jmx) \
    -Djunit.jar=$(build-classpath junit) \
    -Dcommons-digester.jar=$(build-classpath commons-digester) \
    -Dcommons-logging.jar=$(build-classpath commons-logging) \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    dist

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -a dist/%{short_name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a dist/docs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt xdocs
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
