#
# spec file for package apache-commons-text
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


%global base_name text
%global short_name commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.10.0
Release:        0
Summary:        A library focused on algorithms working on strings
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-text/
Source0:        http://archive.apache.org/dist/commons/text/source/commons-text-%{version}-src.tar.gz
Source1:        %{name}-build.xml
Source2:        http://archive.apache.org/dist/commons/text/source/commons-text-%{version}-src.tar.gz.asc
Source3:        https://www.apache.org/dist/commons/KEYS#/%{name}.keyring
BuildRequires:  ant
BuildRequires:  apache-commons-lang3
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Apache Commons Text is a library focused on algorithms working on strings.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-text-%{version}-src
cp %{SOURCE1} build.xml

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.commons</groupId>"

%build
mkdir -p lib
build-jar-repository -s lib apache-commons-lang3
%{ant} package javadoc

%install
# jars
install -dm 755 %{buildroot}%{_javadir}/%{name}
install -m 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{short_name}.jar

# pom
install -dm 755 %{buildroot}%{_mavenpomdir}/%{name}
install -m 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{short_name}.pom
%add_maven_depmap %{name}/%{short_name}.pom %{name}/%{short_name}.jar

# javadoc
install -dm 755 %{buildroot}/%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt NOTICE.txt

%changelog
