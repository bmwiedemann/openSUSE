#
# spec file for package yq
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


%global provider_prefix github.com/mikefarah/yq
%global import_path     %{provider_prefix}

Name:           yq
Version:        4.30.6
Release:        0
Summary:        A portable command-line YAML processor
License:        MIT
URL:            https://github.com/mikefarah/yq
Source0:        https://github.com/mikefarah/yq/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# conflict with all python3X-yq packages since they install /usr/bin/yq
# we need to handle Leap 15.4 specially since the python3dist() is not
# generated there
%if 0%{?suse_version} >= 1550
Conflicts:      python3dist(yq)
%else
Conflicts:      python3-yq
%endif
BuildRequires:  golang(API) = 1.19

%description
A lightweight and portable command-line YAML processor. yq uses jq like syntax
but works with yaml files as well as json. It doesn't yet support everything
jq does - but it does support the most common operations and functions, and more
is being added continuously.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%setup -qa1

%build
go build -buildmode=pie -mod=vendor -o bin/%{name}

%install
install -D -m 0755 ./bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/%{name} shell-completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/%{name} shell-completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/%{name} shell-completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files bash-completion
%defattr(-,root,root)
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%files fish-completion
%defattr(-,root,root)
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%files bash-completion
%defattr(-,root,root)
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%changelog
