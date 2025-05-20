#
# spec file for package python-click-completion
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-click-completion
Version:        0.5.2
Release:        0
Summary:        Fish, Bash, Zsh and PowerShell completion for Click
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/click-contrib/click-completion
Source:         https://github.com/click-contrib/click-completion/archive/v%{version}.tar.gz#/click-completion-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-click
Requires:       python-shellingham
Requires:       python-six
BuildArch:      noarch
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
Fish, Bash, Zsh and PowerShell completion for Click.

%prep
%setup -q -n click-completion-%{version}
sed -i '1 {/^#!/d}' click_completion/*.py examples/*
chmod a-x examples/*

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md examples/
%license LICENSE
%{python_sitelib}/click[-_]completion
%{python_sitelib}/click[-_]completion-%{version}*-info

%changelog
