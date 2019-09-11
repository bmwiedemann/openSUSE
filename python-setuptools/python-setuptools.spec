#
# spec file for package python-setuptools
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
%define oldpython python
Name:           python-setuptools
Version:        41.0.1
Release:        0
Summary:        Enhancements to distutils for building and distributing Python packages
License:        Python-2.0 OR ZPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pypa/setuptools
Source:         https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.zip
Source1:        psfl.txt
Source2:        zpl.txt
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
#!BuildIgnore:  python2-pyparsing
#!BuildIgnore:  python3-pyparsing
# needed for SLE
Requires:       python
Requires:       python-appdirs
Requires:       python-packaging
Requires:       python-six
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Recommends:     ca-certificates-mozilla
%endif
# NOTE(saschpe): Distribute was merged into 0.7.x, so even though distribute
# obsoletes setuptools < 0.6.45, current setuptools obsoletes distribute again
%ifpython2
Provides:       %{oldpython}-distribute = %{version}
Obsoletes:      %{oldpython}-distribute < %{version}
%endif
%python_subpackages

%description
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages,
especially ones that have dependencies on other packages.

%prep
%setup -q -n setuptools-%{version}
find . -type f -name "*.orig" -delete

# fix rpmlint spurious-executable-perm
chmod -x README.rst

# strip shebangs to fix rpmlint warnings
# "explain the sed":
# 1 = first line only
# s@...@...@ = same as s/.../.../ except with @ instead of /
# ^ = start; #!/ = shebang leading characters; .* = rest of line; $ = end
# replace with nothing
sed -r -i '1s@^#!/.*$@@' setuptools/command/easy_install.py

%build
%python_build

%install
%python_install
%prepare_alternative easy_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Can not run testsuite as this introduces build cycle
#%%check
#export LANG="en_US.UTF-8"
#python setup.py ptr --addopts='-rxs'

%post
%python_install_alternative easy_install

%postun
%python_uninstall_alternative easy_install

%files %{python_files}
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/easy_install
%{python_sitelib}/setuptools
%{python_sitelib}/setuptools-%{version}-py%{python_version}.egg-info
%{python_sitelib}/easy_install.py*
%pycache_only %{python_sitelib}/__pycache__/easy_install.*
%dir %{python_sitelib}/pkg_resources
%{python_sitelib}/pkg_resources/*

%changelog
