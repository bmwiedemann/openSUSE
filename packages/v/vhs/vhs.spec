#
# spec file for package vhs
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


%global _lto_cflags %nil
Name:           vhs
Version:        0.9.0
Release:        0
Summary:        CLI video recorder
URL:            https://github.com/charmbracelet/vhs
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
License:        MIT
BuildRequires:  zstd
BuildRequires:  golang(API)
Requires:       ffmpeg
Requires:       ttyd
Recommends:     %{name}-doc = %{version}

%description
VHS records your terminal as videos or gifs for demos.

%package doc
Summary:        Documentation for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch

%description doc
Documentation files and examples for %{name}.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name} = %{version}
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name} = %{version}
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a1
# Delete outputs from examples.
find examples -name '*.mp4' -delete \
  -or -name '*.webm' -delete \
  -or -name '*.gif' -delete \
  -or -name '*.png' -delete

%build
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export CGO_CFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
export CGO_CPPFLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.Version=%{version}"

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

# Completions
for sh in bash zsh fish; do
  ./%{name} completion $sh > %{name}.${sh}
done
install -Dm644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%check
go test -v ./...

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%files doc
%doc examples

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
