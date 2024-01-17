#
# spec file for package opennlp-postag-models
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


Name:           opennlp-postag-models
Version:        1.5
Release:        0
Summary:        OpenNLP Postag Models
License:        Apache-2.0
URL:            https://opennlp.sourceforge.net
Source0:        https://repo1.maven.org/maven2/edu/washington/cs/knowitall/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildArch:      noarch

%description
Stock OpenNLP postag models. Maxent model with tag dictionary.

%prep
%setup -q -c
cp %{SOURCE1} LICENSE
%pom_remove_parent

%build
jar -cf %{name}-%{version}.jar *.bin

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar

%files -f .mfiles
%license LICENSE

%changelog
