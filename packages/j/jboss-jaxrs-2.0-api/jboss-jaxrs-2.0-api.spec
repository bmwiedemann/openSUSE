#
# spec file for package jboss-jaxrs-2.0-api
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-jaxrs-api_2.0_spec
Name:           jboss-jaxrs-2.0-api
Version:        1.0.1
Release:        0
Summary:        JAX-RS 2.0: The Java API for RESTful Web Services
License:        Apache-2.0 AND (CDDL-1.0 OR GPL-2.0-only)
URL:            https://github.com/jboss/jboss-jaxrs-api_spec
Source0:        https://github.com/jboss/jboss-jaxrs-api_spec/archive/%{oname}-%{namedversion}/jboss-jaxrs-api_spec-%{oname}-%{namedversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
JSR 339: JAX-RS 2.0: The Java API for RESTful Web Services.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaxrs-api_spec-%{oname}-%{namedversion}

%pom_remove_plugin :maven-source-plugin

%pom_add_dep javax.xml.bind:jaxb-api::provided

%{mvn_file} :%{oname} %{name}

%{mvn_alias} ":jboss-jaxrs-api_2.0_spec" "org.jboss.resteasy:jaxrs-api"

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
