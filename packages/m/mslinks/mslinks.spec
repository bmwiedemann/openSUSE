#
# spec file for package reload4j
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


Name:           mslinks
Version:        1.0.6.2
Release:        0
Summary:        Library for parsing and creating Windows shortcut files
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/vatbub/mslinks.git
Source0:        %{name}-%{version}.tar.xz
Patch0:         0001-Java-8-compatibility.patch
BuildRequires:  maven-local fdupes java-devel >= 9
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildArch:      noarch

%description
Library for parsing and creating Windows shortcut files (.lnk)

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1

%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

%build
%mvn_build -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
