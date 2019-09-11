#
# spec file for package jupyter-jupyterbgnotify
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           jupyter-jupyterbgnotify
Version:        0.2.1
Release:        0
License:        BSD-3-Clause
Summary:        A Jupyter Notebook %%magic for Browser Notifications of Cell Completion
Url:            https://github.com/benmanns/jupyterbgnotify
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jupyterbgnotify/jupyterbgnotify-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
# SECTION test requirements
BuildRequires:  python3-ipython
BuildRequires:  jupyter-notebook
# /SECTION
BuildRequires:  fdupes
Requires:       python3-ipython
Requires:       jupyter-notebook
BuildArch:      noarch

%description
A Jupyter Notebook %%magic for Browser Notifications of Cell Completion

%prep
%setup -q -n jupyterbgnotify-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc AUTHORS.txt README.rst
%license LICENSE.txt
%{python3_sitelib}/jupyterbgnotify-%{version}-py*.egg-info
%{python3_sitelib}/jupyterbgnotify/


%changelog
