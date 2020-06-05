#
# spec file for package watson
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


%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:           watson
Version:        1.9.0
Release:        0
Summary:        CLI time tracker
License:        MIT
Group:          Productivity/Office/Organizers
URL:            https://github.com/TailorDev/Watson
Source:         https://github.com/TailorDev/Watson/archive/%{version}.tar.gz
Patch0:         watson-arrow-version.patch
BuildRequires:  python3-setuptools
Requires:       python3-arrow
Requires:       python3-click
Requires:       python3-click-didyoumean
Requires:       python3-requests
BuildArch:      noarch

%description
Watson helps managing time. It can tell how much time was spent on projects.
It generates reports for clients.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -n Watson-%{version}

%build
%python3_build

%install
%python3_install
install -D -m 0644 watson.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_watson
mkdir -p %{buildroot}%{_datadir}%{_datadir}/fish/vendor_completions.d/
install -D -m 0644 watson.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/watson.fish
install -D -m 0644 watson.completion  %{buildroot}%{_datadir}/bash-completion/completions/watson

%files
%license LICENSE
%doc CHANGELOG.md README.rst
%{_bindir}/watson
%{python_sitelib}/*

%files bash-completion
%{_datadir}/bash-completion/completions/

%files fish-completion
%dir %{_datadir}/fish/
%{_datadir}/fish/vendor_completions.d/

%files zsh-completion
%dir %{_datadir}/zsh/
%{_datadir}/zsh/site-functions/

%changelog
