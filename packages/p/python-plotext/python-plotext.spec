#
# spec file for package python-plotext
#
# Copyright (c) 2026 SUSE LLC and contributors
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

# affects the python macros even if not used in the spec file
%bcond_without libalternatives

%{?sle15_python_module_pythons}
%define pyname plotext
Name:           python-%{pyname}
Version:        5.3.2
Release:        0
Summary:        Plots directly on terminal
License:        BSD-3-Clause
URL:            https://github.com/piccolomo/%{pyname}
Source:         https://files.pythonhosted.org/packages/source/p/%{pyname}/%{pyname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
plotext plots directly on terminal
* it allows for scatter, line, bar, histogram and date-time plots (including candlestick),
* it can also plot error bars, confusion matrices, and add extra text, lines and shapes to the plot,
* you could use it to plot images (including GIFs) and stream video with audio (including YouTube),
* it can save plots as text or as colored html,
* it provides a simple function to color strings,
* it comes with a dedicated command line tool

%prep
%autosetup -n %{pyname}-%{version}
chmod 644 LICENSE README.md
sed -i "s#env python#python3#" %{pyname}/%{pyname}_cli.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod 755 %{buildroot}%{$python_sitelib}/%{pyname}/%{pyname}_cli.py
%python_clone -a %{buildroot}%{_bindir}/%{pyname}

%check

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{pyname}
%{python_sitelib}/%{pyname}-%{version}.dist-info
%python_alternative %{_bindir}/%{pyname}

%changelog
