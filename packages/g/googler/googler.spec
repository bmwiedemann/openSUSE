#
# spec file for package googler
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


Name:           googler
Version:        4.3.1
Release:        0
Summary:        Google Search, Google Site Search, Google News from the terminal
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/jarun/googler
Source:         https://github.com/jarun/googler/archive/v%{version}.tar.gz
BuildRequires:  python3-devel >= 3.4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
googler is a power tool to Google (Web & News) and Google Site Search
from the command-line. It shows the title, URL and abstract for each
result, which can be directly opened in a browser from the terminal.
Results are fetched in pages (with page navigation). Supports 
sequential searches in a single googler instance.

%prep
%setup -q

%build
make disable-self-upgrade

%install
make PREFIX=%{buildroot}%{_prefix} install
# Fix the googler.noarch: E: env-script-interpreter (Badness: 9) error by
# rpmlint.
sed -i 's|/usr/bin/env\ python|/usr/bin/python|1' %{buildroot}/%{_bindir}/%{name}

# wrong location
rm -rf %{buildroot}%{_datadir}/doc/googler

install -Dm644 auto-completion/fish/googler.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/googler.fish
install -Dm644 auto-completion/bash/googler-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/googler
install -Dm644 auto-completion/zsh/_googler %{buildroot}%{_datadir}/zsh/site-functions/_googler

%files
%defattr(-,root,root)
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/googler
%{_mandir}/man1/googler.*
%{_sysconfdir}/bash_completion.d/
%dir %{_datadir}/fish/
%{_datadir}/fish/vendor_completions.d/
%{_datadir}/zsh/

%changelog
