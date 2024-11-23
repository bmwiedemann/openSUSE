#
# spec file for package python-nbformat
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-nbformat
Version:        5.10.4
Release:        0
Summary:        The Jupyter Notebook format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/nbformat
Source:         https://github.com/jupyter/nbformat/releases/download/v%{version}/nbformat-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE no-hatch-nodejs-version.patch mcepl@suse.com
# We don’t need hatch-nodejs-version dependency
Patch0:         no-hatch-nodejs-version.patch
# PATCH-FEATURE-OPENSUSE no-pep440.patch mcepl@suse.com
# We don’t need pep440 check either
Patch1:         no-pep440.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-fastjsonschema >= 2.15
Requires:       python-jsonschema > 2.6
Requires:       python-traitlets >= 5.1
Requires:       (python-jupyter_core >= 4.12 with (python-jupyter_core < 5 or python-jupyter_core >= 5.1))
Provides:       python-jupyter_nbformat = %{version}-%{release}
Obsoletes:      python-jupyter_nbformat < %{version}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module fastjsonschema >= 2.15}
BuildRequires:  %{python_module jsonschema > 2.6}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module traitlets >= 5.1}
BuildRequires:  %{pythons}
BuildRequires:  %{python_module jupyter_core >= 4.12 with (%python-jupyter_core < 5 or %python-jupyter_core >= 5.1)}
# /SECTION
%python_subpackages

%description
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.

This package provides the python interface.

%prep
%autosetup -p1 -n nbformat-%{version}
sed -i -e 's/"--color=yes", //' -e 's/\@\@\@/%{version}/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-trust
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%fdupes %{buildroot}%{_docdir}/jupyter-nbformat/

%check
# gh#jupyter/nbformat#405
%pytest  -p no:unraisableexception

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter-trust

%post
%python_install_alternative jupyter-trust

%postun
%python_uninstall_alternative jupyter-trust

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative jupyter-trust
%{python_sitelib}/nbformat/
%{python_sitelib}/nbformat-%{version}.dist-info/

%changelog
