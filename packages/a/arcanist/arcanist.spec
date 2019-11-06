#
# spec file for package arcanist
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.0~git.20190905T053100~3cdfe1ff
Release:        0
Summary:        Command-line interface to Phabricator
License:        Apache-2.0

Url:            https://secure.phabricator.com/diffusion/ARC/
Source0:        %{name}-%{version}.tar.xz
Patch0:         remove-arc-upgrade.patch

BuildArch:      noarch
BuildRequires:  php7-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       php7
Requires:       php7-curl
Requires:       php7-json
Requires:       php7-libphutil

Recommends:     bash-completion

# /usr/bin/arc binary name conflicts
Conflicts:      arc

%description
Arcanist is the command-line tool for Phabricator.
It allows you to interact with Phabricator installs to send code for review,
download patches, transfer files, view status, make API calls, and various other
things.

For more information, visit http://www.phabricator.com/docs/arcanist/

%prep
%setup -q
%patch0 -p1

rm -f scripts/breakout.py
# Remove 'arg upgrade'
rm -f src/workflow/ArcanistUpgradeWorkflow.php

# Remove tests
find src -name __tests__ -type d -print0 | xargs -0 rm -rf

%build

%install
# arcanist
install -d %{buildroot}%{_datadir}/phabricator/%{name}
cp -a bin/ resources/ scripts/ src/ %{buildroot}%{_datadir}/phabricator/%{name}/

find %{buildroot}%{_datadir}/phabricator/%{name}/bin \
     %{buildroot}%{_datadir}/phabricator/%{name}/scripts -type f | \
    xargs sed -i '1 s|/usr/bin/env\ php|/usr/bin/php7|'

find %{buildroot}%{_datadir}/phabricator/%{name}/bin -type f | \
    xargs sed -i '1 s|/usr/bin/env\ bash|/bin/bash|'

# symlink arc
install -d -m 0755 %{buildroot}%{_bindir}
ln -sf %{_datadir}/phabricator/%{name}/bin/arc %{buildroot}%{_bindir}/arc

# bash completition
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions
install -m 0644 resources/shell/bash-completion %{buildroot}%{_datadir}/bash-completion/completions/arc

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README.md
%{_bindir}/arc
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/arc
%dir %{_datadir}/phabricator
%{_datadir}/phabricator/%{name}

%changelog
