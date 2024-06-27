#
# spec file for package helmfile
#
# Copyright (c) 2024 SUSE LLC
#               2021-2024 Manfred Hollstein <manfred.h@gmx.net>
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


%define git_commit 655e1f96a410738290662942a93337875b151b99
Name:           helmfile
Version:        0.166.0
Release:        0
Summary:        Deploy Kubernetes Helm Charts
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/helmfile/helmfile
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Requires:       helm >= 3.13.1
Recommends:     helm >= 3.14.0
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.22
Obsoletes:      %{name}-bash-completion < %{version}
Obsoletes:      %{name}-zsh-completion < %{version}

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
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%setup -qa1

%build
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
SOURCE_DATE_EPOCH=$(date -u -d "${modified}" "+%s")
export SOURCE_DATE_EPOCH
rm -f source_date_epoch
echo SOURCE_DATE_EPOCH=$SOURCE_DATE_EPOCH > source_date_epoch
go build -mod=vendor -buildmode=pie

%install
. ./source_date_epoch
export SOURCE_DATE_EPOCH
make TAG=v%{version} install
mkdir -p %{buildroot}%{_bindir}
install -m755 ${HOME}/go/bin/helmfile %{buildroot}/%{_bindir}/helmfile
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/helmfile completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/helmfile completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/helmfile completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/helmfile

%files bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%files fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
