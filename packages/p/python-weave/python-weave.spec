#
# spec file for package python-weave
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
%define skip_python3 1
%define oldpython python

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-weave
Version:        0.17.0
Release:        0
Summary:        A C++ compiler for Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://www.github.com/scipy/weave
Source0:        https://files.pythonhosted.org/packages/source/w/weave/weave-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module scipy}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
# Required for the running of the testsuite
BuildRequires:  system-user-nobody
Requires:       python-numpy
Requires:       python-scipy
Provides:       python-weave-devel = %{version}
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-scipy-weave = %{version}
Obsoletes:      %{oldpython}-scipy-weave < %{version}
%endif
%python_subpackages

%description
Weave provides tools for including C/C++ code within Python code. Inlining
C/C++ code within Python generally results in speedups of 1.5x to 30x over
algorithms written in pure Python.

Weave is the stand-alone version of the deprecated Scipy submodule
``scipy.weave``.   It is Python 2.x only, and is provided for users that need
new versions of Scipy (from which the ``weave`` submodule may be removed) but
have existing code that still depends on ``scipy.weave``.  For new code, users
are recommended to use Cython.

%prep
%setup -q -n weave-%{version}
sed -i -e '1d' weave/setup.py

%build
%python_build

%install
%python_install
%{python_expand # Don't ship tests
    rm -rfv %{buildroot}%{$python_sitelib}/weave/tests
    # Deduplicate files
    %fdupes %{buildroot}%{$python_sitelib}
}

%check
export PYTHONPATH=.
%python_exec -c 'import weave; weave.test(verbose=2)'

%files %{python_files}
%license LICENSE.txt
%doc doc/tutorial*
%{python_sitelib}/weave-%{version}-py*.egg-info
%{python_sitelib}/weave
%exclude %{python_sitelib}/weave/LICENSE.txt

%changelog
