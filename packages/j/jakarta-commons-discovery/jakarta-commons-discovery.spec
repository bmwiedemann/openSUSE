#
# spec file
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


%define short_name commons-discovery
%bcond_with tests
Name:           jakarta-%{short_name}
Version:        0.5
Release:        0
Summary:        Jakarta Commons Discovery
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://jakarta.apache.org/commons/discovery.html
Source0:        https://archive.apache.org/dist/commons/discovery/source/%{short_name}-%{version}-src.tar.gz
Source1:        https://repo1.maven.org/maven2/%{short_name}/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source100:      commons-discovery-build.xml
BuildRequires:  ant
BuildRequires:  commons-logging >= 1.1.1
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Requires:       commons-logging >= 1.1.1
Provides:       %{short_name} = %{version}
Obsoletes:      %{short_name} < %{version}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
The Discovery component is about discovering, or finding,
implementations for pluggable interfaces.  Pluggable interfaces are
specified with the intent that multiple implementations are, or will
be, available to provide the service described by the interface.
Discovery provides facilities for finding and instantiating classes and
for lifecycle management of singleton (factory) classes.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the javadoc documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE100} build.xml
mkdir -p lib

%build
build-jar-repository -s lib commons-logging
ant \
%if %{without tests}
    -Dtest.skip=true \
%endif
    package javadoc

%install
# jar
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-*.jar %{buildroot}%{_javadir}/%{short_name}.jar
(cd %{buildroot}%{_javadir} && ln -s %{short_name}.jar %{name}.jar)

install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}

%changelog
