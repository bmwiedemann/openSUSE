#
# spec file for package googler
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


Name:           googler
Version:        4.3.13
Release:        0
Summary:        Google Search, Google Site Search, Google News from the terminal
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/oksiquatzel/googler
Source:         https://github.com/oksiquatzel/googler/archive/v%{version}.tar.gz
BuildRequires:  python3-devel >= 3.7
BuildArch:      noarch

%description
googler is a power tool to Google (Web & News) and Google Site Search
from the command-line. It shows the title, URL and abstract for each
result, which can be directly opened in a browser from the terminal.
Results are fetched in pages (with page navigation). Supports
sequential searches in a single googler instance.

%prep
%autosetup

%build
%make_build disable-self-upgrade

%install
make PREFIX=%{buildroot}%{_prefix} install
# Fix the googler.noarch: E: env-script-interpreter (Badness: 9) error by
# rpmlint.
sed -i 's|%{_bindir}/env\ python|%{_bindir}/python|1' %{buildroot}/%{_bindir}/%{name}

# wrong location
rm -rf %{buildroot}%{_datadir}/doc/googler

install -Dm644 auto-completion/fish/googler.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/googler.fish
install -Dm644 auto-completion/bash/googler-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/googler
install -Dm644 auto-completion/zsh/_googler %{buildroot}%{_datadir}/zsh/site-functions/_googler

%files
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/googler
%{_mandir}/man1/googler.*
%{_datadir}/bash-completion/completions/
%dir %{_datadir}/fish/
%{_datadir}/fish/vendor_completions.d/
%{_datadir}/zsh/

%changelog
