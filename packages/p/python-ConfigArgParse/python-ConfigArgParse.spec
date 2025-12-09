#
# spec file for package python-ConfigArgParse
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


%{?sle15_python_module_pythons}
Name:           python-ConfigArgParse
Version:        1.7.1
Release:        0
Summary:        A drop-in replacement for argparse
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bw2/ConfigArgParse
Source:         https://files.pythonhosted.org/packages/source/c/configargparse/configargparse-%{version}.tar.gz
Patch1:         https://github.com/bw2/ConfigArgParse/pull/295/commits/5e9f442374bc6d9707a43df13aaff684dff6b535.patch#/py313-skip-exit.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
# Old name of the package
Provides:       python-configargparse = %{version}-%{release}
Obsoletes:      python-configargparse < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
ConfigArgParse allows options to also be set via config files and/or environment
variables.

Applications with more than a handful of user-settable options are best configured
through a combination of command line args, config files, hard-coded defaults, and
in some cases, environment variables.

Python’s command line parsing modules such as argparse have very limited support
for config files and environment variables, so this module extends argparse to
add these features

%prep
%autosetup -p1 -n configargparse-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/bw2/ConfigArgParse/issues/146
export COLUMNS=80
%pytest -k 'not (test_main or testGlobalInstances or testGlobalInstances_WithName or testConfigOrEnvValueErrors or testMutuallyExclusiveArgs)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/configargparse*
%{python_sitelib}/[Cc]onfig[Aa]rg[Pp]arse-%{version}*info
%pycache_only %{python_sitelib}/__pycache__

%changelog
