#
# spec file for package git-annex
#
# Copyright (c) 2020 SUSE LLC
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
Version:        8.20201007
Release:        0
Summary:        Manage files with git, without checking their contents into git
License:        AGPL-3.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND MIT AND GPL-2.0-only
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://github.com/peti/git-annex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  chrpath
BuildRequires:  curl
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-DAV-devel
BuildRequires:  ghc-IfElse-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-SafeSemaphore-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-aws-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bloomfilter-devel
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-clientsession-devel
BuildRequires:  ghc-concurrent-output-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-connection-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-dbus-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-disk-free-space-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-fdo-notify-devel
BuildRequires:  ghc-feed-devel
BuildRequires:  ghc-filepath-bytestring-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-git-lfs-devel
BuildRequires:  ghc-hinotify-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-restricted-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-magic-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-mountpoints-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-bsd-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-info-devel
BuildRequires:  ghc-network-multicast-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-path-pieces-devel
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-sqlite-devel
BuildRequires:  ghc-persistent-template-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-sandi-devel
BuildRequires:  ghc-securemem-devel
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-socks-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-stm-chans-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-rerun-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-torrent-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-uuid-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-tls-devel
BuildRequires:  ghc-yesod-core-devel
BuildRequires:  ghc-yesod-devel
BuildRequires:  ghc-yesod-form-devel
BuildRequires:  ghc-yesod-static-devel
BuildRequires:  git-core
BuildRequires:  gpg2
BuildRequires:  lsof
BuildRequires:  rsync
Requires:       git-core
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

%description
Git-annex allows managing files with git, without checking the file contents
into git. While that may seem paradoxical, it is useful when dealing with files
larger than git can currently easily handle, whether due to limitations in
memory, time, or disk space.

It can store large files in many places, from local hard drives, to a large
number of cloud storage services, including S3, WebDAV, and rsync, with a dozen
cloud storage providers usable via plugins. Files can be stored encrypted with
gpg, so that the cloud storage provider cannot see your data.
git-annex keeps track of where each file is stored, so it knows how many copies
are available, and has many facilities to ensure your data is preserved.

git-annex can also be used to keep a folder in sync between computers, noticing
when files are changed, and automatically committing them to git and
transferring them to other computers. The git-annex webapp makes it easy to set
up and use git-annex this way.

%package bash-completion
Summary:        Bash completion for git-annex
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Optional dependency offering bash completion for git-annex

%prep
%autosetup

%build
%define cabal_configure_options -ftestsuite
%ghc_bin_build

%check
%make_build DESTDIR=%{buildroot} BUILDER=./Setup test

%install
%ghc_bin_install
make DESTDIR=%{buildroot} BUILDER=./Setup install-mans install-completions install-desktop
rm %{buildroot}%{_datadir}/fish/vendor_completions.d/git-annex.fish
rm %{buildroot}%{_datadir}/zsh/site-functions/_git-annex

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYRIGHT
%doc CHANGELOG NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}-shell
%{_bindir}/git-remote-tor-annex
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_sysconfdir}/xdg/autostart/git-annex.desktop
%{_mandir}/man1/git-annex*.1%{?ext_man}
%{_mandir}/man1/git-remote-tor-annex.1%{?ext_man}
%{_datadir}/applications/git-annex.desktop
%{_datadir}/icons/hicolor/16x16/apps/git-annex.png
%{_datadir}/icons/hicolor/scalable/apps/git-annex.svg

%files bash-completion
%{_datadir}/bash-completion/completions/git-annex

%changelog
