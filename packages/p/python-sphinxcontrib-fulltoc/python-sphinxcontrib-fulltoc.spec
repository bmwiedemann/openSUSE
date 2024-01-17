#
# spec file for package python-sphinxcontrib-fulltoc
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sphinxcontrib-fulltoc
Version:        1.2.0
Release:        0
Summary:        Include a full table of contents in your Sphinx HTML sidebar
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://sphinxcontrib-fulltoc.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-fulltoc/sphinxcontrib-fulltoc-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION docs
BuildRequires:  python3-Sphinx
# /SECTION
%python_subpackages

%description
sphinxcontrib-fulltoc is an extension for the Sphinx_ documentation
system that changes the HTML output to include a more detailed table
of contents in the sidebar. By default Sphinx only shows the local
headers for the current page. With the extension installed, all of the
page titles are included, and the local headers for the current page
are also included in the appropriate place within the document.

%prep
%setup -q -n sphinxcontrib-fulltoc-%{version}
sed -i 's/version = subprocess.*/version = "%{version}"/' docs/source/conf.py

%build
%python_build
#pushd docs
#LANG=C.UTF-8 READTHEDOCS=True PYTHONPATH=.. make html
#rm build/html/.buildinfo
#popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc ChangeLog README.rst
#docs/build/html

%changelog
