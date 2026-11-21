#
# spec file for package open-code-review
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           open-code-review
Version:        1.13.10
Release:        0
Summary:        AI-powered code review CLI
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            https://github.com/alibaba/open-code-review
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        README.local-llm.md
# Shells own the completion dirs installed below (cf. helm)
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.26
BuildRequires:  golang-packaging
BuildRequires:  zsh
BuildRequires:  zstd
Requires:       git >= 2.41

%description
Open Code Review is an AI-powered code review CLI tool from Alibaba. It
reads Git diffs, sends changed files to a configurable LLM via an agent
with tool-use capabilities, and generates structured review comments with
line-level precision.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -a 1
cp %{SOURCE2} .
# Drop the prebuilt Gradle wrapper jar shipped for the IntelliJ IDEA
# extension (a Java bootstrap binary); the Go CLI build does not use it
# and it is not shipped.
rm -f extensions/idea/gradle/wrapper/gradle-wrapper.jar

%build
go build -mod=vendor -buildmode=pie -ldflags "-X main.Version=v%{version}" -o ocr ./cmd/opencodereview

%install
install -D -m 0755 ocr %{buildroot}%{_bindir}/ocr
ln -s ocr %{buildroot}%{_bindir}/opencodereview
# shell completions (generated from the build-tree binary, not the
# buildroot one, so the installed binary is never executed here and
# find-debuginfo can open it)
./ocr completion bash > ocr.bash
./ocr completion zsh > _ocr
./ocr completion fish > ocr.fish
install -Dm 644 ocr.bash %{buildroot}%{_datadir}/bash-completion/completions/ocr
install -Dm 644 _ocr %{buildroot}%{_datadir}/zsh/site-functions/_ocr
install -Dm 644 ocr.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/ocr.fish

%check
./ocr --help
./ocr version

%files
%license LICENSE
%doc README.md
%doc README.local-llm.md
%{_bindir}/ocr
%{_bindir}/opencodereview

%files bash-completion
%{_datadir}/bash-completion/completions/ocr

%files zsh-completion
%{_datadir}/zsh/site-functions/_ocr

%files fish-completion
%{_datadir}/fish/vendor_completions.d/ocr.fish

%changelog
