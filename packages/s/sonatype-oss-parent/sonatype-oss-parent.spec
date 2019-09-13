#
# spec file for package sonatype-oss-parent
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


Name:           sonatype-oss-parent
Version:        7
Release:        0
Summary:        Sonatype OSS Parent
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/sonatype/oss-parents
# git clone git://github.com/sonatype/oss-parents.git
# (cd ./oss-parents; git archive --prefix %{name}-%{version}/ oss-parent-%{version}) | xz >%{name}-%{version}.tar.xz
Source:         %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  xz
BuildArch:      noarch

%description
Sonatype OSS parent pom used by other sonatype packages.

%prep
%setup -q
cp -p %{SOURCE1} LICENSE
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

%build

%install
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/oss-parent.pom
%add_maven_depmap %{name}/oss-parent.pom

%files -f .mfiles
%license LICENSE

%changelog
