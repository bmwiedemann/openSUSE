#
# spec file for package python-liblarch
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Dominique Leuenberger, Amsterdam, The Netherlands.
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
#


%define         _name liblarch
%define         _name_gtk liblarch_gtk
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-liblarch
Version:        3.0
Release:        0
Summary:        A Python library to handle data structure
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://live.gnome.org/liblarch
Source:         https://github.com/getting-things-gnome/%{_name}/archive/v%{version}.tar.gz
Patch0:         libarch-py2compat.patch
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
BuildRequires:  typelib(Gtk) >= 3.0
Requires:       python-gobject
BuildArch:      noarch
%python_subpackages

%description
Liblarch is a Python library built to handle data structure such
are lists, trees and acyclic graphs (tree where nodes can have multiple
parents)

%package gtk
Summary:        GTK bindings for liblarch
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-gobject
Requires:       typelib(Gtk) >= 3.0

%description gtk
Liblarch is a Python library built to handle data structure such
are lists, trees and acyclic graphs (tree where nodes can have multiple
parents)

This package provides GTK bindings for liblarch.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# TESTS fail with segf, local execution works
#%check
#%%python_expand xvfb-run nosetests-%{$python_bin_suffix} tests

%files %{python_files}
%license LICENSE
%doc README.md AUTHORS
%{python_sitelib}/%{_name}
%{python_sitelib}/%{_name}*.egg-info

%files %{python_files gtk}
%license LICENSE
%{python_sitelib}/%{_name_gtk}/

%changelog
