#
# spec file for package leiningen
#
# Copyright (c) 2022 SUSE LLC
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


Name:           leiningen
# Change LEIN_VERSION in lein-pkg when bumping
Version:        2.10.0
Release:        0
Summary:        Automation for Clojure projects
License:        EPL-1.0
Group:          Development/Tools/Building
URL:            https://leiningen.org/
Source0:        https://github.com/technomancy/leiningen/releases/download/%{version}/leiningen-%{version}-standalone.jar
# Following files are taken from the upstream repo in the `doc` and `bin` subfolders:
Source1:        https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein-pkg
Source2:        https://raw.githubusercontent.com/technomancy/leiningen/stable/bash_completion.bash
Source3:        https://raw.githubusercontent.com/technomancy/leiningen/stable/zsh_completion.zsh
Source4:        https://raw.githubusercontent.com/technomancy/leiningen/stable/doc/lein.1
BuildRequires:  fdupes
Requires:       clojure >= 1.10.0
Requires:       java >= 1.8.0
BuildArch:      noarch

%description
Working on Clojure projects with tools designed for Java can be an
exercise in frustration. With Leiningen, builds can be describe with
Clojure. Leiningen handles fetching dependencies, running tests,
packaging projects and can be extended with a number of plugins.

%prep

%build

%install
#LEIN_JAR =
mkdir -p %{buildroot}%{_datadir}/java/
install -m 0644 -D %{SOURCE0} %{buildroot}%{_datadir}/java/leiningen-%{version}-standalone.jar
install -m 0755 -D %{SOURCE1} %{buildroot}%{_bindir}/lein
install -m 0644 -D %{SOURCE2} %{buildroot}%{_datadir}/bash-completion/completions/lein
install -m 0644 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/zsh_completion.d/_lein
install -m 0644 -D %{SOURCE4} %{buildroot}%{_mandir}/man1/lein.1

%fdupes %{buildroot}/%{_prefix}

%files
%{_bindir}/lein
%{_mandir}/man1/lein*
%{_datadir}/bash-completion/completions/lein
%{_sysconfdir}/zsh_completion.d
%dir %{_datadir}/java
%{_datadir}/java/leiningen-%{version}-standalone.jar

%changelog
