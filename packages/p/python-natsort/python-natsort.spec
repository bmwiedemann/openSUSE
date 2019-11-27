#
# spec file for package python-natsort
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define skip_python2 1
Name:           python-natsort
Version:        6.2.0
Release:        0
Summary:        Natural sorting in Python
License:        MIT
URL:            https://github.com/SethMMorton/natsort
Source:         https://files.pythonhosted.org/packages/source/n/natsort/natsort-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
BuildRequires:  python2-pathlib
Requires:       python-setuptools
Recommends:     python-PyICU >= 1.0.0
Recommends:     python-fastnumbers >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Natsort provides a function natsorted that helps sort lists
"naturally" ("naturally" is rather ill-defined, but in general it means
sorting based on meaning and not computer code point).

%prep
%setup -q -n natsort-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

export PYTHONPATH=%{buildroot}%{python3_sitelib}
help2man -o natsort.1 -N %{buildroot}%{_bindir}/natsort
install -Dm0644 natsort.1 %{buildroot}%{_mandir}/man1/natsort.1

%check
export LANG=en_US.UTF8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
pytest-%{$python_bin_suffix}
}

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{_mandir}/man1/natsort.1%{ext_man}
%{_bindir}/natsort
%{python_sitelib}/natsort*

%changelog
