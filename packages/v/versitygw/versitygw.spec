#
# spec file for package versitygw
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


Name:           versitygw
Version:        1.5.0
Release:        0
Summary:        High-Performance S3 Translation Service
License:        Apache-2.0
URL:            https://github.com/versity/versitygw
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source21:       system-user-%{name}.conf
BuildRequires:  golang(API) >= 1.25
BuildRequires:  sysuser-tools
# shell completions
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
#
Requires:       %{name}-cli = %{version}

%description
The Versity S3 Gateway: a High-Performance S3 Translation Service

Use Cases
- Turn your local filesystem into an S3 server with a single command!
- Proxy S3 requests to S3 storage
- Simple to deploy S3 server with a single command
- Protocol compatibility in posix allows common access to files via posix or S3
- Simplified interface for adding new storage system support

%package -n %{name}-cli
Summary:        Binary for %{name}, usable to connect to remote instances

%description -n %{name}-cli
This package only installs the %{name} binary to be able to connect to remote
VersityGW instances.

%package -n %{name}-cli-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
BuildArch:      noarch
Requires:       %{name}-cli = %{version}
Requires:       bash-completion
Supplements:    (%{name}-cli and bash-completion)
Obsoletes:      %{name}-bash-completion
Provides:       %{name}-bash-completion = %{version}

%description -n %{name}-cli-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-cli-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
BuildArch:      noarch
Requires:       %{name}-cli = %{version}
Requires:       fish
Supplements:    (%{name}-cli and fish)
Obsoletes:      %{name}-fish-completion
Provides:       %{name}-fish-completion  = %{version}

%description -n %{name}-cli-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-cli-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
BuildArch:      noarch
Requires:       %{name}-cli = %{version}
Requires:       zsh
Supplements:    (%{name}-cli and zsh)
Obsoletes:      %{name}-zsh-completion
Provides:       %{name}-zsh-completion  = %{version}

%description -n %{name}-cli-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1

%build
# hash will be shortened by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.Version=%{version} \
   -X main.Build=${COMMIT_HASH:0:8} \
   -X main.BuildTime=${BUILD_DATE}" \
   -o bin/%{name} ./cmd/%{name}

# system-user
%sysusers_generate_pre %{SOURCE21} user

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# server systemd unit file
install -D -m 0644 extra/%{name}@.service %{buildroot}%{_unitdir}/%{name}@.service
sed -i 's#WorkingDirectory=.*$#WorkingDirectory=/var/lib/versitygw/#' %{buildroot}%{_unitdir}/%{name}@.service
sed -i 's#User=.*$#User=versitygw#' %{buildroot}%{_unitdir}/%{name}@.service
sed -i 's#Group=.*$#Group=versitygw#' %{buildroot}%{_unitdir}/%{name}@.service

# configuration directory in /etc/versitygw.d/
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}.d/

# directory in /var/lib/
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}

# system user
install -Dm644 %{SOURCE21} %{buildroot}%{_sysusersdir}/system-user-%{name}.conf

# Copy the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
install -Dm644 extra/versitygw.sh %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# Copy the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
install -Dm644 extra/versitygw.fish %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# Copy the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
install -Dm644 extra/versitygw.zsh %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%check
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

bin/%{name} --version | grep %{version}
bin/%{name} --version | grep ${COMMIT_HASH:0:8}

%pre -f user.pre
%service_add_pre %{name}@.service

%post
%service_add_post %{name}@.service

%preun
%service_del_preun %{name}@.service

%postun
%service_del_postun %{name}@.service

%files
%doc README.md extra/example.conf
%license LICENSE
%{_unitdir}/%{name}@.service
%{_sysusersdir}/system-user-%{name}.conf
%dir %attr(755,root, %{name}) %{_sysconfdir}/%{name}.d/
%dir %attr(750,%{name}, %{name}) %{_sharedstatedir}/%{name}/

%files -n %{name}-cli
%{_bindir}/%{name}

%files -n %{name}-cli-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-cli-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-cli-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
