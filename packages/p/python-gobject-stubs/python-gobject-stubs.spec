#
# spec file for package python-gobject-stubs
#
# Copyright (c) 2025 SUSE LLC
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

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "gtk3"
%define with_gtk3 1
%endif

%define src_name pygobject_stubs
%define pname python-gobject-stubs
%define psuffix %{?with_gtk3:-gtk3}%{!?with_gtk3:%{nil}}

Name:           %{pname}%{psuffix}
Version:        2.14.0
Release:        0
Summary:        Typing stubs for PyGObject
License:        LGPL-2.1-only
URL:            https://github.com/pygobject/pygobject-stubs
Source:         https://files.pythonhosted.org/packages/source/P/PyGobject-stubs/pygobject_stubs-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  gobject-introspection
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-base >= 3.9
Requires:       python-gobject
Requires:       python-gobject-Gdk
%if 0%{?with_gtk3}
Conflicts:      python-gobject-stubs
%endif
BuildArch:      noarch
%python_subpackages

%description
This package provides typing stubs for python-gobject to (typically) allow IDEs
to provide helpful completion guides and documentation about python-gobject
related modules.

%if 0%{?with_gtk3}
This package provides PyGObject stubs for Gtk3.
%else
This package provides PyGObject stubs for Gtk4.
%endif

%prep
%autosetup -p1 -n %{src_name}-%{version}

%build
%if 0%{?with_gtk3}
export PYGOBJECT_STUB_CONFIG=Gtk3,Gdk3,Soup2
%endif
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/gi-stubs/
%{python_sitelib}/%{src_name}-%{version}.dist-info/

%changelog
