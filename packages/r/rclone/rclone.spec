#
# spec file for package rclone
#
# Copyright (c) 2025 SUSE LLC
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
# nodebuginfo


Name:           rclone
Version:        1.70.2
Release:        0
Summary:        Rsync for cloud storage
License:        MIT
Group:          Productivity/Networking/Web/Utilities
URL:            https://rclone.org/
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  fdupes
BuildRequires:  go >= 1.20
BuildRequires:  golang-packaging
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11
%else
BuildRequires:  gcc
%endif

%description
rsync for cloud storage. rclone is a command line program to sync files and
directories to and from a wide variety of cloud storage providers, providing
various additional features.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Networking/Web/Utilities
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          Productivity/Networking/Web/Utilities
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q
%setup -q -D -T -a 1
%autopatch -p1

%build
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-11"
%endif
# pie not supported on ppc64
go build -o %{name} \
%ifnarch ppc64
  -buildmode=pie \
%endif
  -mod=vendor \
  --ldflags '-X github.com/rclone/rclone/fs.Version=v%{version}'

./%{name} version

./%{name} genautocomplete bash completion.bash
./%{name} genautocomplete zsh  completion.zsh

%install
install -m0755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -m0644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

install -m0644 -D completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -m0644 -D completion.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%fdupes %{buildroot}

%files
%doc MANUAL.md README.md RELEASE.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{name}

%changelog
