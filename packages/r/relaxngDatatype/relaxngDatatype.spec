#
# spec file for package relaxngDatatype
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           relaxngDatatype
Version:        2011.1
Release:        0
Summary:        RELAX NG Datatype API
License:        BSD-3-Clause
Group:          Development/Languages/Java
URL:            https://sourceforge.net/projects/relaxng
Source0:        https://github.com/java-schema-utilities/relaxng-datatype-java/archive/relaxngDatatype-%{version}.tar.gz
# License is not available in the tarball, this copy fetched from the tarball on the old sourceforge.net site
Source1:        copying.txt
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Obsoletes:      %{name}-javadoc
BuildArch:      noarch

%description
RELAX NG is a public space for test cases and other ancillary software
related to the construction of the RELAX NG language and its
implementations.

%prep
%setup -q -n relaxng-datatype-java-relaxngDatatype-%{version}
cp -p %{SOURCE1} .

%pom_remove_parent .

%build
ant \
    -Dbuild.sysclasspath=only \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6

%install
install -Dpm 644 %{name}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a relaxngDatatype:relaxngDatatype

%files -f .mfiles
%license copying.txt
%{_javadir}/*.jar

%changelog
