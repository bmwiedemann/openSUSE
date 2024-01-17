#
# spec file for package fubectl
#
# Copyright (c) 2023 SUSE LLC
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


Name:           fubectl
Version:        0.0.1~alpha.1687425183.3950b1e
Release:        0
Summary:        Fancy kubectl
License:        Apache-2.0
URL:            https://github.com/kubermatic/fubectl
Source:         fubectl-%{version}.tar.gz
BuildArch:      noarch
Requires:       (bash or zsh)
Requires:       fzf
Requires:       jq
Requires:       kubectl-tree
Requires:       kubectl-neat

%description
Reduces repetitive interactions with kubectl

%prep
%setup -q

%build
sed -i '/^#!/ s/env\ bash/bash/' %{name}.source

%install
# Install the script.
install -D -m 0755 %{name}.source %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
chmod 644 %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

%files
%doc README.md
%license LICENSE
%{_datarootdir}/bash-completion/completions/%{name}

%changelog
