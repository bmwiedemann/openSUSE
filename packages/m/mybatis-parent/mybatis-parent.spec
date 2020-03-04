#
# spec file for package mybatis-parent
#
# Copyright (c) 2020 SUSE LLC
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


Name:           mybatis-parent
Version:        31
Release:        0
Summary:        The MyBatis parent POM
License:        Apache-2.0
URL:            https://www.mybatis.org/
Source0:        https://github.com/mybatis/parent/archive/%{name}-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-ssh)
BuildArch:      noarch

%description
The MyBatis parent POM which has to be inherited by all MyBatis modules.

%prep
%setup -q -n parent-%{name}-%{version}
# require com.github.stephenc.wagon:wagon-gitsite:0.4.1
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
# unavailable plugins
%pom_remove_plugin org.apache.maven.plugins:maven-pdf-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin com.mycila:license-maven-plugin
%pom_remove_plugin org.gaul:modernizer-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin

# animal-sniffer is currently broken. it uses asm4, but asm3 is loaded
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_remove_plugin :maven-scm-plugin

%build

%{mvn_build}

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%changelog
