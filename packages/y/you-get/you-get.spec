#
# spec file for package you-get
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


Name:           you-get
Version:        0.4.1710
Release:        0
Summary:        Dumb downloader that scrapes the web
License:        MIT
URL:            https://you-get.org
Source0:        https://github.com/soimort/you-get/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  zsh
Requires:       ffmpeg
BuildArch:      noarch

%description
You-Get is a command-line utility to download media contents
(videos, audios, images) from the Web, in case there is no other
handy way to do it.

%package        bash-completion
Summary:        Bash completion for %{name}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%package        fish-completion
Summary:        Fish completion for %{name}
Requires:       fish
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       zsh
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%prep
%setup -q
# remove shebang
for f in $(find ./src -name "*.py"); do
   sed '0,/^#!/{//d;}' -i ${f}
done
# fix interpreter
sed -i 's|^#!/usr/bin/env python3|#!%{_bindir}/python3|' you-get

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
install -m0755 you-get %{buildroot}%{_bindir}
%fdupes -s %{buildroot}%{python3_sitelib}
install -Dm644 contrib/completion/you-get-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/you-get
install -Dm644 contrib/completion/you-get.fish %{buildroot}%{_datadir}/fish/completions/you-get.fish
install -Dm644 contrib/completion/_you-get %{buildroot}%{_datadir}/zsh/site-functions/_you-get

%files
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{_bindir}/you-get
%{python3_sitelib}/*

%files bash-completion
%{_datadir}/bash-completion/completions/you-get

%files fish-completion
%{_datadir}/fish/completions/you-get.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_you-get

%changelog
