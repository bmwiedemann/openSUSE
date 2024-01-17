#
# spec file for package python-GooCalendar
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2016-2023 Dr. Axel Braun <DocB@opensuse.org>
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


%define         skip_python2 1
Name:           python-GooCalendar
Version:        0.8.0
Release:        0
Summary:        A calendar widget for GTK using PyGoocanvas
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://goocalendar.tryton.org/
Source:         https://files.pythonhosted.org/packages/source/G/GooCalendar/GooCalendar-%{version}.tar.gz
BuildRequires:  %{python_module Genshi}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A calendar widget for GTK using PyGoocanvas (Gnome widget linrary).

%prep
%setup -q -n GooCalendar-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README COPYRIGHT
%{python_sitelib}/goocalendar
%{python_sitelib}/GooCalendar-%{version}*-info

%changelog
