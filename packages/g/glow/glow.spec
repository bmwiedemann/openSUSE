#
# spec file for package glow
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{go_nostrip}
# Disable LTO flags to stop builds failing on some architectures
%global _lto_cflags %nil

Name:           glow
Version:        2.1.1
Release:        0
Summary:        Render markdown on the CLI
License:        MIT
URL:            https://github.com/charmbracelet/glow
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# vendoring obtained by `osc service manualrun`. See README.suse-maint.md for details.
Source1:        vendor.tar.zst
Source2:        README.suse-maint.md
Source3:        fix-CVE-2025-47911_CVE-2025-58190.patch
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.23

%description
Glow is a terminal based markdown reader designed from the ground up to bring
out the beauty—and power—of the CLI.

Use it to discover markdown files, read documentation directly on the command
line and stash markdown files to your own private collection so you can read
them anywhere. Glow will find local markdown files in subdirectories or a local
Git repository.

%package bash-completion
Summary:        Bash Completion for %{name}
BuildRequires:  bash-completion
Supplements:    (%{name} and bash-completion)
Requires:       %{name}
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
Requires:       %{name}
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
BuildRequires:  zsh
Supplements:    (%{name} and zsh)
Requires:       %{name}
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a1 -p1
patch -d vendor/golang.org/x/net/ -p1 -i %{SOURCE3}

%build
%ifnarch ppc64
BUILDMOD="-buildmode=pie"
%endif
export CGO_CFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
export CGO_CPPFLAGS="%{optflags}"
export GOFLAGS="-mod=vendor $BUILDMOD -trimpath -ldflags=-linkmode=external"
mkdir -p build
go build -v -ldflags "-s -X main.Version=%{version}" -o build .

%install
install -D -m 0755 -t %{buildroot}%{_bindir} build/%{name}

# man page (and fix date)
install -d -m 0755 %{buildroot}%{_mandir}/man1
_d="$(date -u -d@$SOURCE_DATE_EPOCH '+%%B %%Y')"
./build/%{name} man | \
  sed -e "s/^\.TH GLOW 1 \".*\" \"glow/.TH GLOW 1 \"$_d\" \"glow %{version}/" \
  > %{buildroot}%{_mandir}/man1/%{name}.1

# Completions
for sh in bash fish zsh; do
  ./build/%{name} completion $sh > %{name}.${sh}
done
install -D -m 0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m 0644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m 0644 %{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
./build/%{name} --version
# Skip TestGlowSources and TestURLParser as they can both fail without internet.
go test -v ./... -skip 'TestGlowSources|TestURLParser'

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%changelog
