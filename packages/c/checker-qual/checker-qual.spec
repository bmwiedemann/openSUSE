#
# spec file for package j2objc-annotations
#
# Copyright (c) 2022 SUSE LLC
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


Name:           checker-qual
Version:        3.22.0
Release:        0
Summary:        Checker Qual
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/typetools/checker-framework
Source0:        https://github.com/typetools/checker-framework/archive/refs/tags/checker-framework-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/checkerframework/%{name}/%{version}/%{name}-%{version}.pom
Source2:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8 javapackages-local
BuildArch:      noarch

%description
Checker Qual contains annotations (type qualifiers) that a programmer
writes to specify Java code for type-checking by the Checker Framework.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n checker-framework-checker-framework-%{version}
cp %{SOURCE2} %{name}/build.xml

%build
pushd %{name}
%{ant} jar javadoc
popd

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 %{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr %{name}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license %{name}/LICENSE.txt

%files javadoc
%doc %{_javadocdir}/%{name}
%license %{name}/LICENSE.txt

%changelog
