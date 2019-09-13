#
# spec file for package python-PsyLab
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-PsyLab
Version:        0.4.7.12
# For license file
%define tag     f6006806c966d5dc8cca93aafe0c212c6d38995d
Release:        0
License:        GPL-3.0+
Summary:        PsyLab: Psychophysics Lab
Url:            https://bitbucket.org/cbrown1/psylab
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/py2.py3/P/PsyLab/PsyLab-%{version}-py2.py3-none-any.whl
Source10:       https://raw.githubusercontent.com/psylab16/psylab/%{tag}/COPYING
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module matplotlib >= 1.2}
BuildRequires:  %{python_module numpy >= 1.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 0.12}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.2
Requires:       python-scipy >= 0.12
Requires:       python-matplotlib >= 1.2
BuildArch:      noarch

%python_subpackages

%description
Psylab is a loose collection of modules useful for various aspects of
running psychophysics experiments, although some might be more
generally useful.

%prep
%setup -c -T
cp %{SOURCE10} .

%build
# Not Needed

%install
%python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%{python_sitelib}/*

%changelog
