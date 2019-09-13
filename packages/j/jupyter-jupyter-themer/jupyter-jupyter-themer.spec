#
# spec file for package jupyter-jupyter-themer
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


%bcond_without test
Name:           jupyter-jupyter-themer
Version:        0.4.0
Release:        0
Summary:        Custom CSS themer for jupyter notebooks
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/transcranial/jupyter-themer
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-themer/jupyter-themer-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       jupyter-notebook
Provides:       python3-jupyter_themer = %{version}
Obsoletes:      python3-jupyter_themer <= %{version}
Provides:       python3-jupyter-themer = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  jupyter-notebook
%endif

%description
Apply custom CSS styling to your jupyter notebooks.

%prep
%setup -q -n jupyter-themer-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc README.md
%license LICENSE
%{_bindir}/jupyter-themer
%{python3_sitelib}/jupyter_themer-%{version}-py*.egg-info
%{python3_sitelib}/jupythemer/

%changelog
