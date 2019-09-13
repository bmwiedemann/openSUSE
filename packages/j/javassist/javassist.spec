#
# spec file for package javassist
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2005, JPackage Project
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


%define tar_version rel_3_23_1_ga
Name:           javassist
Version:        3.23.1
Release:        0
Summary:        Java Programming Assistant: bytecode manipulation
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          Development/Libraries/Java
URL:            https://www.javassist.org/
Source0:        https://github.com/jboss-javassist/javassist/archive/%{tar_version}.tar.gz
Patch0:         javassist-java8-compat.patch
BuildRequires:  ant >= 1.6
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Javassist (Java Programming Assistant) makes Java bytecode manipulation
simple. It is a class library for editing bytecodes in Java; it enables
Java programs to define a new class at runtime and to modify a class
file when the JVM loads it. Unlike other similar bytecode editors,
Javassist provides two levels of API: source level and bytecode level.
If the users use the source-level API, they can edit a class file
without knowledge of the specifications of the Java bytecode. The whole
API is designed with only the vocabulary of the Java language. You can
even specify inserted bytecode in the form of source text; Javassist
compiles it on the fly. On the other hand, the bytecode-level API
allows the users to directly edit a class file as other editors.

%package demo
Summary:        Samples for javassist
Group:          Documentation/Other
Requires:       javassist = %{version}-%{release}

%description demo
Samples for javassist.

%{summary}.

%package javadoc
Summary:        Javadoc for javassist
Group:          Documentation/HTML

%description javadoc
Javadoc for javassist.

%{summary}.

%package manual
Summary:        Tutorial for javassist
Group:          Documentation/Other

%description manual
Tutorial for javassist.

%{summary}.

%prep
%setup -q -n %{name}-%{tar_version}
%if %{?pkg_vcmp:%pkg_vcmp java-devel < 9}%{!?pkg_vcmp:1}
%patch0 -p1
%endif
for j in $(find . -name "*.jar"); do
        mv $j $j.no
done

%build
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 dist

%install
# jars
mkdir -p %{buildroot}/%{_javadir}
cp -p %{name}.jar \
  %{buildroot}/%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}/%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a javassist:javassist

# demo
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}
cp -pr sample/* %{buildroot}/%{_datadir}/%{name}-%{version}

# javadoc
mkdir -p %{buildroot}/%{_javadocdir}/%{name}
cp -pr html/* %{buildroot}/%{_javadocdir}/%{name}

%fdupes -s %{buildroot}/%{_javadocdir}/%{name}/jquery/

# manual
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}/tutorial
cp -pr tutorial/* %{buildroot}/%{_docdir}/%{name}-%{version}/tutorial
cp -p License.html %{buildroot}/%{_docdir}/%{name}-%{version}

%files
%defattr(0644,root,root,0755)
%dir %{_docdir}/%{name}-%{version}
%license %{_docdir}/%{name}-%{version}/License.html
%{_javadir}/*.jar
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}-%{version}

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/tutorial

%changelog
