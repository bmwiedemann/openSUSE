#
# spec file for package python-pywbemtools
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-pywbemtools
Version:        1.3.0
Release:        0
Summary:        Python client tools to work with WBEM Servers using the PyWBEM API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pywbem/pywbemtools
# The PyPI archive does not contain the tests
Source:         https://github.com/pywbem/pywbemtools/archive/%{version}.tar.gz#/pywbemtools-%{version}-gh.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.3.1
Requires:       python-asciitree >= 0.3.3
Requires:       python-click >= 8.0.2
Requires:       python-click-repl >= 0.2
Requires:       python-nocasedict >= 1.0.1
Requires:       python-nocaselist >= 1.0.3
Requires:       python-packaging >= 21.0
Requires:       python-prompt_toolkit >= 3.0.13
Requires:       python-pyparsing >= 2.3.1
Requires:       python-pywbem >= 1.7.2
Requires:       python-toposort >= 1.6
Requires:       python-urllib3 >= 1.26.18
Requires:       python-yamlloader >= 0.5.5
Requires:       (python-click-spinner >= 0.1.8 if python-base < 3.12 else python-click-spinner >= 0.1.10)
Requires:       (python-psutil >= 5.5.0 if python-base < 3.10 else python-psutil >= 5.8.0)
Requires:       (python-six >= 1.14.0 if python-base < 3.10 else python-six >= 1.16.0)
Requires:       (python-tabulate >= 0.8.2 if python-base < 3.10 else python-tabulate >= 0.8.8)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if !%{with test}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
%else
BuildRequires:  %{python_module pytest}
# tests require entrypoint in standard path
BuildRequires:  %{python_module pywbemtools = %{version}}
%endif
%python_subpackages

%description
Pywbemtools is a collection of command line tools that communicate with WBEM
servers. The tools are written in pure Python and support Python 2 and Python
3.

At this point, pywbemtools includes a single command line tool named
pywbemcli that uses the python-pywbem package to issue operations to a
WBEM server using the CIM/WBEM standards defined by the DMTF to perform
system management tasks.

%prep
%autosetup -p1 -n pywbemtools-%{version}
# remove old mock
sed -i '/mock/ d' requirements.txt
sed -i 's/from mock import/from unittest.mock import/' tests/unit/pywbemcli/*.py
sed -i 's/^import mock/from unittest import mock/' tests/unit/test_utils.py pywbemtools/_utils.py

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pywbemcli
%python_clone -a %{buildroot}%{_bindir}/pywbemlistener
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%else

%check
# increase virtual terminal size to avoid unexpected line breaks
export PYWBEMTOOLS_TERMWIDTH=120
# too many cli tests not compatible with click-repl 0.3: https://github.com/pywbem/pywbemtools/issues/1312
donttest="pywbemcli"
%pytest tests/unit -s -k "not ($donttest)"
%endif

%if !%{with test}
%post
%python_install_alternative pywbemcli pywbemlistener

%postun
%python_uninstall_alternative pywbemcli

%files %{python_files}
%python_alternative %{_bindir}/pywbemcli
%python_alternative %{_bindir}/pywbemlistener
%{python_sitelib}/pywbemtools
%{python_sitelib}/pywbemtools-%{version}.dist-info
%endif

%changelog
