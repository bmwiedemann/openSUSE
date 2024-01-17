#
# spec file for package sbt-boilerplate
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


%global scala_short_version 2.13
Name:           sbt-boilerplate
Version:        0.6.1
Release:        0
Summary:        Generator of scala.Tuple/Function related boilerplate code
License:        BSD-2-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/sbt/sbt-boilerplate
Source0:        %{name}-%{version}.tar.xz
# Add a main method to be able to use from command line
Patch0:         0001-Command-line-generator-possible.patch
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  scala >= %{scala_short_version}
BuildRequires:  scala-parser-combinators
Requires:       javapackages-tools
Requires:       scala
Requires:       scala-parser-combinators
BuildArch:      noarch

%description
Boilerplate is an sbt-plugin that generates stubs for code which has to be
expanded for all numbers of arguments from 1 to 22. This is sometimes
necessary to support all of the TupleX or FunctionX generically.

This package contains a simple command-line tool to expand the templates
without using sbt mechanisms.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1

%build
# We do not build against sbt, so the plugin is not buildable
rm -f src/main/scala/spray/boilerplate/BoilerplatePlugin.scala

mkdir -p target/classes
scalac -d target/classes -release:8 -cp $(build-classpath scala) $(find src/main/scala/spray/boilerplate -name \*.scala | xargs)
jar -cf target/%{name}_%{scala_short_version}-%{version}.jar -C target/classes .
mkdir -p target/apidoc
scaladoc -d target/apidoc -release:8 -cp $(build-classpath scala) $(find src/main/scala/spray/boilerplate -name \*.scala | xargs)

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}_%{scala_short_version}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}_%{scala_short_version}.jar

%jpackage_script spray.boilerplate.Generator "" "" %{name}/%{name}_%{scala_short_version}:scala %{name}

install -dm 0755 %{buildroot}%{_javadocdir}
cp -r target/apidoc  %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files
%{_bindir}/%{name}
%{_javadir}/%{name}
%doc README.md
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
