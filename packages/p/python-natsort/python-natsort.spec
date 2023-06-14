#
# spec file for package python-natsort
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-natsort
Version:        8.2.0
Release:        0
Summary:        Natural sorting in Python
License:        MIT
URL:            https://github.com/SethMMorton/natsort
Source:         https://files.pythonhosted.org/packages/source/n/natsort/natsort-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest >= 4.3}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%autopatch -p1

%build
%python_build

%install
%python_install

export PYTHONPATH=%{buildroot}%{python_sitelib}
help2man -o natsort.1 -N %{buildroot}%{_bindir}/natsort
install -Dm0644 natsort.1 %{buildroot}%{_mandir}/man1/natsort.1

%python_clone -a %{buildroot}%{_bindir}/natsort
%python_clone -a %{buildroot}%{_mandir}/man1/natsort.1

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%pytest --hypothesis-profile=slow-tests

%post
%python_install_alternative natsort natsort.1

%postun
%python_uninstall_alternative natsort

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%python_alternative %{_bindir}/natsort
%python_alternative %{_mandir}/man1/natsort.1%{?ext_man}
%{python_sitelib}/natsort
%{python_sitelib}/natsort-%{version}*-info

%changelog
