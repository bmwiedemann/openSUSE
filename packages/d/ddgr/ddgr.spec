#
# spec file for package ddgr
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


Name:           ddgr
Version:        2.1
Release:        0
Summary:        DuckDuckGo from the terminal
License:        GPL-3.0-only
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/jarun/ddgr
Source:         https://github.com/jarun/ddgr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       python3
BuildArch:      noarch

%description
A cmdline utility to search DuckDuckGo from the terminal. Similar to googler for Google.

Unlike the web interface, you can specify the number of search results you would like to see per page. It's more convenient than skimming through 30-odd search results per page. The default interface is carefully designed to use minimum space without sacrificing readability.

%prep
%setup -q
sed -i '/README/ d' Makefile
sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ddgr

%build
#not needed

%install
%make_install PREFIX=%{_prefix}
install -Dm 644 auto-completion/bash/ddgr-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%doc CHANGELOG README.md
%license LICENSE
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%changelog
