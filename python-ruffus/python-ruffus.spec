#
# spec file for package python-ruffus
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-ruffus
Version:        2.8.3
Release:        0
Summary:        Python computational pipeline management package
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.ruffus.org.uk
Source:         https://files.pythonhosted.org/packages/source/r/ruffus/ruffus-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The Ruffus module is a way to add support for running computational pipelines.

%prep
%setup -q -n ruffus-%{version}
sed -i -e '/^#!\//, 1d' ruffus/*.py
sed -i -e '/^#! \//, 1d' ruffus/*.py
sed -i -e '/^#!\//, 1d' ruffus/test/*.py
sed -i -e '/^#! \//, 1d' ruffus/test/*.py
sed -i -e '/^#!\//, 1d' ruffus/test/*.cmd
sed -i -e '/^#! \//, 1d' ruffus/test/*.cmd
chmod a-x ruffus/*.py
chmod a-x ruffus/test/*.cmd
chmod a-x ruffus/test/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd ruffus/test
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
export PYTHONDONTWRITEBYTECODE=1
for f in test_*.py; do
pytest-%{$python_bin_suffix} $f
done
for f in check_*.py; do
$python $f
done
}
popd

%files %{python_files}
%doc CHANGES.TXT README.rst
%license LICENSE.TXT
%{python_sitelib}/*

%changelog
