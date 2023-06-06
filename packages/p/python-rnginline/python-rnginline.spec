#
# spec file for package python-rnginline
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without  test
Name:           python-rnginline
Version:        1.0.0
Release:        0
Summary:        Python libary to flatten multi-file RELAX NG schemas
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/h4l/rnginline
Source:         https://files.pythonhosted.org/packages/source/r/rnginline/rnginline-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docopt
Requires:       python-importlib_resources >= 5.12.0
Requires:       python-lxml
Requires:       python-typing_extensions >= 4.5.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-coverage
Suggests:       python-mock
Suggests:       python-pytest >= 2.6.4
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module importlib_resources >= 5.12.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 4.5.0}
%endif
%python_subpackages

%description
The rnginline package is a Python library and command-line tool for
multi-file RELAX NG schemas from arbitary URLs, and flattening them
into a single RELAX NG schema.

%prep
%setup -q -n rnginline-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rnginline
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
pushd rnginline
%pytest
%endif

%post
%python_install_alternative rnginline

%postun
%python_uninstall_alternative rnginline

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/rnginline
%{python_sitelib}/rnginline*

%changelog
