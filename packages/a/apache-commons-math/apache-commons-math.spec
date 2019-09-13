#
# spec file for package apache-commons-math
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global base_name       math
%global short_name      commons-%{base_name}
Name:           apache-commons-math
Version:        3.6.1
Release:        0
Summary:        The Apache Commons Mathematics Library
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}3-%{version}-src.tar.gz
Patch0:         commons-math3-3.6.1-notests.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
Requires:       java >= 1.8
Provides:       java(commons-math3:commons-math3) = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in
the Java programming language or Commons Lang.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}3-%{version}-src
%patch0 -p1

%build
export CLASSPATH=$(build-classpath ant-junit junit)
ant -Dant.build.javac.source=8 -Dcompile.source=8 \
    -Dant.build.javac.target=8 -Dcompile.target=8 \
    -Dmaven.mode.offline=true -Dmaven.test.skip=true \
    -lib %{_datadir}/java -Dbuild.sysclasspath=first \
	jar javadoc 

%install
# jars
install -Dpm 644 target/%{short_name}*.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/apidocs/ %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(-,root,root)
%doc LICENSE.txt license-header.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml

%files javadoc
%defattr(-,root,root)
%doc LICENSE.txt
%{_javadocdir}/*

%changelog
