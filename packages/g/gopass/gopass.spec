#
# spec file for package gopass
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


%global user_services gopass-secret-service.service
%bcond_with secret_service

%global make_args PREFIX=%{_prefix} GOPASS_REVISION=v%{version}
Name:           gopass
Version:        1.17.4
Release:        0
%global pkg_version %{version}
Summary:        The slightly more awesome standard unix password manager for teams
License:        MIT
URL:            https://www.gopass.pw/
Source:         https://github.com/gopasspw/gopass/archive/refs/tags/v%{pkg_version}.tar.gz#/%{name}-%{pkg_version}.tar.gz
Source1:        vendor.tar.xz
Source2:        system_config
Source9:        series
Patch0:         do-not-strip.patch
BuildRequires:  fish
BuildRequires:  golang-packaging
BuildRequires:  gpg2
BuildRequires:  pkgconfig
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.22
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(systemd)
Requires:       git-core
%{go_nostrip}
%{systemd_ordering}

%description
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (bash and %{name})
BuildArch:      noarch
Provides:       gopass-completion-bash = %{version}-%{release}
Obsoletes:      gopass-completion-bash < %{version}-%{release}

%description bash-completion
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package holds the shell completion for bash.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (fish and %{name})
BuildArch:      noarch
Provides:       gopass-completion-fish = %{version}-%{release}
Obsoletes:      gopass-completion-fish < %{version}-%{release}

%description fish-completion
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package holds the shell completion for fish.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (zsh and %{name})
BuildArch:      noarch
Provides:       gopass-completion-zsh = %{version}-%{release}
Obsoletes:      gopass-completion-zsh < %{version}-%{release}

%description zsh-completion
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package holds the shell completion for zsh.

%package impersonate-pass
Summary:        Provide %{_bindir}/pass as drop-in replacement
Requires:       %{name} = %{version}
Conflicts:      password-store
BuildArch:      noarch

%description impersonate-pass
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package provides a symlink to make this a drop in replacement for password-store.

%if %{with secret_service}
%package secret-service
Summary:        Freedesktop secret service support for gopass
Requires:       %{name} = %{version}
BuildArch:      noarch

%description secret-service
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package provides the secret service support for gopass.
%endif

%prep
%autosetup -p1 -a1 -n %{name}-%{pkg_version}

%build
%make_build %{make_args}

perl -p -i -e 's|@GOPASS@|%{_bindir}/gopass|g' contrib/secret-service/*

%install
%make_install %{make_args}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/gopass/config
ln -sf gopass %{buildroot}%{_bindir}/pass

%if %{with secret_service}
install -D -m 0644 -t %{buildroot}%{_userunitdir}      contrib/secret-service/gopass-secret-service.service
install -D -m 0644 -t %{buildroot}/usr/share/dbus-1/services/ contrib/secret-service/org.freedesktop.secrets.service

%pre secret-service
%systemd_user_pre %{user_services}

%post secret-service
%systemd_user_post %{user_services}

%preun secret-service
%systemd_user_preun %{user_services}

%postun secret-service
%systemd_user_postun %{user_services}
%endif

%files
%license LICENSE
%doc *.md
%config(noreplace) %{_sysconfdir}/gopass/
%{_bindir}/gopass
%{_mandir}/man1/gopass.1%{?ext_man}

%if %{with secret_service}
%files secret-service
%{_userunitdir}/gopass-secret-service.service
/usr/share/dbus-1/services/org.freedesktop.secrets.service
%endif

%files bash-completion
%license LICENSE
%{_datadir}/bash-completion/completions/gopass

%files fish-completion
%license LICENSE
%{_datadir}/fish/vendor_completions.d/gopass.fish

%files zsh-completion
%license LICENSE
%{_datadir}/zsh/site-functions/_gopass

%files impersonate-pass
%license LICENSE
%{_bindir}/pass

%changelog
