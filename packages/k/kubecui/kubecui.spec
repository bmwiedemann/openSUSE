#
# spec file for package kubecui
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


Name:           kubecui
Version:        1.0.2
Release:        0
Summary:        Simple but still extremely powerful K9S alternative
License:        MIT
URL:            https://github.com/pymag09/kubecui
Source0:        %{name}-%{version}.tar.gz
Source1:        etc_profile.d_kubecui.sh
BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  filesystem
Requires:       bash
Requires:       fzf
Requires:       jq
Recommends:     trivy
Recommends:     tmux
Recommends:     tmuxp
Recommends:     kube-no-trouble

%description
kubeui makes kubectl more user friendly. This is still kubectl but enhanced
with fzf.

I believe, anybody who is new to kubernetes, must use kubectl. Because kubectl
is the basics.

However, kubectl slows you down - requires heavy keyboard typing. In order to
alleviate interaction with kubernetes API and describe the fields associated
with each supported API resource directly in the Terminal, kubectl was
complemented by fzf.

%prep
%autosetup -p 1

%build
cp %{SOURCE1} ./etc_profile.d_kubecui.sh

%install
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -D -m 0755 kubecui.sh %{buildroot}/%{_datadir}/%{name}/kubecui.sh
install -D -m 0755 init.sh %{buildroot}/%{_datadir}/%{name}/init.sh
install -D -m 0755 kui_start.sh %{buildroot}/%{_datadir}/%{name}/kui_start.sh

cp -vr fx/ %{buildroot}%{_datadir}/%{name}

install -d -m 0755 %{buildroot}%{_sysconfdir}/profile.d/
cp etc_profile.d_kubecui.sh %{buildroot}%{_sysconfdir}/profile.d/kubecui.sh

%files
%doc README.md
%license LICENSE
%{_datadir}/%{name}
%{_sysconfdir}/profile.d/kubecui.sh

%changelog
