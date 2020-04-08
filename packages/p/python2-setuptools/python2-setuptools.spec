#
# spec file for package python2-setuptools
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


Name:           python2-setuptools
Version:        44.0.0
Release:        0
Summary:        Enhancements to distutils for building and distributing Python packages
License:        MIT
URL:            https://github.com/pypa/setuptools
Source:         https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.zip
Patch0:         sort-for-reproducibility.patch
Patch1:         importlib.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-base
BuildRequires:  unzip
# The dependency download feature may require SSL, which is in python3-base and python(2)
Requires:       python2
Requires:       python2-base
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     ca-certificates-mozilla
Provides:       python-distribute = %{version}
Obsoletes:      python-distribute < %{version}
BuildArch:      noarch

%description
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages,
especially ones that have dependencies on other packages.

%prep
%setup -q -n setuptools-%{version}
%autopatch -p1

# # strip shebangs to fix rpmlint warnings
sed -r -i '1s@^#!/.*$@@' setuptools/command/easy_install.py \
    pkg_resources/_vendor/appdirs.py

%build
%python2_build

%install
%python2_install
%prepare_alternative easy_install
%fdupes %{buildroot}%{python2_sitelib}

%post
%python_install_alternative easy_install

%postun
%python_uninstall_alternative easy_install

%files
%license LICENSE
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/easy_install
%{python2_sitelib}/setuptools
%{python2_sitelib}/setuptools-%{version}-py*.egg-info
%{python2_sitelib}/easy_install.py*
%dir %{python2_sitelib}/pkg_resources
%{python2_sitelib}/pkg_resources/*

%changelog
