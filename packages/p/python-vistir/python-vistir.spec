#
# spec file for package python-vistir
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


Name:           python-vistir
Version:        0.8.0
Release:        0
Summary:        Utilities for filesystems, paths, projects, subprocesses, and more
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/vistir
Source:         https://github.com/sarugaku/vistir/archive/refs/tags/v%{version}.tar.gz#/vistir-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama >= 0.3.4
Recommends:     python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module colorama >= 0.3.4}
BuildRequires:  %{python_module hypothesis-fspaths}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Miscellaneous utilities for dealing with filesystems, paths, projects,
subprocesses, and more.

%prep
%setup -q -n vistir-%{version}

sed -i '/invoke/d;/parver/d;/wheel$/d;/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8

# test_open_file_without_requests requires network access
# test_path_to_url needs bigger seed than some of our virtuals provide
# test_ensure_mkdir_p race condition
# test_mkdir_p very slow on Leap Python 2
# test_decode_encode and test_run_failing_subprocess fails on Leap 15.2 Python 2
%{python_expand skip_tests="test_open_file_without_requests"
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m pytest -v -k "not ($skip_tests)"
}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/vistir
%{python_sitelib}/vistir-%{version}*-info

%changelog
