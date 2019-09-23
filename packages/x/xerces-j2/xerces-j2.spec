#
# spec file for package xerces-j2
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


%global cvs_version 2_12_0
%define __requires_exclude system.bundle
Name:           xerces-j2
Version:        2.12.0
Release:        0
Summary:        Java XML parser
License:        Apache-2.0 AND W3C
Group:          Development/Libraries/Java
URL:            http://xerces.apache.org/xerces2-j/
Source0:        http://www.eu.apache.org/dist/xerces/j/source/Xerces-J-src.%{version}.tar.gz
Source1:        %{name}-version.sh
Source2:        %{name}-constants.sh
Source3:        %{name}-version.1
Source4:        %{name}-constants.1
Source5:        http://repo.maven.apache.org/maven2/xerces/xercesImpl/%{version}/xercesImpl-%{version}.pom
# Patch the build so that it doesn't try to use bundled xml-commons source
# Also remove the use of the special taglets and xjavac task
Patch0:         %{name}-build.patch
Patch1:         xerces-2_11_0-jdk7.patch
Patch2:         %{name}-manifest.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  xalan-j2 >= 2.7.1
BuildRequires:  xml-commons-apis >= 1.4.01
BuildRequires:  xml-commons-resolver >= 1.2
#!BuildIgnore:  xerces-j2 osgi(org.apache.xerces) jaxp_parser_impl
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Requires:       xalan-j2 >= 2.7.1
Requires:       xml-commons-apis >= 1.4.01
Requires:       xml-commons-resolver >= 1.2
Provides:       %{name}-scripts = %{version}-%{release}
Provides:       jaxp_parser_impl = 1.4
Obsoletes:      %{name}-scripts < %{version}-%{release}
BuildArch:      noarch

%description
Xerces2 is an XML parser in the Apache Xerces family. This version is the
reference implementation of the Xerces Native Interface (XNI), a modular
framework for building parser components and configurations.

Xerces2 implements the Document Object Model Level 3 Core and Load/Save W3C
Recommendations, the XML Inclusions (XInclude) W3C Recommendation, and supports
OASIS XML Catalogs v1.1. It can parse documents conforming to the XML 1.1
Recommendation, except that it does not yet provide an option to enable
normalization checking as described in section 2.13 of this specification. It
handles name spaces according to the XML Namespaces 1.1 Recommendation, and
serializes XML 1.1 documents if the DOM level 3 load/save APIs are in use.

%package        javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description    javadoc
This package contains the API documentation for %{name}.

%package        demo
Summary:        Demonstrations and samples for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description    demo
%{summary}.

%prep
%setup -q -n xerces-%{cvs_version}
find "(" -name "*.class" -o -name "*.jar" ")" -delete
find -type f -exec dos2unix {} \;
%patch0 -p1
%patch1 -p1
%patch2

%build
mkdir -p tools
pushd tools
ln -sf $(build-classpath xalan-j2-serializer) serializer.jar
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
ln -sf $(build-classpath xml-commons-resolver) resolver.jar
popd

# Build everything
export ANT_OPTS="-Xmx256m -Djava.awt.headless=true -Dbuild.sysclasspath=first -Ddisconnected=true"
ant -Djavac.source=1.6 -Djavac.target=1.6 \
    -Dbuild.compiler=modern \
    clean jars javadocs

%install
# jar
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 build/xercesImpl.jar %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir} && ln -s %{name}.jar jaxp_parser_impl.jar)

# pom
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a xerces:xerces,xerces:xmlParserAPIs,apache:xerces-j2

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_javadocdir}/%{name}/impl
mkdir -p %{buildroot}%{_javadocdir}/%{name}/xs
mkdir -p %{buildroot}%{_javadocdir}/%{name}/xni
mkdir -p %{buildroot}%{_javadocdir}/%{name}/other

cp -pr build/docs/javadocs/xerces2/* %{buildroot}%{_javadocdir}/%{name}/impl
cp -pr build/docs/javadocs/api/* %{buildroot}%{_javadocdir}/%{name}/xs
cp -pr build/docs/javadocs/xni/* %{buildroot}%{_javadocdir}/%{name}/xni
cp -pr build/docs/javadocs/other/* %{buildroot}%{_javadocdir}/%{name}/other

%fdupes -s %{buildroot}%{_javadocdir}

# scripts
install -pD -m755 -T %{SOURCE1} %{buildroot}%{_bindir}/%{name}-version
install -pD -m755 -T %{SOURCE2} %{buildroot}%{_bindir}/%{name}-constants

# manual pages
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE4} %{buildroot}%{_mandir}/man1

# demo
install -pD -T build/xercesSamples.jar %{buildroot}%{_datadir}/%{name}/%{name}-samples.jar
cp -pr data %{buildroot}%{_datadir}/%{name}

%post
update-alternatives --remove jaxp_parser_impl %{_javadir}/%{name}.jar >/dev/null 2>&1 || :
# it deletes the link, set it up again
ln -sf %{name}.jar %{_javadir}/jaxp_parser_impl.jar

%files
%license LICENSE
%doc NOTICE README
%{_bindir}/*
%{_javadir}/*
%{_mandir}/*/*
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
