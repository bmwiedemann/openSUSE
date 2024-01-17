#
# spec file for package german-pos-dict
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


Name:           german-pos-dict
Version:        1.1
Release:        0
Summary:        German part-of-speech dictionary
License:        CC-BY-SA-4.0
URL:            http://danielnaber.de/morphologie/
Source0:        https://github.com/languagetool-org/%{name}/archive/v%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(org.carrot2:morfologik-fsa)
BuildRequires:  mvn(org.carrot2:morfologik-stemming)
BuildArch:      noarch

%description
A German part-of-speech (POS) dictionary as a Morfologik binary

%prep
%setup -q
%pom_remove_plugin :nexus-staging-maven-plugin

%build
%{mvn_build} -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%changelog
