#
# spec file for package minlog
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


Name:           minlog
Version:        1.3.1
Release:        0
Summary:        Minimal overhead Java logging
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/EsotericSoftware/minlog
Source0:        https://github.com/EsotericSoftware/minlog/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
MinLog is a Java logging library. Key features:

* Zero overhead Logging statements below a given level
  can be automatically removed by javac at compile time.
  This means applications can have detailed trace and
  debug logging without having any impact on the finished product.

* Simple and efficient The API is concise and the code
  is very efficient at run-time.

* Extremely lightweight The entire project consists of a single
  Java file with ~100 non-comment lines of code.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find -name "*.class" -delete
find -name "*.jar" -delete

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions"

sed -i 's/\r//' license.txt

%{mvn_file} :%{name} %{name}
%{mvn_alias} :%{name} "com.googlecode:%{name}" "com.esotericsoftware.%{name}:%{name}"
%{mvn_package} ":%{name}::tests:"

%build

%{mvn_build}

%install
%{mvn_install}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
