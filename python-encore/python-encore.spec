#
# spec file for package python-encore
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
Name:           python-encore
Version:        0.7.0
Release:        0
License:        LGPL-2.1 and Apache-2.0 and Python-2.0
Summary:        Low-level core modules for building Python applications
Url:            https://github.com/enthought/encore
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/e/encore/encore-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests}
BuildRequires:  python-futures
# /SECTION
Recommends:     python-requests
%ifpython2
Requires:       python-futures
%endif
BuildArch:      noarch

%python_subpackages

%description
This package consists of a collection of core utility packages useful
for building Python applications.  This package is intended to be at
the bottom of the software stack and have zero required external
dependencies aside from the Python Standard Library.

Packages:

  * Events: A package implementing a lightweight application-wide
    Event dispatch system.  Listeners can subscribe to events based
    on Event type or by filtering on event attributes.  Typical uses
    include UI components listening to low-level progress
    notifications and change notification for distributed resources.

  * Storage: Abstract base classes and concrete implementations of a
    basic key-value storage API. The API is intended to be general
    purpose enough to support a variety of local and remote storage
    systems.

  * Concurrent: A package of tools for handling concurrency within
    applications.

  * Terminal: Some utilities for working with text-based terminal
    displays.

%prep
%setup -q -n encore-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
