#
# spec file for package apache-commons-beanutils
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


%define base_name	beanutils
%define short_name	commons-%{base_name}
Name:           apache-commons-beanutils
Version:        1.9.4
Release:        0
Summary:        Utility methods for accessing and modifying the properties of JavaBeans
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/beanutils
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz.asc
Patch0:         jdk9.patch
Patch1:         apache-commons-beanutils-fix-build-version.patch
BuildRequires:  ant
BuildRequires:  commons-collections
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  xml-commons-apis
Requires:       commons-collections >= 2.0
Requires:       commons-logging >= 1.0
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
The scope of this package is to create a package of Java utility
methods for accessing and modifying the properties of arbitrary
JavaBeans.  No dependencies outside of the JDK are required, so the use
of this package is very lightweight.

%package javadoc
Summary:        Javadoc for jakarta-commons-beanutils
Group:          Development/Libraries/Java

%description javadoc
The scope of the Jakarta Commons BeanUtils Package is to create a
package of Java utility methods for accessing and modifying the
properties of arbitrary JavaBeans.  No dependencies outside of the JDK
are required, so the use of this package is very lightweight.

This package contains the javadoc documentation for the Jakarta Commons
BeanUtils Package.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' *.txt
# bug in ant build
touch README.txt

%build
export CLASSPATH=%(build-classpath commons-collections commons-logging)
ant -Dbuild.sysclasspath=first dist

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar

pushd %{buildroot}%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
for jar in *.jar; do
    ln -sf ${jar} `echo $jar| sed "s|apache-||g"`
done
popd # come back from javadir

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar -a "org.apache.commons:%{short_name}"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%license LICENSE.txt
%doc NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
