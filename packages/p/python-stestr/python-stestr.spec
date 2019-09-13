#
# spec file for package python-stestr
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-stestr
Version:        2.4.0
Release:        0
Summary:        A test runner runner similar to testrepository
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mtreinish/stestr
Source:         https://files.pythonhosted.org/packages/source/s/stestr/stestr-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.10.0}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module cliff >= 2.8.0}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module ddt >= 1.0.1}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module mock >= 2.0}
BuildRequires:  %{python_module pbr >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-subunit >= 1.3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module testtools >= 2.2.0}
BuildRequires:  %{python_module voluptuous >= 0.8.9}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dbm
Requires:       python-PyYAML >= 3.10.0
Requires:       python-cliff >= 2.8.0
Requires:       python-fixtures >= 3.0.0
Requires:       python-future
Requires:       python-pbr >= 2.0.0
Requires:       python-python-subunit >= 1.3.0
Requires:       python-six >= 1.10.0
Requires:       python-testtools >= 2.2.0
Requires:       python-voluptuous >= 0.8.9
%ifpython3
Requires:       python-dbm
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if !0%{?_no_weakdeps}
Recommends:     python-SQLAlchemy
Recommends:     python-subunit2sql >= 1.8.0
%endif
BuildArch:      noarch
%python_subpackages

%description
stestr is a fork of the `testrepository`_ that concentrates on being a
dedicated test runner for python projects. The generic abstraction
layers which enabled testr to work with any subunit emitting runner are gone.
stestr hard codes python-subunit-isms into how it works. The code base is also
designed to try and be explicit, and to provide a python api that is documented
and has examples.

%prep
%setup -q -n stestr-%{version}
# do not test sql
rm stestr/tests/repository/test_sql.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/stestr
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand mkdir build/bin
for filepath in %{buildroot}/%{_bindir}/stestr*-%{$python_bin_suffix}; do
  filename=$(basename $filepath)
  unsuffixed=${filename/-%{$python_bin_suffix}/}
  cp $filepath build/bin/$unsuffixed
done
export PATH="$(pwd)/build/bin:$PATH"
export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix} -v stestr/tests
rm -r build/bin
}

%post
%python_install_alternative stestr

%postun
%python_uninstall_alternative stestr

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/stestr
%{python_sitelib}/*

%changelog
