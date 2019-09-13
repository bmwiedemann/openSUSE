#
# spec file for package xmlunit
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2008, JPackage Project
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


Name:           xmlunit
Version:        1.5
Release:        0
Summary:        Provides classes to do asserts on XML
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://xmlunit.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}-src.zip
Source1:        http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
# Needed for maven conversions
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis >= 1.3
Requires:       junit
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xml-commons-apis >= 1.3
BuildArch:      noarch

%description
XMLUnit extends JUnit to simplify unit testing of XML. It compares a control
XML document to a test document or the result of a transformation, validates
documents against a DTD, and (from v0.5) compares the results of XPath
expressions.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}. Also contains userguide.

%prep
%setup -q

perl -pi -e 's/\r$//g' README.txt LICENSE.txt

# remove all binary libs and javadocs
find . -name "*.jar" -delete

%build

cat > build.properties << EOF
junit.lib=$(build-classpath junit)
xmlxsl.lib=$(build-classpath xalan-j2 xerces-j2 xml-commons-jaxp-1.3-apis)
test.report.dir=test
EOF

cat > docbook.properties <<EOF
db5.xsl=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/
EOF

export CLASSPATH=
export OPT_JAR_LIST="junit ant/ant-junit jaxp_transform_impl ant/ant-trax xalan-j2-serializer"
ant -Djavac.source=1.6 -Djavac.target=1.6 -Dbuild.compiler=modern -Dhaltonfailure=yes jar javadocs

%install
mkdir -p %{buildroot}%{_javadir}
install -m 0644 build/lib/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir}/ && ln -s %{name}-%{version}.jar %{name}.jar)

# Javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE1} \
    %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar

%files
%license LICENSE.txt
%doc README.txt
%{_javadir}/*.jar
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files javadoc
%doc userguide
%{_javadocdir}/%{name}

%changelog
