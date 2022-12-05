#
# spec file for package jetbrains-annotations
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


%global oname annotations
Name:           jetbrains-annotations
Version:        23.0.0
Release:        0
Summary:        IntelliJ IDEA Annotations
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.jetbrains.org
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/org/jetbrains/annotations/%{version}/annotations-%{version}.pom
Source2:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
A set of annotations used for code inspection support and code documentation.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
cp -p %{SOURCE2} build.xml

%{mvn_file} org.jetbrains:%{oname} %{name}
%{mvn_alias} org.jetbrains:%{oname} com.intellij:

%{mvn_artifact} %{SOURCE1} target/annotations-%{version}.jar

%build
%{ant} jar javadoc

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
