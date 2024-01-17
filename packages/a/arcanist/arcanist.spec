#
# spec file for package arcanist
#
# Copyright (c) 2022 SUSE LLC
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


Name:           arcanist
Version:        0.0~git.20220517T162014~85c953e
Release:        0
Summary:        Command-line interface to Phabricator
License:        Apache-2.0
URL:            https://secure.phabricator.com/diffusion/ARC/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE remove-arc-upgrade.patch -- Remove workflow/ArcanistUpgradeWorkflow.php
Patch0:         remove-arc-upgrade.patch
# https://secure.phabricator.com/D21746
Patch1:         arcanist-default-error_reporting.patch
BuildRequires:  ca-certificates
BuildRequires:  php8-curl
BuildRequires:  xz
Requires:       ca-certificates
Requires:       php8
Requires:       php8-curl
Recommends:     bash-completion
# /usr/bin/arc binary name conflicts
Conflicts:      arc
Provides:       php7-libphutil = %{version}
Obsoletes:      php7-libphutil < %{version}
BuildArch:      noarch

%description
Arcanist is the command-line tool for Phabricator.
It allows you to interact with Phabricator installs to send code for review,
download patches, transfer files, view status, make API calls, and various other
things.

For more information, visit http://www.phabricator.com/docs/arcanist/

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f scripts/breakout.py
# Remove 'arc upgrade'
rm -f src/workflow/ArcanistUpgradeWorkflow.php

# Remove tests
find src -name __tests__ -type d -print0 | xargs -0 rm -rf

# Generate bash completion
bin/arc shell-complete --generate --

%build

%install
# arcanist
install -d %{buildroot}%{_datadir}/phabricator/%{name}
cp -a bin/ support/ resources/ scripts/ src/ externals/ %{buildroot}%{_datadir}/phabricator/%{name}/

find %{buildroot}%{_datadir}/phabricator/%{name}/bin \
     %{buildroot}%{_datadir}/phabricator/%{name}/scripts -type f | \
    xargs sed -i '1 s|%{_bindir}/env\ php|%{_bindir}/php8|'

find %{buildroot}%{_datadir}/phabricator/%{name}/bin -type f | \
    xargs sed -i '1 s|%{_bindir}/env\ bash|/bin/bash|'

# symlink arc
install -d -m 0755 %{buildroot}%{_bindir}
ln -sf %{_datadir}/phabricator/%{name}/bin/arc %{buildroot}%{_bindir}/arc

# Replace bundled ca-bundle with symlink to system bundle.
rm %{buildroot}%{_datadir}/phabricator/arcanist/resources/ssl/default.pem
ln -s /var/lib/ca-certificates/ca-bundle.pem %{buildroot}%{_datadir}/phabricator/arcanist/resources/ssl/default.pem

# bash completion

install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions
install -m 0644 support/shell/rules/bash-rules.sh %{buildroot}%{_datadir}/bash-completion/completions/arc

%files
%doc NOTICE README.md
%license LICENSE
%{_bindir}/arc
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/arc
%dir %{_datadir}/phabricator
%{_datadir}/phabricator/%{name}

%changelog
