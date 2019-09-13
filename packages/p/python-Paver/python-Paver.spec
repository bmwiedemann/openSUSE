#
# spec file for package python-Paver
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
Name:           python-Paver
Version:        1.3.4
Release:        0
Summary:        Build, distribution and deployment scripting
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/paver/paver
Source:         https://files.pythonhosted.org/packages/source/P/Paver/Paver-%{version}.tar.gz
BuildRequires:  %{python_module cogapp}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Paver is a Python-based build/distribution/deployment scripting tool along the
lines of Make or Rake. Paver integrates with commonly
used Python libraries.

%prep
%setup -q -n Paver-%{version}
rm paver/docs/.buildinfo
chmod a-x paver/docs/*.*
chmod a-x paver/docs/*/*.*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/paver

%check
%python_exec setup.py test

%post
%python_install_alternative paver

%preun
%python_uninstall_alternative paver

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%doc paver/docs/
%python_alternative %{_bindir}/paver
%{python_sitelib}/paver/
%{python_sitelib}/Paver-%{version}-py*.egg-info

%changelog
