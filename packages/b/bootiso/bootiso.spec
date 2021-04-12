#
# spec file for package bootiso
#
# Copyright (c) 2021 SUSE LLC
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


Name:           bootiso
Version:        4.2.0
Release:        0
License:        GPL-3.0-only
Group:          Development/Tools/Other
Summary:        A bash script to securely create a bootable USB device from one image file
URL:            https://github.com/jsamr/bootiso
Source:         https://github.com/jsamr/bootiso/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          syslinux-lib-root.patch
BuildArch:      noarch
Requires:       bc
Requires:       jq
Requires:       syslinux
Requires:       wimtools
# zsh needed for installing completion
BuildRequires:  zsh

%description
A bash program to securely and easily create a bootable USB device from one image file

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (bootiso and bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Supplements:    (bootiso and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%prep
%autosetup

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/man/man1
install -Dm755  %{name}                            '%{buildroot}%{_bindir}/%{name}'
install -Dm644  extra/completions/completions.zsh  '%{buildroot}%{_datadir}/zsh/site-functions/_%{name}'
install -Dm644  extra/completions/completions.bash '%{buildroot}%{_datadir}/bash-completion/completions/%{name}'
install -Dm644  extra/man/%{name}.1                '%{buildroot}%{_datadir}/man/man1/%{name}.1'

%files
%license LICENSE
%doc changelog.md readme.md
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.*

%files zsh-completion
%{_datadir}/zsh/site-functions/_bootiso

%files bash-completion
%{_datadir}/bash-completion/completions/bootiso

%changelog
