#
# spec file for package watson
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define pythons %{primary_python}
Name:           watson
Version:        3.0.1
Release:        0
Summary:        CLI time tracker
License:        MIT
URL:            https://github.com/jmaupetit/Watson
Source:         https://github.com/jmaupetit/Watson/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module arrow >= 1.4.0}
BuildRequires:  %{python_module click >= 8.3.1}
BuildRequires:  %{python_module click-didyoumean >= 0.3.1}
BuildRequires:  %{python_module colorama >= 0.4.6}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-datafiles}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.32.5}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}-arrow >= 1.4.0
Requires:       %{primary_python}-click >= 8.3.1
Requires:       %{primary_python}-click-didyoumean >= 0.3.1
Requires:       %{primary_python}-colorama >= 0.4.6
Requires:       %{primary_python}-requests >= 2.32.5
BuildArch:      noarch

%description
Watson helps managing time. It can tell how much time was spent on projects.
It generates reports for clients.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -p1 -n Watson-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/watson
install -D -m 0644 watson.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_watson
install -D -m 0644 watson.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/watson.fish
install -D -m 0644 watson.completion %{buildroot}%{_datadir}/bash-completion/completions/watson
%fdupes %{buildroot}%{python_sitelib}

%check
%pytest

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/watson
%{python_sitelib}/watson
%{python_sitelib}/td_watson-%{version}.dist-info

%files bash-completion
%{_datadir}/bash-completion/completions/watson

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/watson.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_watson

%changelog
