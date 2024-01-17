#
# spec file for package aopalliance
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


Name:           aopalliance
Version:        1.0
Release:        0
Summary:        Java/J2EE AOP standards
License:        SUSE-Public-Domain
Group:          Development/Libraries/Java
URL:            https://aopalliance.sourceforge.net/
# cvs -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance login
# password empty
# cvs -z3 -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        aopalliance-src.tar.gz
Patch0:         aopalliance-manifest.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Aspect-Oriented Programming (AOP) offers a better solution to many
problems than do existing technologies, such as EJB.  AOP Alliance
facilitates and standardizes the use of AOP.

This package contains APIs for program instrumentation, interception
mechanisms, and a set of interfaces for implementing a generic
reflection API.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
# Inject OSGi manifest required by Eclipse.
%patch0 -p1

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} \
  -Dant.build.javac.source=1.8 \
  -Dant.build.javac.target=1.8 \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# maven metadata
%add_maven_depmap aopalliance:aopalliance:%{version} %{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
