#
# spec file for package linode-cli
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cli_name    linode-cli
%bcond_without python2

Name:           linode-cli
Version:        5.25.0
Release:        0
Summary:        The Linode command-line interface
License:        BSD-3-Clause
URL:            https://github.com/linode/linode-cli
Source:         https://github.com/linode/linode-cli/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        openapi.yaml
# PATCH-FIX-OPENSUSE 0001-Remove-shebang-from-non-executable-files.patch
Patch0:         0001-Remove-shebang-from-non-executable-files.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module terminaltables}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python-enum34
BuildRequires:  python2-future
%endif
Requires:       python-PyYAML
Requires:       python-requests
Requires:       python-terminaltables
%ifpython2
Requires:       python-enum34
Requires:       python2-future
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The Linode Command Line interface

%package -n %{name}-bash-completion
Summary:        Bash completion for linode-cli
Group:          System/Shells
Supplements:    %{python_module linode-cli and bash-completion}
BuildArch:      noarch

%description -n %{name}-bash-completion

Bash completion files for %{name}

%prep
%autosetup -p1

%build
# harcode version to prevent calling out to git during build
echo "#!/bin/sh
echo %version" > version

# bake data files, output with different name based on the python version
%python_exec -m linodecli bake "%{SOURCE1}" --skip-config
cp data-* linodecli/

# run the actual build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/%{cli_name}

# move installed bash completions to proper location
install -d %{buildroot}%{_datarootdir}/bash-completion/completions
mv %{buildroot}%{python_sitelib}%{_sysconfdir}/bash_completion.d/%{cli_name}.sh  %{buildroot}%{_datarootdir}/bash-completion/completions/%{cli_name}
%python_expand rm -r %{buildroot}%{$python_sitelib}%{_sysconfdir}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative %{cli_name}

%postun
%python_uninstall_alternative %{cli_name}

%files %{python_files}
%python_alternative %{_bindir}/%{cli_name}
%{python_sitelib}/linodecli
%{python_sitelib}/linode_cli-%{version}.dist-info

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{cli_name}

%changelog
