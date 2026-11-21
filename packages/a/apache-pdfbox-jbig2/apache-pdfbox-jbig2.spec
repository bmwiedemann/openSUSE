#
# spec file for package apache-pdfbox-jbig2
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global short_name pdfbox-jbig2
Name:           apache-%{short_name}
Version:        3.0.5
Release:        0
Summary:        Java ImageIO plugin for JBIG2
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/apache/%{short_name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildArch:      noarch

%description
The Java ImageIO plugin for JBIG2 enables access to images encoded using the
JBIG2 image compression standard. This component is part of the Apache PDFBox®
project.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}

%pom_xpath_set 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:source' 8
%pom_xpath_set 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:target' 8

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin com.googlecode.maven-download-plugin:download-maven-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license {NOTICE,LICENSE}.txt
%doc RELEASE-NOTES.txt README.md

%files javadoc -f .mfiles-javadoc
%license {NOTICE,LICENSE}.txt

%changelog
