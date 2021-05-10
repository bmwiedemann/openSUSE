#
# spec file for package helmfile
#
# Copyright (c) 2021 SUSE LLC
#               2021 Manfred Hollstein <manfred.h@gmx.net>
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

%define git_commit efa404e2750868e7ecc70641bc22c26113019e94
Name:           helmfile
Version:        0.139.2
Release:        0
Summary:        Deploy Kubernetes Helm Charts
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/roboll/helmfile
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Requires:       helm
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.16
%{go_nostrip}
%{go_provides}

%description
Helmfile is a declarative spec for deploying helm charts. It lets you...

 * Keep a directory of chart value files and maintain changes in version control.
 * Apply CI/CD to configuration changes.
 * Periodically sync to avoid skew in environments.

To avoid upgrades for each iteration of helm, the helmfile executable
delegates to helm - as a result, helm must be installed.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -qa1

%build
go build -mod=vendor -buildmode=pie

%install
make TAG=v%{version} install
mkdir -p %{buildroot}%{_bindir}
install -m755 ${HOME}/go/bin/helmfile %{buildroot}/%{_bindir}/helmfile
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
install -m644 autocomplete/helmfile_bash_autocomplete \
  %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
install -m644 autocomplete/helmfile_zsh_autocomplete \
  %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/helmfile

%files bash-completion
%defattr(-,root,root)
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%changelog
