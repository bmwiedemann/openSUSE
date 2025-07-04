#
# spec file for package glab
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2021-2022 Orville Q. Song <orville@anislet.dev>
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


Name:           glab
Version:        1.61.0
Release:        0
Summary:        A GitLab command line tool
License:        MIT
Group:          Development/Tools/Other
URL:            https://gitlab.com/gitlab-org/cli
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# https://sources.debian.org/src/glab/1.49.0-1/debian/patches/0001-Disable-update-check.patch
Patch0:         glab-disable_update_check.patch
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?almalinux_version} || 0%{?rocky_version}
BuildRequires:  golang >= 1.24.1
%else
BuildRequires:  go >= 1.24.1
BuildRequires:  golang-packaging
%endif
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
Suggests:       glab-doc

%description
glab is a command line tool bringing GitLab's features to the command line.

%package doc
Summary:        Documentation for GLab
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
glab is a command line tool bringing GitLab's features to the command line.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1 -n %{name}-%{version}

%build
# hash will be shortened by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go build \
        -mod=vendor \
        -buildmode=pie \
        -trimpath \
        -ldflags "-X main.version=v%{version} \
        -X main.build=${BUILD_DATE} \
        -X main.commit=${COMMIT_HASH:0:8} \
        -X main.debugMode=false" \
        ./cmd/glab

# Build HTML docs
go run ./cmd/gen-docs/docs.go

# Build manpages
go run -v -p 4 -x -mod=vendor ./cmd/gen-docs/docs.go --manpage --path ./share/man/man1
gzip -r ./share/man/man1

# Generate completion files
go run -v -p 4 -x -mod=vendor ./cmd/glab/ completion -s bash > %{name}.bash
go run -v -p 4 -x -mod=vendor ./cmd/glab/ completion -s zsh > %{name}.zsh
go run -v -p 4 -x -mod=vendor ./cmd/glab/ completion -s fish > %{name}.fish

%install
mkdir -p "%{buildroot}/%{_bindir}/"
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Install HTML docs
mkdir -p "%{buildroot}/%{_docdir}/%{name}/"
cp -vr ./docs/source/* %{buildroot}%{_docdir}/%{name}/
find %{buildroot}%{_docdir}/%{name}/ -type f -exec chmod 644 {} "+"
find %{buildroot}%{_docdir}/%{name}/ -type d -exec chmod 755 {} "+"

# Install manpages
mkdir -p "%{buildroot}/%{_mandir}/man1/"
cp ./share/man/man1/* %{buildroot}%{_mandir}/man1/
find %{buildroot}%{_mandir}/man1/ -type f -exec chmod 644 {} "+"

# Install completion files
install -D -m0644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -D -m0644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%check
%{buildroot}/%{_bindir}/%{name} version | grep %{version}

%files
%license LICENSE
%doc README.md
%{_mandir}/*/*
%{_bindir}/%{name}

%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/README.md

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%changelog
