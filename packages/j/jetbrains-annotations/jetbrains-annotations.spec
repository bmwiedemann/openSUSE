#
# spec file for package jetbrains-annotations
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
BuildRequires:  javapackages-local >= 6
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

%build
%{ant} jar javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/annotations-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a com.intellij:annotations

install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
