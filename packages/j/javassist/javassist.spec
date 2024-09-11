#
# spec file for package javassist
#
# Copyright (c) 2024 SUSE LLC
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


%define tar_version rel_3_30_2_ga
Name:           javassist
Version:        3.30.2
Release:        0
Summary:        Java Programming Assistant: bytecode manipulation
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          Development/Libraries/Java
URL:            https://www.javassist.org/
Source0:        https://github.com/jboss-javassist/javassist/archive/%{tar_version}.tar.gz
Patch0:         javassist-java8-compat.patch
Patch1:         javassist-osgi.patch
BuildRequires:  ant >= 1.6
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
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
%if %{!?pkg_vcmp:1}%{?pkg_vcmp:%pkg_vcmp java-devel < 9}
%patch -P 0 -p1
%endif
%patch -P 1 -p1
find . -name "*.jar" -print -delete

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 dist

%install
# jars
mkdir -p %{buildroot}/%{_javadir}
cp -p %{name}.jar %{buildroot}/%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a javassist:javassist

# demo
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}
cp -pr sample/* %{buildroot}/%{_datadir}/%{name}-%{version}

# javadoc
mkdir -p %{buildroot}/%{_javadocdir}/%{name}
cp -pr html/* %{buildroot}/%{_javadocdir}/%{name}

%fdupes -s %{buildroot}/%{_javadocdir}/%{name}

# manual
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}/tutorial
cp -pr tutorial/* %{buildroot}/%{_docdir}/%{name}-%{version}/tutorial

%files -f .mfiles
%license License.html

%files demo
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}

%files manual
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/tutorial

%changelog
