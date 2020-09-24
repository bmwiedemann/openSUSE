#
# spec file for package twups
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


Name:           twups
Version:        git20200908
Release:        0
Summary:	Tumbleweed Update Scrutinizer
License:        GPL-3.0-or-later
URL:            https://codeberg.org/ProgrammerPolymathic/twups
Source:         %{name}-%{version}.tar.gz
Patch0:		install.patch
Requires:       curl
Requires:       tumbleweed-cli

%description
Fetches snapshot scores from Boombatower and can prompt for update based on stability ratings. Searching the snapshot database is also allowed with regex support.

%prep
%setup -q
sed -i -e '/#!\/usr\/bin\/env bash/d' twups-completion.bash
sed -i 's/#!\/usr\/bin\/env bash/#!\/usr\/bin\/bash/g' twups
%patch0 -p0

%build

%install
%make_install

%files
%license COPYING
%{_bindir}/twups
%{_mandir}/man1/twups.1.gz
%dir %{_datadir}/bash_completion
%dir %{_datadir}/bash_completion/completions
%{_datadir}/bash_completion/completions/twups-completion.bash


%changelog

