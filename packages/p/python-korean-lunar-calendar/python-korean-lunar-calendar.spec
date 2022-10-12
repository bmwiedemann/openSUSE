#
# spec file for package python-korean-lunar-calendar
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
%define modname korean_lunar_calendar
Name:           python-korean-lunar-calendar
Version:        0.3.1
Release:        0
Summary:        Korean Lunar Calendar
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.org/project/korean-lunar-calendar/
Source:         https://files.pythonhosted.org/packages/source/k/korean_lunar_calendar/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Provides:       python-%{modname} = %{version}-%{release}
%python_subpackages

%description
This is GUI for GPaste clipboard manager for Gnome Shell. It
allows to paste, edit and search through clipboard history. GUI
display can be toggled with keyboard shortcut so is easy to
use without mouse.

%prep
%setup -q -n korean_lunar_calendar-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%doc *.rst
%license LICENSE
%{python_sitelib}/korean_lunar_calendar
%{python_sitelib}/korean_lunar_calendar-%{version}-py*.egg-info

%changelog
