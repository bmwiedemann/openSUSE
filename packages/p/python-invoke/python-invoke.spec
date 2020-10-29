#
# spec file for package python-invoke
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


# broken with pytest-relaxed (same author -- all of this is unmaintained)
%bcond_with test

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-invoke
Version:        1.4.1
Release:        0
Summary:        Pythonic Task Execution
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://www.pyinvoke.org
Source:         https://files.pythonhosted.org/packages/source/i/invoke/invoke-%{version}.tar.gz
Patch0:         0001-Make-test-fallback-to-system-modules-when-vendorized.patch
Patch1:         pytest4.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-fluidity-sm
Requires:       python-lexicon
Requires:       python-pexpect
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module fluidity-sm}
BuildRequires:  %{python_module lexicon}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pexpect}
# pytest < 6.1 to resolve pytest-relaxed constraint
# https://github.com/bitprophet/pytest-relaxed/issues/12
BuildRequires:  %{python_module pytest < 6.1}
BuildRequires:  %{python_module pytest-relaxed}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
Invoke is a Python (2.7 and 3.4+) task execution tool & library, drawing
inspiration from various sources to arrive at a powerful & clean feature set.

%prep
%setup -q -n invoke-%{version}
# Remove bundled libs, import will fallback to system provided libs
rm -fr invoke/vendor/*

%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/inv
%python_clone -a %{buildroot}%{_bindir}/invoke

%if %{with test}
%check
%pytest -s
%endif

%post
%{python_install_alternative inv invoke}

%postun
%python_uninstall_alternative inv

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/inv
%python_alternative %{_bindir}/invoke
%{python_sitelib}/invoke/
%{python_sitelib}/invoke-%{version}-py*

%changelog
