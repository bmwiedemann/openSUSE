#
# spec file for package skopeo
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
# nodebuginfo


%define project        github.com/containers/skopeo

Name:           skopeo
Version:        1.15.1
Release:        0
Summary:        Container image repository tool
License:        Apache-2.0
Group:          System/Management
URL:            https://%project
Source:         %{name}-%{version}.tar.xz
Source1:        skopeo.rpmlintrc
Requires:       libcontainers-common
BuildRequires:  bash
BuildRequires:  device-mapper-devel >= 1.2.68
BuildRequires:  glib2-devel
BuildRequires:  go-go-md2man
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libcontainers-common
BuildRequires:  libgpgme-devel
BuildRequires:  golang(API) >= 1.21
ExcludeArch:    s390

%description
skopeo is a command line utility for various operations on container images and
image repositories. skopeo is able to inspect a repository on a Docker registry
and fetch images layers. skopeo can copy container images between various
storage mechanisms.

%package bash-completion
Summary:        Bash completion for skopeo
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
This package contains the bash completion for skopeo.

%package fish-completion
Summary:        Fish completion for skopeo
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)

%description fish-completion
This package contains the fish completion for skopeo.

%package zsh-completion
Summary:        Zsh completion for skopeo
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
This package contains the zsh completion for skopeo.

%prep
%autosetup

%build
mkdir -p .gopath/src/github.com/containers
ln -s $PWD .gopath/src/%{project}
export GOPATH=$PWD/.gopath

export BUILDTAGS="exclude_graphdriver_aufs"

# Build.
GO111MODULE=on go build -mod=vendor "-buildmode=pie" -ldflags "-X main.gitCommit=" -gcflags "" -tags "$BUILDTAGS" -o skopeo %{project}/cmd/skopeo
%make_build docs PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} install-docs install-completions
# Drop unneeded files
rm -rv %{buildroot}/etc/containers

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/skopeo*.1*

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
