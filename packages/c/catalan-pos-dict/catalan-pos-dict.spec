#
# spec file for package catalan-pos-dict
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


Name:           catalan-pos-dict
Version:        2.7+git6dc3553
Release:        0
Summary:        German part-of-speech dictionary
License:        GPL-2.0-only OR LGPL-2.1-only
URL:            https://github.com/Softcatala/catalan-dict-tools
Source0:        %{name}-%{version}.tar.xz
Patch0:         catalan-pos-dict-classpath.patch
BuildRequires:  bash
BuildRequires:  languagetool-tools
BuildRequires:  maven-local
BuildRequires:  mvn(org.carrot2:morfologik-fsa)
BuildRequires:  mvn(org.carrot2:morfologik-stemming)
BuildArch:      noarch

%description
A Catalan part-of-speech (POS) dictionary as a Morfologik binary

%prep
%setup -q
%patch0 -p1
%pom_remove_plugin :nexus-staging-maven-plugin resultats/java-lt

%build
LT_TOOLS_CLASSPATH=$(build-classpath languagetool morfologik-stemming commons-cli beust-jcommander hppc) \
bash build-morfologik-lt.sh

pushd resultats/java-lt
%{mvn_build} -f
popd

%install
pushd resultats/java-lt
%mvn_install
popd

%files -f resultats/java-lt/.mfiles
%license resultats/java-lt/LICENSE
%license resultats/java-lt/gpl-2.0.txt
%license resultats/java-lt/lgpl-2.1.txt
%doc resultats/java-lt/README.md

%changelog
