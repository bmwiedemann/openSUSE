#
# spec file for package c3p0
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


%define mchange_commons_version 0.2.11
Name:           c3p0
Version:        0.9.5.2
Release:        0
Summary:        JDBC DataSources/Resource Pools
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            http://sourceforge.net/projects/c3p0/
Source0:        http://downloads.sourceforge.net/sourceforge/c3p0/c3p0-0.9.5.2.src.tgz
Patch1:         %{name}-javadoc.patch
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  mchange-commons = %{mchange_commons_version}
Requires:       mchange-commons = %{mchange_commons_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       hibernate_jdbc_cache
BuildArch:      noarch

%description
c3p0 is a library for augmenting traditional (DriverManager-based)
JDBC drivers with JNDI-bindable DataSources, including DataSources
that implement Connection and Statement Pooling, as described by the
jdbc3 spec and jdbc2 standard extension.

%package javadoc
Summary:        Javadoc for c3p0
Group:          Documentation/HTML

%description javadoc
Javadoc documentation for c3p0.

%prep
%setup -q -n %{name}-%{version}.src
%patch1 -p1

%build
export CLASSPATH=
export OPT_JAR_LIST="ant/ant-nodeps"
ant \
    -Dmchange-commons-java.jar.file=%{_javadir}/mchange-commons/mchange-commons-java.jar \
	-Djunit.jar.file=$(build-classpath junit) -Djvm.target.version=8 \
    jar javadoc

sed -i "s/@c3p0.version.maven@/%{version}/g" src/maven/pom.xml
sed -i "s/@mchange-commons-java.version.maven@/%{mchange_commons_version}/g" \
  src/maven/pom.xml

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
mkdir -p %{buildroot}%{_mavenpomdir}
cp -p src/maven/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar -a c3p0:c3p0

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}

# hibernate_jdbc_cache ghost symlink
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/hibernate_jdbc_cache.jar \
  %{buildroot}%{_javadir}/hibernate_jdbc_cache.jar

%post
update-alternatives --install %{_javadir}/hibernate_jdbc_cache.jar \
  hibernate_jdbc_cache %{_javadir}/%{name}.jar 20

%preun
if [ "$1" = 0 ] ; then
  update-alternatives --remove hibernate_jdbc_cache %{_javadir}/%{name}.jar
fi

%files
%license src/dist-static/LICENSE
%doc src/doc/index.html
%{_javadir}/*
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml
%endif
%ghost %{_sysconfdir}/alternatives/hibernate_jdbc_cache.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
