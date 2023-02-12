#
# spec file for package glab
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021-2022 Orville Q. Song <orville@anislet.dev>
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


%global build_date      2021-01-11

%global provider        github
%global provider_tld    com
%global project         profclems
%global repo            glab
%global provider_prefix %{provider}.%{provider_tld}/%{project}
%global import_path     %{provider_prefix}/%{repo}

Name:           glab
Version:        1.25.3
Release:        0
Summary:        An open-source GitLab command line tool
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/profclems/glab
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.16
Suggests:       glab-doc

%description
glab is an open-source GitLab command line tool bringing GitLab's cool features to your command line.

%package doc
Summary:        Documentation for GLab
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
glab is an open-source GitLab command line tool bringing GitLab's cool features to your command line.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%{go_nostrip}
%{go_provides}

%prep
%setup -q -n %{name}-%{version}
%setup -a1 %{SOURCE1}

%build
%goprep .
mkdir -p vendor/%{provider_prefix}
ln -s . vendor/%{import_path}
%gobuild -mod=vendor -ldflags "-s -w -X main.version=%{version} -X main.build=%{build_date} -X main.debugMode=false" ./cmd/glab

# Build HTML docs
go run -v -p 4 -x -mod=vendor ./cmd/gen-docs/
make -C docs html

# Build manpages
go run -v -p 4 -x -mod=vendor ./cmd/gen-docs/ -m --path ./docs/build/man
gzip -r ./docs/build/man

# Generate completion files
go run -v -p 4 -x -mod=vendor ./cmd/glab/ completion -s bash > %{name}.bash
go run -v -p 4 -x -mod=vendor ./cmd/glab/ completion -s zsh > %{name}.zsh
go run -v -p 4 -x -mod=vendor ./cmd/glab/ completion -s fish > %{name}.fish

%install
%goinstall

# Install HTML docs
for i in $(find ./docs/build/html/ -type f | grep -vE "_source|.buildinfo|objects.inv"); do install -D -m0644 $i %{buildroot}%{_docdir}/%{name}/$(echo $i | sed -e s@^./docs/build/html/@@); done;

# Install manpages
for i in $(find ./docs/build/man/ -type f); do install -D -m0644 $i %{buildroot}%{_mandir}/man1/$(echo $i | sed -e s@^./docs/build/man/@@); done;

# Install comletion files
install -D -m0644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -D -m0644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_mandir}/*/*
%{_bindir}/%{name}

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/README.md

%files bash-completion
%dir %{_datadir}/bash-completion/
%{_datadir}/bash-completion/completions/

%files fish-completion
%dir %{_datadir}/fish/
%{_datadir}/fish/vendor_completions.d/

%files zsh-completion
%dir %{_datadir}/zsh/
%{_datadir}/zsh/site-functions/

%changelog
