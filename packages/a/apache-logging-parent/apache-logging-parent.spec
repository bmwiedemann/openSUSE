#
# spec file for package apache-logging-parent
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


Name:           apache-logging-parent
Version:        2
Release:        0
Summary:        Parent pom for Apache Logging Services projects
License:        Apache-2.0
URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/logging-parent/%{version}/logging-parent-%{version}-source-release.zip
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache:apache:pom:)
BuildArch:      noarch

%description
Parent pom for Apache Logging Services projects.

%prep
%setup -q -n logging-parent-%{version}

%build
%{mvn_build}

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
