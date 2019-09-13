#
# spec file for package python-click-completion
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-click-completion
Version:        0.5.1
Release:        0
Summary:        Fish, Bash, Zsh and PowerShell completion for Click
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/click-contrib/click-completion
Source:         https://github.com/click-contrib/click-completion/archive/v%{version}.tar.gz#/click-completion-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-click
Requires:       python-shellingham
Requires:       python-six
%ifpython2
Requires:       python-enum34
%endif
BuildArch:      noarch
%python_subpackages

%description
Fish, Bash, Zsh and PowerShell completion for Click.

%prep
%setup -q -n click-completion-%{version}
sed -i '1 {/^#!/d}' click_completion/*.py examples/*
chmod a-x examples/*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md examples/
%license LICENSE
%{python_sitelib}/*

%changelog
