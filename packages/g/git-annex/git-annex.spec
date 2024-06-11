#
# spec file for package git-annex
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


Name:           git-annex
Version:        10.20240531
Release:        0
Summary:        Manage files with git, without checking their contents into git
License:        AGPL-3.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND MIT AND GPL-2.0-only
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://github.com/opensuse-haskell/git-annex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-persistent-2.12.0.1-include-the-code-from-persistent.patch
BuildRequires:  bash-completion
BuildRequires:  chrpath
BuildRequires:  curl
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-DAV-devel
BuildRequires:  ghc-DAV-prof
BuildRequires:  ghc-IfElse-devel
BuildRequires:  ghc-IfElse-prof
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-SafeSemaphore-devel
BuildRequires:  ghc-SafeSemaphore-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-aws-devel
BuildRequires:  ghc-aws-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bloomfilter-devel
BuildRequires:  ghc-bloomfilter-prof
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-byteable-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-clientsession-devel
BuildRequires:  ghc-clientsession-prof
BuildRequires:  ghc-concurrent-output-devel
BuildRequires:  ghc-concurrent-output-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-criterion-devel
BuildRequires:  ghc-criterion-prof
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-crypto-api-prof
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-dbus-devel
BuildRequires:  ghc-dbus-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-disk-free-space-devel
BuildRequires:  ghc-disk-free-space-prof
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-edit-distance-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-fdo-notify-devel
BuildRequires:  ghc-fdo-notify-prof
BuildRequires:  ghc-feed-devel
BuildRequires:  ghc-feed-prof
BuildRequires:  ghc-filepath-bytestring-devel
BuildRequires:  ghc-filepath-bytestring-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-free-prof
BuildRequires:  ghc-git-lfs-devel
BuildRequires:  ghc-git-lfs-prof
BuildRequires:  ghc-hinotify-devel
BuildRequires:  ghc-hinotify-prof
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-restricted-devel
BuildRequires:  ghc-http-client-restricted-prof
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-conduit-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-magic-devel
BuildRequires:  ghc-magic-prof
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-mountpoints-devel
BuildRequires:  ghc-mountpoints-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-bsd-devel
BuildRequires:  ghc-network-bsd-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-info-devel
BuildRequires:  ghc-network-info-prof
BuildRequires:  ghc-network-multicast-devel
BuildRequires:  ghc-network-multicast-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-path-pieces-devel
BuildRequires:  ghc-path-pieces-prof
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-prof
BuildRequires:  ghc-persistent-sqlite-devel
BuildRequires:  ghc-persistent-sqlite-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-sandi-devel
BuildRequires:  ghc-sandi-prof
BuildRequires:  ghc-securemem-devel
BuildRequires:  ghc-securemem-prof
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-shakespeare-prof
BuildRequires:  ghc-socks-devel
BuildRequires:  ghc-socks-prof
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-stm-chans-devel
BuildRequires:  ghc-stm-chans-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-tagsoup-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
BuildRequires:  ghc-tasty-rerun-devel
BuildRequires:  ghc-tasty-rerun-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-torrent-devel
BuildRequires:  ghc-torrent-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unbounded-delays-devel
BuildRequires:  ghc-unbounded-delays-prof
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unliftio-core-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-uuid-devel
BuildRequires:  ghc-uuid-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-warp-tls-devel
BuildRequires:  ghc-warp-tls-prof
BuildRequires:  ghc-yesod-core-devel
BuildRequires:  ghc-yesod-core-prof
BuildRequires:  ghc-yesod-devel
BuildRequires:  ghc-yesod-form-devel
BuildRequires:  ghc-yesod-form-prof
BuildRequires:  ghc-yesod-prof
BuildRequires:  ghc-yesod-static-devel
BuildRequires:  ghc-yesod-static-prof
BuildRequires:  git-core
BuildRequires:  gpg2
BuildRequires:  lsof
BuildRequires:  rsync
Requires(post): desktop-file-utils
Requires(post): hicolor-icon-theme
Requires(postun): desktop-file-utils
Requires(postun): hicolor-icon-theme
Recommends:     curl
Recommends:     gpg2
Recommends:     lsof
Recommends:     rsync
Recommends:     ssh
Suggests:       %{name}-bash-completion
ExcludeArch:    %{ix86}

%description
Git-annex allows managing files with git, without checking the file contents
into git. While that may seem paradoxical, it is useful when dealing with files
larger than git can currently easily handle, whether due to limitations in
memory, time, or disk space.

It can store large files in many places, from local hard drives, to a large
number of cloud storage services, including S3, WebDAV, and rsync, and many
other usable via plugins. Files can be stored encrypted with gpg, so that the
cloud storage provider cannot see your data. git-annex keeps track of where
each file is stored, so it knows how many copies are available, and has many
facilities to ensure your data is preserved.

git-annex can also be used to keep a folder in sync between computers, noticing
when files are changed, and automatically committing them to git and
transferring them to other computers. The git-annex webapp makes it easy to set
up and use git-annex this way.

%package bash-completion
Summary:        Bash completion for git-annex
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Optional dependency offering bash completion for git-annex

%prep
%autosetup -p1

%build
%define cabal_configure_options -ftestsuite
%ghc_bin_build

%check
%make_build DESTDIR=%{buildroot} BUILDER=./Setup test

%install
%ghc_bin_install
make DESTDIR=%{buildroot} BUILDER=./Setup install-bins install-mans install-completions install-desktop
rm %{buildroot}%{_datadir}/fish/vendor_completions.d/git-annex.fish
rm %{buildroot}%{_datadir}/zsh/site-functions/_git-annex

%files
%license COPYRIGHT
%doc CHANGELOG NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}-shell
%{_bindir}/git-remote-tor-annex
%{_bindir}/git-remote-annex
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_sysconfdir}/xdg/autostart/git-annex.desktop
%{_mandir}/man1/git-annex*.1%{?ext_man}
%{_mandir}/man1/git-remote-tor-annex.1%{?ext_man}
%{_mandir}/man1/git-remote-annex.1%{?ext_man}
%{_datadir}/applications/git-annex.desktop
%{_datadir}/icons/hicolor/16x16/apps/git-annex.png
%{_datadir}/icons/hicolor/scalable/apps/git-annex.svg

%files bash-completion
%{_datadir}/bash-completion/completions/git-annex

%changelog
