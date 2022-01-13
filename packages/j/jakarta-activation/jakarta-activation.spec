#
# spec file for package jakarta-activation
#
# Copyright (c) 2021 SUSE LLC
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


Name:           jakarta-activation
Version:        2.1.0
Release:        0
Summary:        Jakarta Activation Specification and Implementation
License:        BSD-3-Clause
URL:            https://eclipse-ee4j.github.io/jaf/
Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/jaf-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaf-%{version}

%pom_remove_parent api
%pom_remove_plugin :maven-enforcer-plugin api
%pom_remove_plugin :build-helper-maven-plugin api
%pom_remove_plugin :buildnumber-maven-plugin api

%build
pushd api
%{mvn_build} -f
popd

%install
pushd api
%mvn_install
popd
%fdupes -s %{buildroot}%{_javadocdir}

%files -f api/.mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%files javadoc -f api/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
