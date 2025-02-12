#
# spec file for package python-Mathics-Django
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


%define modname Mathics_Django
%define skip_python313 1
Name:           python-Mathics-Django
Version:        8.0.1
Release:        0
Summary:        A Django front end for Mathics3
# Mathics itself is licensed as GPL-3.0 but it includes third-party software with MIT, BSD-3-Clause, and Apache-2.0 Licensing; also includes data from wikipedia licensed under CC-BY-SA-3.0 and GFDL-1.3
License:        Apache-2.0 AND BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            https://mathics.org/
Source:         https://files.pythonhosted.org/packages/source/m/mathics-django/Mathics_Django-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module django}
BuildRequires:  %{python_module Mathics-Scanner >= 1.4.1}
BuildRequires:  %{python_module Mathics3 >= 8.0.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module networkx >= 3.0}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
BuildRequires:  fdupes
Requires:       python-django
Requires:       python-Mathics-Scanner >= 1.4.1
Requires:       python-Mathics3 >= 8.0.0
Requires:       python-matplotlib
Requires:       python-networkx >= 3.0
Requires:       python-pygments
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
%{name} provides a Django front end for Mathics3, integrating GUI and help
browser.

%prep
%autosetup -p1 -n mathics_django-%{version}
find ./ -name *~ -delete -print
find ./mathics_django/web/ -name *.js -exec chmod -x {} \;
sed -Ei "1{\@^#\!/usr/bin/env python@d}" ./mathics_django/{docpipeline,manage,server}.py
sed -Ei "1{\@^#\!/usr/bin/env python@d}" ./mathics_django/web/{authentication,forms}.py
sed -Ei "1{\@^#\!/usr/bin/env python@d}" ./mathics_django/web/templatetags/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mathicsserver
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # Tests
export PYTHONPATH=%{buildroot}%{$python_sitelib}
export MPLCONFIGDIR=`mktemp -d -p .`
export HOME=${PWD}
$python %{buildroot}%{$python_sitelib}/mathics_django/manage.py test test_django
}

%post
%python_install_alternative mathicsserver

%postun
%python_uninstall_alternative mathicsserver

%files %{python_files}
%python_alternative %{_bindir}/mathicsserver
%{python_sitelib}/mathics_django/
%{python_sitelib}/%{modname}-%{version}.dist-info/

%changelog
