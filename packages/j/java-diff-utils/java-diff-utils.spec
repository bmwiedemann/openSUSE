#
# spec file for package java-diff-utils
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


Name:           java-diff-utils
Version:        4.12
Release:        0
Summary:        A Java library for performing the comparison operations between texts
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://java-diff-utils.github.io/%{name}/
Source:         https://github.com/%{name}/java-diff-utils/archive/refs/tags/%{name}-parent-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildArch:      noarch

%description
Diff Utils library is an OpenSource library for performing the comparison
operations between texts: computing diffs, applying patches, generating unified
diffs or parsing them, generating diff output for easy future displaying (like
side-by-side view) and so on.

Main reason to build this library was the lack of easy-to-use libraries with
all the usual stuff you need while working with diff files. Originally it was
inspired by JRCS library and it's nice design of diff module.

This is originally a fork of java-diff-utils from Google Code Archive.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{name}-parent-%{version}
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc {README,CHANGELOG}.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
