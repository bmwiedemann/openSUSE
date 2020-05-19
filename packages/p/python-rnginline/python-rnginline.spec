#
# spec file for package python-rnginline
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
Name:           python-rnginline
Version:        0.0.2
Release:        0
Summary:        Python libary to flatten multi-file RELAX NG schemas
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/h4l/rnginline
Source:         https://files.pythonhosted.org/packages/source/r/rnginline/rnginline-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docopt
Requires:       python-lxml
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-coverage
Suggests:       python-mock
Suggests:       python-pytest >= 2.6.4
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
The rnginline package is a Python library and command-line tool for
multi-file RELAX NG schemas from arbitary URLs, and flattening them
into a single RELAX NG schema.

%prep
%setup -q -n rnginline-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rnginline
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%post
%python_install_alternative rnginline

%postun
%python_uninstall_alternative rnginline

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%python_alternative %{_bindir}/rnginline
%{python_sitelib}/*

%changelog
