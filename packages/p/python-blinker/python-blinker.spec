#
# spec file for package python-blinker
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-blinker
Version:        1.4
Release:        0
Summary:        Object-to-object and broadcast signaling in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://pythonhosted.org/blinker/
Source:         https://files.pythonhosted.org/packages/source/b/blinker/blinker-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Blinker provides a dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%package -n python-blinker-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Provides:       %{python_module blinker-doc = %{version}}

%description -n python-blinker-doc
Blinker provides a dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

This sub-package contains the HTML documentation.

%prep
%setup -q -n blinker-%{version}
# remove unneded doc file that trigger rpmlint
rm docs/html/objects.inv

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec %{_bindir}/nosetests-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.md
%{python_sitelib}/blinker-%{version}-py%{python_version}.egg-info
%{python_sitelib}/blinker

%files -n python-blinker-doc
%doc docs/html

%changelog
