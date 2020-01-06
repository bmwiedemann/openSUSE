#
# spec file for package python-vistir
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
Name:           python-vistir
Version:        0.4.3
Release:        0
Summary:        Utilities for filesystems, paths, projects, subprocesses, and more
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/vistir
Source:         https://github.com/sarugaku/vistir/archive/%{version}.tar.gz#/vistir-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://github.com/sarugaku/vistir/issues/65
Patch0:         fix-test_Account-for-encoded-length.patch
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama >= 0.3.4
Requires:       python-requests
Requires:       python-six
Recommends:     python-yaspin
BuildArch:      noarch
%ifpython2
Requires:       python2-backports.functools_lru_cache
Requires:       python2-backports.shutil_get_terminal_size
Requires:       python2-backports.weakref
Requires:       python2-pathlib2
%endif
# SECTION test requirements
BuildRequires:  %{python_module colorama >= 0.3.4}
BuildRequires:  %{python_module hypothesis-fspaths}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module yaspin}
BuildRequires:  python2-backports.functools_lru_cache
BuildRequires:  python2-backports.shutil_get_terminal_size
BuildRequires:  python2-backports.weakref
BuildRequires:  python2-pathlib2
# /SECTION
%python_subpackages

%description
Miscellaneous utilities for dealing with filesystems, paths, projects,
subprocesses, and more.

%prep
%setup -q -n vistir-%{version}
%patch0 -p1

sed -i '/invoke/d;/parver/d;/wheel$/d;/addopts/d' setup.cfg
rm -r tasks

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# test_open_file requires network access
# test_path_to_url needs bigger seed than some of our virtuals provide
# test_ensure_mkdir_p race condition
%pytest -k 'not (test_open_file or test_path_to_url or test_ensure_mkdir_p)'

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
