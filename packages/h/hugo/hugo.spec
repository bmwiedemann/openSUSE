#
# spec file for package hugo
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


Name:           hugo
Version:        0.126.3
Release:        0
Summary:        Static website generator written in Go
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/gohugoio/hugo
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  golang(API) >= 1.18
BuildRequires:  pkgconfig(libsass)
BuildRequires:  pkgconfig(libwebp)

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized
for speed, ease of use, and configurability, and designed to work well for any
kind of website including blogs, tumbles, and docs. Hugo takes a directory with
Markdown and templates and renders them into a full HTML website, typically in a
fraction of a second. You can run Hugo from any directory, which works well for
shared hosts and other systems where you don’t have a privileged account. Hugo
provides a Privacy Config that can assist with General Data Protection
Regulation (GDPR) compliance issues.

https://gohugo.io/

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}, generated during the build.

%prep
%autosetup -a 1

%build
# Force using the system version of libsass.
# Due to https://github.com/golang/go/issues/26366
# libsass would not be vendored properly anyway.
export CGO_CFLAGS="$(pkg-config --cflags libsass) -DUSE_LIBSASS_SRC $(pkg-config --cflags libwebp) -DLIBWEBP_NO_SRC"
export CGO_CXXFLAGS="${CGO_CFLAGS}"
export CGO_LDFLAGS="$(pkg-config --libs libsass) $(pkg-config --libs libwebp)"

# Build the binary.
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -tags extended

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Build the man pages.
%{buildroot}/%{_bindir}/%{name} gen man

# Install the man pages.
mkdir -p "%{buildroot}/%{_mandir}/man1"
install -D -m 0644 man/%{name}*.1 "%{buildroot}/%{_mandir}/man1"

# Build the shell autocomplete files
%{buildroot}/%{_bindir}/%{name} completion bash > %{name}-autocomplete.bash
%{buildroot}/%{_bindir}/%{name} completion zsh > %{name}-autocomplete.zsh

# Install the shell autocomplete files
install -Dm 644 %{name}-autocomplete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm 644 %{name}-autocomplete.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
# execute the binary as a basic check
./%{name} --help

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1.gz

%files bash-completion
%{_datadir}/bash-completion

%files zsh-completion
%{_datadir}/zsh

%changelog
