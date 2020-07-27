#
# spec file for package bean-validation-api
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           bean-validation-api
Version:        2.0.1
Release:        0
Summary:        Bean Validation API (JSR 349)
License:        Apache-2.0
URL:            https://beanvalidation.org/
Source0:        https://github.com/beanvalidation/beanvalidation-api/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
This package contains Bean Validation (JSR-349) API.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n beanvalidation-api-%{namedversion}

%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%{mvn_file} : %{name}

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license license.txt copyright.txt

%files javadoc -f .mfiles-javadoc
%doc README.md
%license license.txt copyright.txt

%changelog
