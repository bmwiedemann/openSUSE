#
# spec file for package git-fzlog
#
# Copyright (c) 2023 SUSE LLC
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


Name:           git-fzlog
Version:        20230630.55521ba
Release:        0
Summary:        Git log and patch viewer and fuzzy searcher
License:        AGPL-3.0-or-later    
URL:            https://github.com/asdil12/git-fzlog
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       git
Requires:       bat
Requires:       fzf

%description
Git log and patch viewer and fuzzy searcher.
This command provides a two column view with the left column containing the list of commits
and the right column showing the currently selected commit.

%prep
%autosetup

%build

%install
install -D -m 0755 ./%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog

