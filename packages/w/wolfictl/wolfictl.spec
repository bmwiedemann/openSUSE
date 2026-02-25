#
# spec file for package wolfictl
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


Name:           wolfictl
Version:        0.39.1
Release:        0
Summary:        A CLI used to work with the Wolfi OSS project
License:        Apache-2.0
URL:            https://github.com/wolfi-dev/wolfictl
Source:         wolfictl-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.25

%description
wolfictl is a command line tool for working with Wolfi

%package doc
Summary:        Documentation for wolfictl
Group:          Documentation/Markdown
BuildArch:      noarch

%description doc
wolfictl is a command line tool for working with Wolfi

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%setup -q
%setup -q -T -D -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -trimpath \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X sigs.k8s.io/release-utils/version.gitVersion=%{version} \
   -X sigs.k8s.io/release-utils/version.gitCommit=v%{version} \
   -X sigs.k8s.io/release-utils/version.gitTreeState=clean \
   -X sigs.k8s.io/release-utils/version.buildDate=$BUILD_DATE" \
   -o ./bin/%{name}  ./

# generate docs and manpages
go build \
   -mod=vendor \
   -buildmode=pie \
   -o ./bin/docs cmd/docs/*.go
./bin/docs --target=./docs/cmd
./bin/docs --target=./docs/man/man1 --kind=man

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

# Install manpages
mkdir -p "%{buildroot}/%{_mandir}/man1/"
cp ./docs/man/man1/* %{buildroot}%{_mandir}/man1/
find %{buildroot}%{_mandir}/man1/ -type f -exec chmod 644 {} "+"

# Install HTML docs
mkdir -p "%{buildroot}/%{_docdir}/%{name}/"
cp -vr ./docs/cmd/* %{buildroot}%{_docdir}/%{name}/
find %{buildroot}%{_docdir}/%{name}/ -type f -exec chmod 644 {} "+"
find %{buildroot}%{_docdir}/%{name}/ -type d -exec chmod 755 {} "+"

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%files
%doc README.md
%license LICENSE
%{_mandir}/*/*
%{_bindir}/%{name}

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/README.md

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
