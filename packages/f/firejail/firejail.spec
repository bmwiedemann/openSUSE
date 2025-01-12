#
# spec file for package firejail
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


Name:           firejail
Version:        0.9.72
Release:        0
Summary:        Linux namepaces sandbox program
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://firejail.wordpress.com
Source0:        https://github.com/netblue30/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/netblue30/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
# https://firejail.wordpress.com/download-2/
Source2:        %{name}.keyring
Source3:        %{name}-group.conf
BuildRequires:  apparmor-rpm-macros
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libapparmor-devel
BuildRequires:  sysuser-tools
BuildRequires:  xz
Requires(post): permissions
%sysusers_requires

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces and seccomp-bpf. It includes sandbox profiles for
many existing applications like Iceweasel/Mozilla Firefox and Chromium.

Firejail also expands the restricted shell facility found in bash by adding
Linux namespace support. It supports sandboxing specific users upon login.

%package bash-completion
Summary:        Firejail Bash completion
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Optional dependency offering bash completion for firejail

%package zsh-completion
Summary:        Firejail zsh completion
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Optional dependency offering zsh completion for firejail

%prep
%autosetup
sed -i '1s/^#!\/usr\/bin\/env /#!\/usr\/bin\//' contrib/fj-mkdeb.py contrib/fjclip.py contrib/fjdisplay.py contrib/fjresize.py contrib/sort.py contrib/fix_private-bin.py contrib/jail_prober.py

%build
%sysusers_generate_pre %{SOURCE3} %{name} %{name}-group.conf
%configure --docdir=%{_docdir}/%{name} \
	   --enable-apparmor
%make_build

%install
%make_install
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}-group.conf
rm %{buildroot}%{_docdir}/firejail/COPYING
%fdupes -s %{buildroot}

%pre -f %{name}.pre

%post
%set_permissions %{_bindir}/firejail
%apparmor_reload %{_sysconfdir}/apparmor.d/firejail-default

%verifyscript
%verify_permissions -e %{_bindir}/firejail

%files
%license COPYING
%attr(4750,root,firejail) %verify(not user group mode) %{_bindir}/firejail
%{_bindir}/firecfg
%{_bindir}/firemon
%{_bindir}/jailcheck
%{_libdir}/%{name}
%doc %{_docdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*
%config %{_sysconfdir}/apparmor.d/firejail-default
%config %{_sysconfdir}/apparmor.d/local/firejail-default
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/local
%dir %{_sysconfdir}/apparmor.d/abstractions
%dir %{_sysconfdir}/apparmor.d/abstractions/base.d
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/ftdetect/firejail.vim
%{_datadir}/vim/vimfiles/syntax/firejail.vim
%dir %{_datadir}/gtksourceview-5
%dir %{_datadir}/gtksourceview-5/language-specs
%{_datadir}/gtksourceview-5/language-specs/firejail-profile.lang
%config /etc/apparmor.d/abstractions/base.d/firejail-base
%{_sysusersdir}/%{name}-group.conf

%files bash-completion
%license COPYING
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*

%files zsh-completion
%license COPYING
%dir %{_datarootdir}/zsh
%dir %{_datarootdir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_firejail

%changelog
