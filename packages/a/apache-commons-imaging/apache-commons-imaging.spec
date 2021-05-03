#
# spec file for package apache-commons-imaging
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


%global base_name imaging
%global short_name commons-%{base_name}
%global base_ver 1.0
%global pre_ver alpha2
Name:           apache-%{short_name}
Version:        %{base_ver}~%{pre_ver}
Release:        0
Summary:        Apache Commons Imaging
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-csv/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{base_ver}-%{pre_ver}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildArch:      noarch

%description
Apache Commons Imaging (previously Sanselan) is a pure-Java image library.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{base_ver}-%{pre_ver}-src
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
