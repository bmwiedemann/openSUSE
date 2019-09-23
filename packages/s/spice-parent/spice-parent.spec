#
# spec file for package spice-parent
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           spice-parent
Version:        26
Release:        0
Summary:        Sonatype Spice Components
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://github.com/sonatype/oss-parents
Source0:        http://repo1.maven.org/maven2/org/sonatype/spice/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://apache.org/licenses/LICENSE-2.0.txt
Patch0:         pom.patch
BuildRequires:  forge-parent
BuildRequires:  javapackages-local
Requires:       mvn(org.sonatype.forge:forge-parent:pom:)
BuildArch:      noarch

%description
Spice components and libraries are common components
used throughout the Sonatype Forge.

%prep
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} .

#Remove plexus-javadoc
%patch0

%pom_xpath_remove pom:project/pom:parent/pom:relativePath

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
