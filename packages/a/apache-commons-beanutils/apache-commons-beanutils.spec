#
# spec file for package apache-commons-beanutils
#
# Copyright (c) 2025 SUSE LLC
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


%{?!mvn_install_pom:%global mvn_install_pom install -pm 0644}
%define base_name	beanutils
%define short_name	commons-%{base_name}
Name:           apache-commons-beanutils
Version:        1.11.0
Release:        0
Summary:        Utility methods for accessing and modifying the properties of JavaBeans
License:        Apache-2.0
URL:            https://commons.apache.org/beanutils
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz.asc
Patch0:         jdk9.patch
Patch1:         apache-commons-beanutils-fix-build-version.patch
BuildRequires:  ant
BuildRequires:  commons-collections
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
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

%description javadoc
The scope of the Jakarta Commons BeanUtils Package is to create a
package of Java utility methods for accessing and modifying the
properties of arbitrary JavaBeans.  No dependencies outside of the JDK
are required, so the use of this package is very lightweight.

This package contains the javadoc documentation for the Jakarta Commons
BeanUtils Package.

%prep
%autosetup -p1 -n %{short_name}-%{version}-src

# The previous empty line needs to be maintained for sle12 compatibility
sed -i 's/\r//' *.txt
# bug in ant build
touch README.txt

%build
export CLASSPATH=%(build-classpath commons-collections commons-logging)
ant -Dbuild.sysclasspath=first -Dcomponent.version=%{version} dist

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "%{short_name}:%{short_name}-core,%{short_name}:%{short_name}-bean-collections"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/%{name}.jar
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
