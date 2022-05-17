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


Name:           j2objc-annotations
Version:        2.2
Release:        0
Summary:        J2ObjC Annotations
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/j2objc
Source0:        %{name}-%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/google/j2objc/master/LICENSE
Source2:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8 javapackages-local
BuildArch:      noarch

%description
A set of annotations that provide additional information to
the J2ObjC translator to modify the result of translation.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} build.xml

%pom_remove_parent

%build
%{ant} jar javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%doc %{_javadocdir}/%{name}
%license LICENSE

%changelog
