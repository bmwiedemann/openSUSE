#
# spec file for package python-pygtkspellcheck
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


%define modname gtkspellcheck
Name:           python-pygtkspellcheck
Version:        5.0.3
Release:        0
Summary:        A spellchecking library for GTK written in pure Python
License:        GPL-3.0-or-later
URL:            https://github.com/koehlma/pygtkspellcheck
Source:         https://files.pythonhosted.org/packages/source/p/pygtkspellcheck/pygtkspellcheck-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gobject >= 3.42.1
Requires:       python-pyenchant >= 3.0
Provides:       python-%{modname} = %{version}
BuildArch:      noarch
%python_subpackages

%description
Python GTK Spellcheck is a simple but quite powerful spellchecking library for
GTK written in pure Python. Its spellchecking component is based on Enchant and
it supports both GTK 3 and 4 via PyGObject.

%prep
%autosetup -p1 -n pygtkspellcheck-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/py%{modname}-%{version}*.*-info

%changelog
