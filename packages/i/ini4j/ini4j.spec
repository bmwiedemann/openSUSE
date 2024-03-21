#
# spec file for package ini4j
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ini4j
Version:        0.5.4
Release:        0
Summary:        Java API for handling Windows ini file format
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.ini4j.org/
Source0:        https://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}-src.zip
Source1:        %{name}.build.xml
Patch0:         ini4j-java8-compat.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
Requires:       java
BuildArch:      noarch

%description
The [ini4j] is a simple Java API for handling configuration files in
Windows .ini format. Additionally, the library includes Java
Preferences API implementation based on the .ini file.

%package javadoc
Summary:        Java API for handling Windows ini file format
Group:          Development/Libraries/Java
Requires(post): /bin/ln
Requires(post): /bin/rm
Requires(postun): /bin/rm

%description javadoc
The [ini4j] is a simple Java API for handling configuration files in
Windows .ini format. Additionally, the library includes Java
Preferences API implementation based on the .ini file.

%prep
%setup -q

cp %{SOURCE1} build.xml

%patch -P 0 -p1

%build
%{ant} package javadoc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}/%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
