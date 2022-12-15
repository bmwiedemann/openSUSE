#
# spec file for package python-watchdog
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-watchdog
Version:        2.2.0
Release:        0
Summary:        Filesystem events monitoring
License:        Apache-2.0
URL:            https://github.com/gorakhargosh/watchdog
Source:         https://files.pythonhosted.org/packages/source/w/watchdog/watchdog-%{version}.tar.gz
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-PyYAML >= 3.10
Requires:       python-pathtools >= 0.1.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pathtools >= 0.1.1}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION test
%python_subpackages

%description
Python API and shell utilities to monitor file system events.

%package doc
Summary:        Documentation and examples for %{name}

%description doc
This package contains documentation and examples for %{name}.

%prep
%setup -q -n watchdog-%{version}
chmod -x README.rst
# Remove all shebangs
find src -name "*.py" | xargs sed -i -e '/^#!\//, 1d'

%build
%python_build
cd docs && make html && rm -r build/html/.buildinfo build/html/objects.inv # Build HTML docs

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/watchmedo
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i '/--cov/d' setup.cfg
export LANG=en_US.UTF-8
# test_event_dispatcher randomly fails on SLE15
# test_unmount_watched_directory_filesystem requires sudo/root which is not available
%pytest -k 'not test_event_dispatcher and not test_unmount_watched_directory_filesystem'

%post
%python_install_alternative watchmedo

%postun
%python_uninstall_alternative watchmedo

%files %{python_files}
%license COPYING LICENSE
%doc AUTHORS changelog.rst MANIFEST.in README.rst
%python_alternative %{_bindir}/watchmedo
%{python_sitelib}/watchdog
%{python_sitelib}/watchdog-%{version}-py%{python_version}.egg-info

%files %{python_files doc}
%doc docs/build/html

%changelog
