#
# spec file for package jj-fzf
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


Name:           jj-fzf
Version:        0.33.0
Release:        0
Summary:        Text UI for Jujutsu based on fzf
License:        MPL-2.0
URL:            https://github.com/tim-janik/jj-fzf
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  awk
BuildRequires:  bash >= 5.1.16
BuildRequires:  coreutils
BuildRequires:  fzf
BuildRequires:  jujutsu >= 0.33.0
BuildRequires:  pandoc
BuildRequires:  sed
Requires:       awk
Requires:       bash >= 5.1.16
Requires:       coreutils
Requires:       fzf
Requires:       jujutsu >= 0.33.0
Requires:       sed

# jujutsu is not built for these architectures
ExcludeArch:    i586 s390x armv7hl armv7l armv7l:armv6l:armv5tel armv6hl

%description
JJ-FZF is a text UI for jj based on fzf, implemented as a bash shell script.
The main view centers around jj log, providing previews for the jj diff or jj
obslog of every revision. Several key bindings are available to quickly perform
actions such as squashing, swapping, rebasing, splitting, branching,
committing, abandoning revisions and more. A separate view for the operations
log jj op log enables fast previews of old commit histories or diffs between
operations, making it easy to jj undo any previous operation. The available
hotkeys are displayed onscreen for simple discoverability. The commands and key
bindings can also be displayed with jj-fzf --help and are documented in the
wiki: jj-fzf-help

The jj-fzf script is implemented in bash-5.1, using fzf and jj with git.
Command line tools like sed, grep, gawk are assumed to provide GNU tool
semantics.

%prep
%autosetup -p1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

sed -i 's#env bash#bash#' %{name} preflight.sh ./lib/*

# # scripts in lib directory are copied to libexec
sed -i '/preflight.sh/ s#/preflight.sh$#/../libexec/%{name}/preflight.sh#' %{name}
sed -i '/common.sh/ s#/lib/common.sh#/../libexec/%{name}/common.sh#' %{name}
sed -i '/--preview/ s#/lib/preview.sh#/../libexec/%{name}/preview.sh#g' %{name}

# fix version output in jj-fzf,
# so the version.sh script (which is not working) is
# no longer required
sed -i '/--version/ s|".*"|%{name} %{version}|' %{name}
sed -i "/--version/ s|%{name} %{version}|%{name} %{version} ${BUILD_DATE}|" %{name}

# manpage
pandoc -f markdown+hard_line_breaks+autolink_bare_uris+emoji+lists_without_preceding_blankline-smart -s -p \
        -M date="${BUILD_DATE}" \
        -M footer="jj-fzf-%{version}" \
        -t man doc/jj-fzf.1.md -o doc/jj-fzf.1

sed -i '/exec man/ s/exec man .*$/exec man jj-fzf ;;/g' %{name}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

install -D -d -m 0755 %{buildroot}%{_libexecdir}/%{name}
for file in preflight.sh ./lib/*
do
        install -m 0755 ${file} %{buildroot}%{_libexecdir}/%{name}
done

install -D -d -m 0755 %{buildroot}%{_mandir}/man1/
install -m 0644 doc/jj-fzf.1 %{buildroot}%{_mandir}/man1/

%check
mkdir TEST && cd TEST
jj git init
# version output without leading "v"
%{buildroot}%{_bindir}/%{name} --version
%{buildroot}%{_bindir}/%{name} --version | grep %{version}

%files
%license LICENSE
%doc README.md NEWS.md
%{_bindir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*.sh
%{_mandir}/man1/%{name}*

%changelog
