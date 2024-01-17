#
# spec file for package sonatype-plugins-parent
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


%global tag a594629
Name:           sonatype-plugins-parent
Version:        8
Release:        0
Summary:        Sonatype Plugins Parent POM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/sonatype/oss-parents
Source:         https://github.com/sonatype/oss-parents/tarball/plugins-parent-%{version}#/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  forge-parent
BuildRequires:  maven-local
BuildArch:      noarch

%description
This package provides Sonatype plugins parent POM used by other Sonatype
packages.

%prep
%setup -q -n sonatype-oss-parents-%{tag}
cp -p %{SOURCE1} LICENSE

%build
cd ./plugins-parent
%{mvn_build}

%install
cd ./plugins-parent
%mvn_install

%files -f plugins-parent/.mfiles
%license LICENSE

%changelog
