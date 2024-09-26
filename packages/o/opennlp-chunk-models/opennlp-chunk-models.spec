#
# spec file for package opennlp-chunk-models
#
# Copyright (c) 2024 SUSE LLC
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


Name:           opennlp-chunk-models
Version:        1.5
Release:        0
Summary:        OpenNLP Chunker Models
License:        Apache-2.0
URL:            https://opennlp.sourceforge.net
Source0:        https://repo1.maven.org/maven2/edu/washington/cs/knowitall/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
BuildArch:      noarch

%description
Stock OpenNLP chunker models trained on conll2000 shared task data.

%prep
%setup -q -c
cp %{SOURCE1} LICENSE

%build
jar --create --verbose \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --file=%{name}-%{version}.jar *.bin

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar

%files -f .mfiles
%license LICENSE

%changelog
