#
# spec file for package python-coloredlogs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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
Name:           python-coloredlogs
Version:        10.0
Release:        0
Summary:        Colored terminal output for Python's logging module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/xolox/python-coloredlogs
Source:         https://files.pythonhosted.org/packages/source/c/coloredlogs/coloredlogs-%{version}.tar.gz
# PATCH-FIX-OPENSUSE test_cli_conversion_test.patch mcepl@suse.com
# With using alternatives, we don't have versionless command in time of %check
Patch0:         test_cli_conversion_test.patch
BuildRequires:  %{python_module capturer >= 2.4}
BuildRequires:  %{python_module humanfriendly >= 3.2}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module pytest >= 3.0.3}
BuildRequires:  %{python_module pytest-cov >= 2.3.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module verboselogs >= 1.7}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-capturer >= 2.4
Requires:       python-humanfriendly >= 3.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-verboselogs >= 1.7
BuildArch:      noarch
%python_subpackages

%description
The `coloredlogs` package enables colored terminal output for Python's logging_
module. The ColoredFormatter_ class inherits from `logging.Formatter`_ and uses
`ANSI escape sequences`_ to render your logging messages in color. It uses only
standard colors so it should work on any UNIX terminal. It's currently tested
on Python 2.6, 2.7, 3.4, 3.5 and PyPy. On Windows `coloredlogs` automatically
pulls in Colorama_ as a dependency and enables ANSI escape sequence translation
using Colorama.

%prep
%setup -q -n coloredlogs-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/coloredlogs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative coloredlogs

%postun
%python_uninstall_alternative coloredlogs

%check
# test_auto_install - requires the install to the system to be actually complete
# test_plain_text_output_format - random hickupy test
export PATH=%{buildroot}%{_bindir}:$PATH
%pytest coloredlogs/tests.py -k 'not (test_auto_install or test_plain_text_output_format)'

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.txt
%python_alternative %{_bindir}/coloredlogs
%{python_sitelib}/coloredlogs/
%{python_sitelib}/coloredlogs.pth
%{python_sitelib}/coloredlogs-%{version}-py*.egg-info

%changelog
