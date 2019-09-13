#
# spec file for package python-buku
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-buku
Version:        4.2.2
Release:        0
Summary:        Command-line bookmark manager
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/jarun/Buku
Source0:        https://files.pythonhosted.org/packages/source/b/buku/buku-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  python-rpm-macros
BuildRequires:  zsh
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4 >= 4.4.1}
BuildRequires:  %{python_module cryptography >= 1.2.3}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.9.1}
BuildRequires:  %{python_module vcrpy}
BuildRequires:  sqlite3
# /SECTION
Requires:       python-base
Requires:       python-beautifulsoup4 >= 4.4.1
Requires:       python-colorama
Requires:       python-cryptography >= 1.2.3
Requires:       python-html5lib >= 1.0.1
Requires:       python-requests >= 2.9.1
Requires:       python-setuptools
Requires:       python-urllib3 >= 1.13.1
Requires:       sqlite3
Recommends:     xsel
BuildArch:      noarch
Provides:       Buku == %{version}
Obsoletes:      Buku < %{version}
%python_subpackages

%description
Bookmark management utility written in Python3 and SQLite3.

With tagging and multiple options to search bookmarks, including
regex and a deep scan mode (particularly for URLs), finding a
bookmark is very easy. Multiple search results can be opened in
the browser at once.

Though a terminal utility, it's possible to add bookmarks to buku
without touching the terminal.
Buku supports revisiting random forgotten bookmarks too.

%package        bash-completion
Summary:        Bash completion for %{name}
Group:          Productivity/Networking/Web/Utilities
Supplements:    packageand(%{name}:bash)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%package        fish-completion
Summary:        Fish completion for %{name}
Group:          Productivity/Networking/Web/Utilities
Supplements:    packageand(%{name}:fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %{name}.

%package        zsh-completion
Summary:        ZSH Completion for %{name}
Group:          Productivity/Networking/Web/Utilities
Supplements:    packageand(%{name}:zsh)
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%prep
%setup -q -n buku-%{version}
# remove shebang
sed -e '1d' -i buku.py

%build
%python_build

%install
%python_install
# we do not have enough dependencies, at least python-flask-api, at time of writing
rm %{buildroot}%{_bindir}/bukuserver
mkdir -pv %{buildroot}%{_mandir}/man1 %{buildroot}%{_datadir}/bash-completion/completions \
          %{buildroot}%{_datadir}/fish/completions %{buildroot}%{_datadir}/zsh/site-functions
install -m0644 buku.1 -t %{buildroot}%{_mandir}/man1
install -m0644 auto-completion/bash/buku-completion.bash -t %{buildroot}%{_datadir}/bash-completion/completions
install -m0644 auto-completion/fish/buku.fish -t %{buildroot}%{_datadir}/fish/completions
install -m0644 auto-completion/zsh/_buku -t %{buildroot}%{_datadir}/zsh/site-functions

%check
# turn off online tests
%pytest -k 'not (test_load_firefox_database or
                 test_network_handler_with_url or
                 test_tnyfy_url or test_refreshdb or
                 test_print_rec_hypothesis or
                 test_add_rec_exec_arg or
                 test_add_rec_exec_arg or
                 test_update_rec_exec_arg or
                 test_search_by_tag_query or
                 test_update_rec_update_all_bookmark)'

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%python3_only %{_bindir}/buku
%python3_only %{_mandir}/man1/buku.1%{ext_man}
%{python_sitelib}/*

%files %{python_files bash-completion}
%{_datadir}/bash-completion/completions/buku-completion.bash

%files %{python_files fish-completion}
%{_datadir}/fish/completions/buku.fish

%files %{python_files zsh-completion}
%{_datadir}/zsh/site-functions/_buku

%changelog
