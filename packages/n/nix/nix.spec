#
# spec file for package nix
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Eyad Issa
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


%global services nix-daemon.socket nix-daemon.service

%bcond_with docs

%if 0%{?suse_version} == 1500
%global force_boost_version 1_75_0
%endif

Name:           nix
Version:        2.33.3
Release:        0
Summary:        The purely functional package manager
License:        LGPL-2.1-only
URL:            https://nixos.org/
Source:         https://github.com/NixOS/nix/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Source1:        nix.conf
Source2:        sysusers.conf
Source9:        series
Patch1:         0001-port-option-to-disable-functional-tests-to-meson.patch
Patch2:         0002-libutil-fix-unreachable-case.patch
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  busybox-static
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  jq
BuildRequires:  libboost_container%{?force_boost_version}-devel
BuildRequires:  libboost_context%{?force_boost_version}-devel
BuildRequires:  libboost_coroutine%{?force_boost_version}-devel
BuildRequires:  libboost_iostreams%{?force_boost_version}-devel
BuildRequires:  libboost_url%{?force_boost_version}-devel
BuildRequires:  libtool
BuildRequires:  lowdown
BuildRequires:  lsof
BuildRequires:  meson
BuildRequires:  perl-DBD-SQLite
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  (pkgconfig(readline) or readline-devel)
BuildRequires:  cmake(toml11)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libblake3)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libcpuid)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2) >= 1.9.0
BuildRequires:  pkgconfig(libseccomp) >= 2.5.5
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(lowdown)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
# Needed by -Dembedded-sandbox-shell
Requires:       busybox-static
Requires:       jq
%{?systemd_ordering}
%{?sysusers_requires}
%if %{with docs}
BuildRequires:  mdbook
BuildRequires:  mdbook-linkcheck
BuildRequires:  rsync
%endif

%description
Nix is a powerful package manager for Linux and other Unix systems
that makes package management reliable and reproducible.
Please refer to the Nix manual for more details.

%package devel
Summary:        The purely functional package manager
Requires:       %{name} = %{version}
Requires:       perl-base

%description devel
Nix is a powerful package manager for Linux and other Unix systems
that makes package management reliable and reproducible.
Please refer to the Nix manual for more details.

This package holds the development files for nix.

%package doc
Summary:        Documentation for the Nix package manager
Requires:       %{name} = %{version}
Supplements:    (%{name} and %{name}-devel)
BuildArch:      noarch

%description doc
Documentation for the Nix package manager.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
Bash command-line completion for the Nix package manager.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion for the Nix package manager.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command-line completion for the Nix package manager.

%prep
%autosetup -p1

%build
echo %{version} > .version

# Warning
# It is best not to change the Nix store from its default, since
# doing so makes it impossible to use pre-built binaries from the
# standard Nixpkgs channels — that is, all packages will need to
# be built from source.
#
# https://nix.dev/manual/nix/2.28/installation/building-source
#
# Nix keeps its store (the place where packages are stored) in
# /nix/store by default. This can be changed using -Dstore-dir=path.

%meson \
    --localstatedir=%{_sharedstatedir}/nix \
    --libdir=%{_libdir}/nix/ \
    -Dunit-tests=false \
    -Dfunctional-tests=disabled \
    -Djson-schema-checks=false \
    -Dkaitai-struct-checks=false \
    -Dlibcmd:readline-flavor=readline \
    -Dlibstore:embedded-sandbox-shell=true \
    -Dlibstore:sandbox-shell=busybox-static \
    -Dlibstore:s3-aws-auth=disabled \
    %{?with_docs:-Ddoc-gen=true} \
    %{nil}

%meson_build

%sysusers_generate_pre %{SOURCE2} %{name} %{name}.conf

%install
%meson_install

mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}

# fix pkgconfig installation location
mv %{buildroot}%{_libdir}/nix/pkgconfig/ %{buildroot}%{_libdir}

# fix perl bindings installation location
install_dir="%{buildroot}%{_prefix}/lib/perl5/vendor_perl"
mkdir -p "$install_dir"
mv %{buildroot}%{_libdir}/nix/perl5/site_perl/* "$install_dir/"
rm -rf %{buildroot}%{_libdir}/nix/perl5

# nix.conf
install -D -m 0644 -t %{buildroot}%{_sysconfdir}/%{name}/ %{SOURCE1}
# sysusers.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

# add nix libdir to ld.so.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/nix/" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/nix.conf

%fdupes %{buildroot}

%check
%meson_test

%pre -f %{name}.pre
%service_add_pre %{services}

%preun
%service_del_preun %{services}

%post
%tmpfiles_create %{_tmpfilesdir}/nix-daemon.conf
%service_add_post %{services}
%{ldconfig}

%postun
%service_del_postun %{services}
%{ldconfig}

%files
%license COPYING
%doc doc/manual/source/release-notes/rl-2.33.md
%doc CONTRIBUTING.md README.md
# config files
%config(noreplace) %{_sysconfdir}/nix/
%config %{_sysconfdir}/profile.d/nix-daemon.fish
%config %{_sysconfdir}/profile.d/nix-daemon.sh
%config %{_sysconfdir}/profile.d/nix.fish
%config %{_sysconfdir}/profile.d/nix.sh
# binaries
%{_bindir}/nix*
# systemd
%{_unitdir}/nix*
%{_tmpfilesdir}/nix-daemon.conf
%{_sysusersdir}/%{name}.conf
# libraries
%{_libexecdir}/nix/
%{_libdir}/nix
%config %{_sysconfdir}/ld.so.conf.d/nix.conf
# custom nix root dir
%ghost %dir %attr(755,root,root) /nix
%ghost %dir %attr(755,root,root) /nix%{_localstatedir}
%ghost %dir %attr(755,root,root) /nix%{_localstatedir}/nix
%ghost %dir %attr(755,root,root) /nix%{_localstatedir}/nix/daemon-socket
%ghost %dir %attr(755,root,root) /nix%{_localstatedir}/nix/builds
# manual
%if %{with docs}
%{_mandir}/man?/nix*
%endif

%if %{with docs}
%files doc
%{_datadir}/doc/nix/
%endif

%files devel
%{_includedir}/nix*.h
%{_includedir}/nix*.hh
%{_includedir}/nix/
%{_includedir}/nix_api_store/
%{_libdir}/pkgconfig/nix*

# perl bindings
%{perl_vendorarch}/Nix
%dir %{perl_vendorarch}/auto
%{perl_vendorarch}/auto/Nix

%files bash-completion
%{_datadir}/bash-completion/completions/nix

%files zsh-completion
%{_datadir}/zsh/site-functions/_nix
%{_datadir}/zsh/site-functions/run-help-nix

%files fish-completion
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/nix.fish

%changelog
